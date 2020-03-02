
import cv2
vcap = cv2.VideoCapture("rtsp://192.168.183.242:554")

if __name__ == '__main__':
    # time.sleep(2)
    cv2.namedWindow('VIDEO')
    while(1):

        ret, frame = vcap.read()
        if ret:
            cv2.imshow('VIDEO', frame)

        k = cv2.waitKey(1)
        txt = None
        if k == 27 or k == 3:
            break  # esc to quit

    cv2.destroyAllWindows()