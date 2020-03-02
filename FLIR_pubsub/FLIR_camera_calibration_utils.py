# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/94_camera_calibration_utils.ipynb (unless otherwise specified).

__all__ = ['Capture']

# Cell

import imutils
import cv2
from imutils.video import FPS
import zmq
import numpy as np
import time

class Capture:
    def __init__(self, name='FrontLeft', url='localhost'):
        self.PORT = 5555
        self.width = 1000
        self.height = 750
        self.name = name
        self.url = url
        self.socket_sub = None
        self.context = None


    def _recv_array(self, socket:zmq.Context.socket, flags=0, copy=True, track=False):
        """recv a numpy array"""
        md = socket.recv_json(flags=flags)
        msg = socket.recv(flags=flags, copy=copy, track=track)
        buf = memoryview(msg)
        A = np.frombuffer(buf, dtype=md['dtype'])
        # return (A.reshape(md['shape']), md)
        return (A, md)

    def _recv_frame(self, socket):
        """ Receive and process an image from camera"""
        try:
            #  Get the reply.
            topic = socket.recv_string()
            rec_frame, md = self._recv_array(socket)
            rec_frame = cv2.imdecode(rec_frame, cv2.IMREAD_GRAYSCALE)
            rec_frame = cv2.cvtColor(rec_frame, cv2.COLOR_BAYER_BG2BGR)
            rec_frame = rec_frame.reshape((3000, 4000, 3))
            # rec_frame = imutils.resize(rec_frame, width=width, height=height)
            # cv2.putText(rec_frame, f'Received frame {md}',
            #             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        except Exception as e:
            rec_frame = np.ones((self.width, self.height))
            topic = 'cam1'
            md = None
            # cv2.putText(rec_frame, f'error:  {e}',
            #             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            print (f"error: message timeout {e}")
            time.sleep(1)
        return topic, rec_frame, md

    def _poll_server(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(f"tcp://{self.url}:{self.PORT + 1}")
        socket.setsockopt(zmq.LINGER, 0)
        poller = zmq.Poller()
        poller.register(socket, flags=zmq.POLLIN)

        socket.send_string(f"keep_alive {self.name}")
        result = dict(poller.poll(1000))
        poller.unregister(socket)

    def open_client(self, name='FrontLeft', url='localhost'):
        """ Received frames from a single camera. Must have the server running"""

        self.context = zmq.Context()

        # subscribe socket
        print( "Connecting to server...")
        self.socket_sub = self.context.socket(zmq.SUB)
        self.socket_sub.connect( f"tcp://{url}:{self.PORT}")
        self.socket_sub.setsockopt_string(zmq.SUBSCRIBE, name)


    def close_client(self):
        self.socket_sub.close()

        self.context.term()
        cv2.destroyAllWindows()

        print('Finished')

#     def get_image(self):
#         self._poll_server()

#         try:
#             topic, rec_frame, md = self._recv_frame(self.socket_sub)
# #             rec_frame = imutils.resize(rec_frame, width=2400, height=1800)

#         except KeyboardInterrupt:
#             pass

#         return topic, rec_frame, md

    def fetch_image(self):
        self.open_client()
        self._poll_server()
        topic, rec_frame, md = self._recv_frame(self.socket_sub)
        self.close_client()
        return topic, rec_frame, md