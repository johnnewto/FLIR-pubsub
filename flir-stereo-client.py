import imutils
import cv2
from imutils.video import FPS
import zmq
import numpy as np
import time
from datetime import datetime
import argparse
import skvideo.io


PORT = 5555
width = 2000
height = 1500


def recv_array(socket:zmq.Context.socket, flags=0, copy=True, track=False):
    """recv a numpy array"""
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)
    buf = memoryview(msg)
    A = np.frombuffer(buf, dtype=md['dtype'])
    # return (A.reshape(md['shape']), md)
    return (A, md)

def recv_frame(socket):
    # try:
    #  Get the reply.
    topic = socket.recv_string()
    rec_frame, md = recv_array(socket)
    rec_frame = cv2.imdecode(rec_frame, cv2.IMREAD_GRAYSCALE)
    rec_frame = cv2.cvtColor(rec_frame, cv2.COLOR_BAYER_BG2BGR)
    rec_frame = rec_frame.reshape((3000, 4000, 3))
    # rec_frame = imutils.resize(rec_frame, width=width, height=height)

    fps.update()
    return topic, rec_frame, md
    # except Exception as e:
    #     rec_frame = np.ones((width,height))
    #     topic = 'cam1'
    #     cv2.putText(rec_frame, f'error:  {e}',
    #                 (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    #     print (f"error: message {i},  {e}")
    #     time.sleep(1)
    # return topic, rec_frame, md

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--video", default='video.avi',
	help="video file name")
ap.add_argument("--vcodec", default='libx264',
	help="video codec, ie libx264 ")

ap.add_argument("--url", default='localhost',
	help="base URL, ie '10.42.0.17' ")
ap.add_argument("--name1", default='FrontLeft',
	help="camera name 1, ie 'FrontLeft' ")
ap.add_argument("--name2", default='FrontRight',
	help="camera name 2, ie 'FrontRight' ")

args = vars(ap.parse_args())
outputfile = args["video"]
vcodec = args["vcodec"]
name1 = args["name1"]
name2 = args["name2"]
url = args["url"]

context = zmq.Context()
print( "Connecting to server...")
socket1 = context.socket(zmq.SUB)
socket1.connect( f"tcp://{url}:{PORT}"  )
socket1.setsockopt_string(zmq.SUBSCRIBE, f'Cam {name1}')
socket2 = context.socket(zmq.SUB)
socket2.connect( f"tcp://{url}:{PORT}"  )
socket2.setsockopt_string(zmq.SUBSCRIBE, f'Cam {name2}')

fps = FPS().start()

i = 0

writer = skvideo.io.FFmpegWriter(outputfile, outputdict={'-vcodec': 'mjpeg'})
# writer = skvideo.io.FFmpegWriter(outputfile, outputdict={'-vcodec': vcodec, '-b': '30000000', '-r': "2"})

SHOW_CV_WINDOW = True

stop = False
while stop == False:
    i += 1
    try:
        try:
            topic1, rec_frame1, md1 = recv_frame(socket1)
            topic2, rec_frame2, md2 = recv_frame(socket2)
        except Exception as e:
            print(f"Video error:  {e}")
        else:
            cv2.putText(rec_frame1, f"{md1['framedata']['frameid']}",
                        (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)
            cv2.putText(rec_frame2, f"{md2['framedata']['frameid']}",
                        (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)

            s_frame = np.concatenate((rec_frame1, rec_frame2), axis=1)
            writer.writeFrame(s_frame)
            print(f"Writing Frame pair {md1['framedata']['frameid']}, {md2['framedata']['frameid']}")

            if SHOW_CV_WINDOW:
                rec_frame1 = imutils.resize(rec_frame1, width=width, height=height)
                rec_frame2 = imutils.resize(rec_frame2, width=width, height=height)
                # cv2.putText(rec_frame1, f"{md2['framedata']['frameid']}",
                #             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                # cv2.putText(rec_frame2, f"{md2['framedata']['frameid']}",
                #             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                cv2.imshow(topic1, rec_frame1)
                cv2.imshow(topic2, rec_frame2)
                k = cv2.waitKey(10)
                if k == 27 or k == 3:
                   stop = True
    except KeyboardInterrupt:
        stop = True
        print("Stopping")

fps.stop()
writer.close()
socket1.close()
socket2.close()
context.term()
cv2.destroyAllWindows()

print('Finished')
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()/2))


import skvideo.io

# outputfile = "/tmp/video.mp4"
# writer = skvideo.io.FFmpegWriter(outputfile, outputdict={'-vcodec': 'libx264'})
# for frame in frames:
#     writer.writeFrame(frame)
