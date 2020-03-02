import time
import cv2
import numpy as np

from scratch.flask_VS_like.base_camera import *


class CameraTest(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [cv2.imread('../images/' + f + '.jpg') for f in ['1', '2', '3']]
    a = 'do nothing'


    @staticmethod
    def frames():
        shape = (1000, 1500, 3)
        i = 0
        while True:
            time.sleep(0.1)
            img = np.zeros(shape, dtype=np.uint8)
            cv2.putText(img, f"frame: {i}",
                        (shape[1] // 4, shape[0] // 2), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 5)
            i += 1
            # if not close
            # yield Camera.imgs[int(time.time()) % 3]
            yield img


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (frame)


if __name__ == '__main__':



    frames1 = gen(CameraTest())
    cv2.namedWindow('VIDEO1')
    frames2 = gen(CameraTest())
    cv2.namedWindow('VIDEO2')
    count = 0
    while True:
        count += 1
        if count < 10:

            frame = next(frames1, None)
            if frame is not None:
                cv2.imshow('VIDEO1', frame)

            frame = next(frames2, None)
            if frame is not None:
                cv2.imshow('VIDEO2', frame)
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