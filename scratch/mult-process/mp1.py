# from multiprocessing import Process
#
#
# def print_func(continent='Asia'):
#     print('The name of continent is : ', continent)
#
# if __name__ == "__main__":  # confirms that the code is under main function
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)  # instantiating without any argument
#     procs.append(proc)
#     proc.start()
#
#     # instantiating process with arguments
#     for name in names:
#         # print(name)
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#
#     # complete the processes
#     for proc in procs:
#         proc.join()
#


# from multiprocessing import Process, Queue
# import numpy as np
# import time
# arr = np.ones((2000,3000, 3), dtype=np.uint8)
# def f(q):
#     while True:
#         q.put(arr)
#         time.sleep(0.1)
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#
#     print (q.get().shape )   # prints "[42, None, 'hello']"
#     p.join()

# import os
import logging
import multiprocessing
from multiprocessing import Process, freeze_support, Queue, current_process, Lock
from queue import Empty, Full

import numpy as np
import time

lock = Lock()

def camera_process(qcam, qcntr):
    arr = np.ones((2000, 3000, 3), dtype=np.uint8)
    i = 0
    stop = False
    while not stop:
        try:
            qcam.put(arr, block=True)
            time.sleep(0.5)
            try:
                g = qcntr.get(block=True, timeout=1)
            except Empty:
                pass
            print('Cam:', i)
            # time.sleep(0.5)
            i += 1

            if g == 'stop':
                stop = True
                print('Cam:  Stop Receieved')
            if i == 5:
                # qcntr.put('stop', block=True)
                pass
                # break
        except KeyboardInterrupt:
            print("Cam: KeyboardInterrupt")
            pass

    print('Cam: end of code')


if __name__ == '__main__':
    # freeze_support() # for MS Windows
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    qcam = Queue()
    qcntr = Queue()
    p = Process(target=camera_process, name='camera_process', args=(qcam, qcntr,))
    p.start()
    i = 0
    stop = False
    while not stop:
        try:
            qcntr.put('go', block=True)
            try:
                qi = qcam.get(block=True, timeout=1)
            except Empty:
                pass
            else:
                try:
                    #
                    print("Main: received", qi.shape, i)
                except:
                    print('Main: got array with error', i)

        except KeyboardInterrupt:
            qcntr.put('stop', block=True)
            print("Main: KeyboardInterrupt")

            stop = True
        else:
            i += 1
            if i == 5:
                qcntr.put('stop', block=True)
                stop = True

            if i == 7:
                break
            pass
    try:
        # while not qcam.empty():
        qi = qcam.get(block=True, timeout=1)

        pass
    except Empty:
        pass
    p.join()
    time.sleep(2)
    print('Main: End of program')
    qcam.close()
    qcntr.close()
    qcam.join_thread()
    qcntr.join_thread()
    print('Main: join')
    print('Main: bye')

