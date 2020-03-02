
import logging
import multiprocessing
from multiprocessing import Process, freeze_support, Lock, current_process, Value, Array, RawArray, RawValue

import numpy as np
import time
import cv2, imutils

class NP_SharedMemory:
    """
    Controls access to shared memory for the main and camera processes
    https://research.wmz.ninja/articles/2018/03/on-sharing-large-arrays-when-using-pythons-multiprocessing.html
    https://docs.python.org/3/library/multiprocessing.html
    https://dzone.com/articles/python-201-a-multiprocessing-tutorial
    https://docs.python.org/3.7/library/multiprocessing.html#synchronization-primitives
    """

    def __init__(self, shape, name='demo'):
        self.shape = shape
        self.name = name
        self.paint = Value('B', False)
        self.stop  = Value('B', False)
        self.start = Value('B', 0)
        self.lock = Lock()

        # create shared buffer buf_mp
        self._arr_mp = Array('B', shape[0] * shape[1] * shape[2])
        self.arr = None   # need to call set_local_np_view in local process

    def set_local_np_view(self):
        """ run this within the local process to create a local NP view of the shared memory """
        # Wrap buf_mp as an numpy array so we can easily manipulates its data.
        self.arr = np.frombuffer(self._arr_mp.get_obj(), dtype=np.uint8).reshape(self.shape)
        print(f'{current_process} - {self.name}: Setting up Local NP Buffer: { self.arr.shape}')


def demo_camera_process(sm:NP_SharedMemory,):
    """ Run a separate process to process and decode camera frames """
    sm.set_local_np_view()
    i = 0
    last_access = time.time()
    cam_running = True

    while not sm.stop.value:
        time.sleep(0.1)
        # sm.lock.acquire()
        try:
            if sm.start.value:
                last_access = time.time()
                print(f'Cam {sm.name}: Stream Start: i = {i}')
                sm.start.value = False
                cam_running = True
                i = 0

            if time.time() - last_access > 2:
                if cam_running:
                    print(f'Cam {sm.name}: Stream Idle : i = {i}')
                    cam_running = False

            if cam_running:
                # fill buffer
                sm.arr += 1
                cv2.putText(sm.arr, f"frame: {i}",
                            (sm.shape[1]//4, sm.shape[0]//2), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 10)

                sm.paint.value = True
                i = i + 1

        except KeyboardInterrupt:
            print("Cam: KeyboardInterrupt")
            pass

        # sm.lock.release()

    print('Cam: Stop')



if __name__ == '__main__':
    # freeze_support() # for MS Windows
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

    p1 = Process(target=demo_camera_process, args=(sm1,)).start()
    p2 = Process(target=demo_camera_process, args=(sm2,)).start()

    i = 10
    sm1.start.value = True
    while True:
        time.sleep(0.1)

        # sm1.lock.acquire()
        try:
            if sm1.paint.value:
                cv2.imshow(sm1.name, sm1.arr)
                sm1.paint.value = False

            if sm2.paint.value:
                cv2.imshow(sm2.name, sm2.arr)
                sm2.paint.value = False

            k = cv2.waitKey(1)
            txt = None
            if k == 27 or k == 3:
                # sm1.stop.value = True
                break  # esc to quit
            elif k == ord('s'):
                sm1.start.value = False
                sm2.start.value = False
                # i = 0

            elif k == ord('g'):
                sm1.start.value = True
                sm2.start.value = True
                # i = 10
        except KeyboardInterrupt:
            print("Main: KeyboardInterrupt")
            break

        # sm1.lock.release()

    print('Main: End of program')

    sm1.stop.value = True
    sm2.stop.value = True

    # sm1.lock.release()
    # time.sleep(2)
    print('Main: join')
    p1.join()
    p2.join()
    print('Main: bye')
    cv2.destroyAllWindows()
