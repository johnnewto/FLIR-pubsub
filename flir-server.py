
import multi_pyspin, time
import zmq
import threading
import cv2
import imutils


PORT = 5555

SHOW_CV_WINDOW = False



class CameraThread:
    def __init__(self, socket_pub, i, yaml_dict):
        self.stopped = True
        self.socket_pub = socket_pub
        self.i = i
        self.yaml_dict = yaml_dict
        self.name = yaml_dict['name']
        self.serial = str(yaml_dict['serial'])
        self.encoding = yaml_dict['encoding']
        self.last_access = time.time()

    def send_array(self, A, flags=0, framedata=None, copy=True, track=False):
        """send a numpy array with metadata"""
        md = dict(
            dtype=str(A.dtype),
            shape=A.shape,
            framedata=framedata,
        )
        self.socket_pub.send_string(self.name, zmq.SNDMORE)
        self.socket_pub.send_json(md, flags | zmq.SNDMORE)
        return self.socket_pub.send(A, flags, copy=copy, track=track)

    def start(self):
        """
        Initialise and set camera thread and begin acquisisition
        """
        self.thread = threading.Thread(target=self.update, args=(self.socket_pub, self.i, self.yaml_dict, ))
        self.thread.daemon = False
        self.stopped = False
        self.thread.start()
        return self

    def stop(self):
        """indicate that the thread should be stopped"""
        self.stopped = True
        # wait until stream resources are released (producer thread might be still grabbing frame)
        self.thread.join()

    def update(self, socket, cam_num, yaml_dict):
        # Prepare publisher

        multi_pyspin.init(self.serial)
        multi_pyspin.start_acquisition(self.serial)
        print(f'Starting : {self.name}')
        i = 0
        while True:
            i += 1

            # cam = multi_pyspin._get_cam(serial)
            # image = cam.GetNextImage()
            image, image_dict = multi_pyspin.get_image(self.serial)
            img = image.GetNDArray()
            shape = img.shape
            if self.encoding is not None:
                img = cv2.imencode(self.encoding, img)[1]

            md = {'frameid': i, 'encoding': self.encoding, 'size': img.size, 'shape': shape}
            # print(f"{topic}, Frame: {md['frameid']}, Framesize {img.shape}") #, end='\r')
            # print(f'\033[{cam_num+1};0f', end='')
            # print(f"{self.name}, {md}")  # , end='\r')

            self.send_array( img, framedata=md)

            if SHOW_CV_WINDOW:
                if self.encoding is not None:
                    _frame = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
                else:
                    _frame = img

                _frame = cv2.cvtColor(_frame, cv2.COLOR_BAYER_BG2BGR)
                _frame = imutils.resize(_frame, width=1000, height=750)
                cv2.imshow(self.name, _frame)
                cv2.waitKey(10)

            if time.time() - self.last_access > 10:
                print(f'Stopping {self.name} due to inactivity.')
                self.stopped = True

            if self.stopped:
                break


        multi_pyspin.end_acquisition(self.serial)
        multi_pyspin.deinit(self.serial)
        # del cam


# This main
def main():
    global STOP

    print("\033[2J", end='')

    context = zmq.Context()
    socket_pub = context.socket(zmq.PUB)
    socket_pub.setsockopt(zmq.SNDHWM, 20)
    socket_pub.bind(f"tcp://*:{PORT}")

    socket_rep = context.socket(zmq.REP)
    socket_rep.RCVTIMEO = 1000
    socket_rep.bind(f"tcp://*:{PORT+1}")

    # # Install cameras
    pub_threads = []
    yaml_dicts = []
    for i, serial in enumerate(list(multi_pyspin._SERIAL_DICT)):
        yaml_dict = multi_pyspin.setup(f'{serial}.yaml')
        yaml_dicts.append(yaml_dict)

    for i, yaml_dict in enumerate(list(yaml_dicts)):
        ct = CameraThread(socket_pub, i, yaml_dict)
        ct.start()
        pub_threads.append(ct)
    count = 0
    while True:
        try:
            message = socket_rep.recv().decode("utf-8")
            socket_rep.send_string("OK")
            name = message.split()[1]
            pt = [pt for pt in pub_threads if pt.name == name]
            assert len(pt) == 1, "Expect one item only"
            pt[0].last_access = time.time()
            if pt[0].stopped:
                pt[0].start()

        except zmq.error.Again:
            pass

        except KeyboardInterrupt:
            break

    for ct in pub_threads:
        print(f"stopping {ct.name}")
        ct.stop()

    cv2.destroyAllWindows()
    socket_pub.close()
    socket_rep.close()
    context.term()
if __name__== "__main__":
    main()
