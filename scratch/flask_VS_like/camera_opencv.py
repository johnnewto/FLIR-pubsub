import cv2
import time
from scratch.flask_VS_like.base_camera import *


class CameraRTSP(BaseCamera):
    video_source = 0

    def __init__(self, src):
        self.set_video_source(src)
        # if os.environ.get('OPENCV_CAMERA_SOURCE'):
        #     Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(CameraRTSP, self).__init__()

    @staticmethod
    def set_video_source(source):
        CameraRTSP.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(CameraRTSP.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            grabbed, img = camera.read()

            # encode as a jpeg image and return it
            # yield cv2.imencode('.jpg', img)[1].tobytes()
            yield img


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (frame)


if __name__ == '__main__':

    frames1 = gen(CameraRTSP("rtsp://192.168.183.242:554"))
    cv2.namedWindow('VIDEO1')
    # frames2 = gen(CameraRTSP("rtsp://192.168.183.242:554"))
    # cv2.namedWindow('VIDEO2')

    count = 0
    while True:
        count += 1
        if count < 10:

            frame = next(frames1, None)
            if frame is not None:
                cv2.imshow('VIDEO1', frame)

            # frame = next(frames2, None)
            # if frame is not None:
            #     cv2.imshow('VIDEO2', frame)
        else:
            time.sleep(0.1)

        k = cv2.waitKey(10)
        txt = None
        if k == 27 or k == 3:
            break  # esc to quit
        elif k == ord('s'):
            count = 0

        # print(count)

    cv2.destroyAllWindows()
