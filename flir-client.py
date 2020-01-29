import imutils
import cv2
from imutils.video import FPS
import zmq
import numpy as np
import time
from datetime import datetime
import argparse

PORT = 5555
width = 1000
height = 750

def recv_array(socket:zmq.Context.socket, flags=0, copy=True, track=False):
    """recv a numpy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = memoryview(msg)
    A = np.frombuffer(buf, dtype=md['dtype'])
    # return (A.reshape(md['shape']), md)
    return (A, md)

def recv_frame(socket):
    try:
        #  Get the reply.
        topic = socket.recv_string()
        rec_frame, md1 = recv_array(socket)
        rec_frame = cv2.imdecode(rec_frame, cv2.IMREAD_GRAYSCALE)
        rec_frame = cv2.cvtColor(rec_frame, cv2.COLOR_BAYER_BG2BGR)
        rec_frame = rec_frame.reshape((3000, 4000, 3))
        # rec_frame = imutils.resize(rec_frame, width=width, height=height)
        cv2.putText(rec_frame, f'Received frame {md1}',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        fps.update()

    except Exception as e:
        rec_frame = np.ones((width,height))
        topic = 'cam1'
        cv2.putText(rec_frame, f'error:  {e}',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        print (f"error: message timeout {i},  {e}")
        time.sleep(1)
    return topic, rec_frame


def poll_server(name):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{url}:{PORT + 1}")
    socket.setsockopt(zmq.LINGER, 0)
    poller = zmq.Poller()
    poller.register(socket, flags=zmq.POLLIN)

    socket.send_string(f"keep_alive {name}")
    result = dict(poller.poll(1000))
    poller.unregister(socket)




# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--cam", default=0,
	help="camera number")
ap.add_argument("--url", default='localhost',
	help="base URL, ie '10.42.0.116' ")
ap.add_argument("--name", default='FrontLeft',
	help="camera name, ie 'FrontLeft' ")
args = vars(ap.parse_args())
camnum = int(args["cam"])
name = args["name"]
url = args["url"]
port = str(PORT + camnum)

context = zmq.Context()

# subscribe socket
print( "Connecting to server...")
socket_sub = context.socket(zmq.SUB)
socket_sub.connect( f"tcp://{url}:{PORT}")
socket_sub.setsockopt_string(zmq.SUBSCRIBE, name)

fps = FPS().start()

i = 0
while True:
    poll_server(name)
    try:
        topic, rec_frame = recv_frame(socket_sub)
        rec_frame = imutils.resize(rec_frame, width=2400, height=1800)
        # except:
        #     topic = ""
        #     rec_frame = np.zeros((100, 100, 3))
        cv2.imshow(topic, rec_frame)
        k = cv2.waitKey(10)
        if k == 27 or k == 3:
           break  # esc to quit
    except KeyboardInterrupt:
        break

fps.stop()

socket_sub.close()

context.term()
cv2.destroyAllWindows()

print('Finished')
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
