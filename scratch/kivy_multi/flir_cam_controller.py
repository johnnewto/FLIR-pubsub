"""
This is designed the spread each FLIR camera jpeg decoding to a separate process so not to block the main python process
the interprocess communication is via shared memory
"""
__all__ = ['NP_SharedMemory', 'SpinProcess', 'fake_camera_process', 'flir_camera_process', 'VideoCapture']
import logging
import multiprocessing
from multiprocessing import Process, freeze_support, Lock, current_process, Value, Array

import numpy as np
import time
import cv2, imutils, os

from FLIR_pubsub import FLIR_client_utils as flir
width = 1000
height = 750

class NP_SharedMemory:
    """
    Controls access to shared memory for the main and camera processes
    https://research.wmz.ninja/articles/2018/03/on-sharing-large-arrays-when-using-pythons-multiprocessing.html
    https://docs.python.org/3/library/multiprocessing.html
    https://dzone.com/articles/python-201-a-multiprocessing-tutorial
    https://docs.python.org/3.7/library/multiprocessing.html#synchronization-primitives
    https://docs.python.org/3.7/library/array.html#module-array
    Note for Windows:
        https://docs.python.org/2/library/multiprocessing.html#windows

    """

    def __init__(self, shape, name='demo'):
        # self.shape = shape
        self.name = name
        self._paint = Value('B', False) # signal ready to _paint , 'B' unsigned char
        self._stop  = Value('B', False) # signal _stop process
        self._kick = Value('B', 0) # _kick to keep awake
        # self._lock = Lock()
        self._width = Value('I', 0) # 'I' unsigned int
        self._height = Value('I', 0) # 'I' unsigned int

        # create shared buffer buf_mp
        self._base_arr:Array = Array('B', 4000*3000*3)  # largest size
        # self._base_arr:Array = Array('B', shape[0] * shape[1] * shape[2])
        self.arr = None   # need to call set_local_np_view in local process

    def set_local_np_view(self):
        """ run this within the local process to create a local NP view of the shared memory """
        # Wrap buf_mp as an numpy array so we can easily manipulates its data.
        # self.arr = np.frombuffer(self._arr_mp.get_obj(), dtype=np.uint8).reshape(self.shape)
        self.arr = np.frombuffer(self._base_arr.get_obj(), dtype=np.uint8)  # No reshape i.e flat
        print(f'{current_process().name} PID:{os. getpid()} - {self.name}: Setting up local numpy array view: {self.arr.shape} of {self.arr.dtype}')
    def close(self):
        ''' not sure if we need this'''
        del self._base_arr


def FLIR_camera_process(sm:NP_SharedMemory, name='', url='localhost'):
    """ Received frames from a single camera. Must have the server running"""
    chan = flir.FLIR_Client(name=name, url=url)
    i = 0
    while not sm._stop.value:
        try:
            frame, topic, md = chan.read_image()

        except KeyboardInterrupt:
            break
        k = cv2.waitKey(10)
        if k == 27 or k == 3:
           break  # esc to quit

        if frame is not None:
            frame = imutils.resize(frame, width=width, height=height)
            cv2.putText(frame, f"{md['framedata']['frameid']}",
                        (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)
            cv2.imshow(topic, frame)

            txt = None
            if k == ord('c'):
                i = 0
                txt = f'Reset name to {topic}-{i}.jpg'
            elif k >= ord('s'):
                txt = f'Saving {topic}-{i}.jpg'
                cv2.imwrite(f'{topic}-{i}.jpg', frame)
                i += 1
            if txt is not None:
                print(txt)
                cv2.putText(frame, txt, (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)
                cv2.imshow(topic, frame)
                cv2.waitKey(1000)

    chan.close()
    cv2.destroyAllWindows()

    print('Finished')
    print("[INFO] approx. FPS: {:.2f}".format(chan.fps.fps()))

class SpinProcess():
    '''
    Spin a multiprocess with controlls to read a  shared numpy array
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    '''
    def __init__(self, target=None, sharemem=None):
        self.sm = sharemem
        self.proc = Process(target=target, args=(sharemem,))
        self.proc.start()

    def read(self, kick=True):
        ''' read the process across shared memory '''
        if kick: self.sm._kick.value = True  # kick signal keep process from idle
        # todo JN could restart process if stopped
        shape = (self.sm._height.value, self.sm._width.value, 3)
        if self.sm._paint.value and shape[0]*shape[0] > 10000:
            # .reshape()
            # self.sm.arr.shape = shape
            ret = self.sm
            self.sm._paint.value = False
            return ret
        else:
            return None

    def kick(self):
        ''' kick the process to keep alive '''
        # todo JN could restart process if stopped
        self.sm._kick.value = True

    def shutdown(self):
        ''' shutdown process'''
        self.sm._stop.value = True

    def set_stop(self):
        ''' shutdown process'''
        self.sm._stop.value = True

    def get_paint(self):
        return sm1._paint.value
    def set_paint(self, val):
        sm1._paint.value = val

    def join(self):
        self.sm._stop.value = True
        self.proc.join()

    def release(self):
        self.sm._stop.value = True
        self.proc.join()

class VideoCapture():
    """ Return a videocapture view of the spin process read """
    def __init__(self, src=None, sharemem=None):
        self.src = src
        self._proc = SpinProcess(target=src, sharemem=sharemem)
        self._open = True

    def getBacendName(self):
            return "flir_cam_controller"

    def read(self, kick=True):
        # todo JN could restart process if stopped
        return self._proc.read()

    def isOpened(self):
        return self._open

    def kick(self):
        self._proc._kick()

    def release(self):
        self._open = False
        self._proc.shutdown()

import time
import FLIR_pubsub.FLIR_client_utils as fcu


def fake_camera_process(sm:NP_SharedMemory,):
    """ Run a fake or test separate process to process and decode camera frames """
    sm.set_local_np_view()
    i = 0
    last_access = time.time()
    cam_idle = False
    IDLE_TIMEOUT = 5

    while not sm._stop.value:
        # sm._lock.acquire()
        try:
            if sm._kick.value:
                last_access = time.time()
                # print(f'Cam {sm.name}: Stream Start: i = {i}')
                sm._kick.value = False
                cam_idle = False

            if time.time() - last_access > IDLE_TIMEOUT:
                if not cam_idle:
                    print(f'Cam {sm.name}: Stream Idle : i = {i}')
                    cam_idle = True

            if not cam_idle:
                # do work
                time.sleep(0.01)
                # do some hard work for 10 msec
                start = time.monotonic()
                while time.monotonic() - start < 0.01:
                    pass
                # fill buffer with fake data
                arr = np.ones((2000//2,3000//2,3), dtype=np.uint8)*33
                # arr = np.ones((2000, 3000, 3), dtype=np.uint8) * 33
                arr += 10  # here just inc by 1
                cv2.putText(arr, f"{i} : FLIR ",
                            (arr.shape[1]//20, arr.shape[0]//2), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 10)
                sm._width.value = arr.shape[1]
                sm._height.value = arr.shape[0]
                # arr = np.flipud(arr).ravel() # kivy requires flipping
                sm.arr[:arr.size] = arr.ravel()
                # np.copyto(sm.arr[:arr.size], arr)
                sm._paint.value = True
                i = i + 1
            else:
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("Cam: KeyboardInterrupt")
            pass

        # sm._lock.release()

    print('Cam: _stop')

def flir_camera_process(sm:NP_SharedMemory,):
    """ start a client socket process to process and decode remote FLIR camera frames """
    name = 'FrontLeft'
    url = 'localhost'
    client = fcu.FLIR_Client(name=name, url=url)

    sm.set_local_np_view()
    i = 0
    last_access = time.time()
    cam_idle = False
    IDLE_TIMEOUT = 5

    while not sm._stop.value:
        # sm._lock.acquire()
        try:
            if sm._kick.value:
                last_access = time.time()
                # print(f'Cam {sm.name}: Stream Start: i = {i}')
                sm._kick.value = False
                cam_idle = False

            if time.time() - last_access > IDLE_TIMEOUT:
                if not cam_idle:
                    print(f'Cam {sm.name}: Stream Idle : i = {i}')
                    cam_idle = True

            if not cam_idle:

                time.sleep(0.01)
                # # do some hard work for 10 msec
                # start = time.monotonic()
                # while time.monotonic() - start < 0.01:
                #     pass
                # fill buffer
                arr, name, md = client.read_image()


                if arr is not None:
                    arr = imutils.resize(arr, width=1200)
                    cv2.putText(arr, f"{i}",
                                (arr.shape[1]//20, arr.shape[0]//2), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 10)
                    sm._width.value = arr.shape[1]
                    sm._height.value = arr.shape[0]
                    # arr = np.flipud(arr).ravel() # kivy requires flipping
                    sm.arr[:arr.size] = arr.ravel()
                    # np.copyto(sm.arr[:arr.size], arr)

                    # sm.arr += 1  # here just inc by 1

                    sm._paint.value = True
                    i = i + 1
                else:
                    time.sleep(0.01)
            else:
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("Cam: KeyboardInterrupt")
            pass

        # sm._lock.release()

    print('Cam: _stop')


if __name__ == '__main__':
    ''' Test the above of the using fake data and cv2.namedWindow() view '''
    freeze_support() # The freeze_support() line can be omitted if the program will be run normally instead of frozen.
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    # # shared memory
    sm1 = NP_SharedMemory((2000, 3000, 3), name='camera_1')
    sm1.set_local_np_view()

    sm2 = NP_SharedMemory((2000, 3000, 3), name='camera_2')
    sm2.set_local_np_view()

    cv2.namedWindow(sm1.name, cv2.WINDOW_NORMAL )
    cv2.namedWindow(sm2.name, cv2.WINDOW_NORMAL )
    p1 = SpinProcess(target=fake_camera_process, sharemem=sm1)
    vc2 = VideoCapture(src=fake_camera_process, sharemem=sm2)

    while True:
        try:
            time.sleep(0.1)

            arr = p1.read(kick=False)  # dont kick process to test idle state
            if arr is not None:
                cv2.imshow(sm1.name, arr)

            arr = vc2.read()
            if arr is not None:
                cv2.imshow(sm2.name, arr)

            k = cv2.waitKey(1)
            txt = None
            if k == 27 or k == 3:
                break  # esc to quit
            elif k == ord('s'):
                p1.shutdown()
                vc2.release()
            elif k == ord('g'):
                p1.kick()
                vc2.kick()
        except KeyboardInterrupt:
            print("Main: KeyboardInterrupt")
            break

    print('Main: End of program')
    p1.release()
    vc2.release()


    cv2.destroyAllWindows()
