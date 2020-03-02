import sys
from  pathlib import Path
sys.path.append(str(Path.cwd()))
from FLIR_pubsub.FLIR_client_utils import *

import imutils
import cv2
from imutils.video import FPS
import zmq
import numpy as np
import time
import skvideo.io


PORT = 5555
width = 1000
height = 750

def client(name='FrontLeft', url='localhost'):
    """ Received frames from a single camera. Must have the server running"""

    context = zmq.Context()

    # subscribe socket
    print( "Connecting to server...")
    socket_sub = context.socket(zmq.SUB)
    socket_sub.connect( f"tcp://{url}:{PORT}")
    socket_sub.setsockopt_string(zmq.SUBSCRIBE, name)

    fps = FPS().start()

    i = 0
    while True:
        poll_server(url, name)
        try:
            topic, rec_frame, md = recv_frame(socket_sub, fps)
            rec_frame = imutils.resize(rec_frame, width=2400, height=1800)

        except KeyboardInterrupt:
            break
        else:
            # cv2.putText(rec_frame, f"{md['framedata']['frameid']}",
            # (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)
            cv2.putText(rec_frame, f'Received frame {md}',
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.imshow(topic, rec_frame)

            k = cv2.waitKey(10)
            txt = None
            if k == 27 or k == 3:
               break  # esc to quit
            elif k == ord('c'):
                i = 0
                txt = f'Reset name to {topic}-{i}.jpg'
            elif k >= ord('s'):
                txt = f'Saving {topic}-{i}.jpg'
                cv2.imwrite(f'{topic}-{i}.jpg', rec_frame)
                i += 1
            if txt is not None:
                print(txt)
                cv2.putText(rec_frame, txt, (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)
                cv2.imshow(topic, rec_frame)
                cv2.waitKey(1000)
    fps.stop()

    socket_sub.close()

    context.term()
    cv2.destroyAllWindows()

    print('Finished')
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

if __name__=='__main__':

    name = 'FrontLeft'
    url = 'localhost'
    print(f'Connecting to {name} on {url}')
    client(name=name, url=url)