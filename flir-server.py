
import multi_pyspin, time
import zmq
import threading
import cv2
import imutils


PORT = 5555
MODE = 'test'
MODE = 'cam'
STOP = False
SHOW_CV_WINDOW = False

def send_array(socket, A, flags=0, framedata=None, copy=True, track=False):
    """send a numpy array with metadata"""
    md = dict(
        dtype=str(A.dtype),
        shape=A.shape,
        framedata=framedata,
    )
    socket.send_json(md, flags | zmq.SNDMORE)
    return socket.send(A, flags, copy=copy, track=track)

def publisher(cam_num, yaml_dict):
    # Prepare publisher
    serial = str(yaml_dict['serial'])
    encoding = yaml_dict['encoding']
    name = yaml_dict['name']
    # port = str(PORT + cam_num)
    # context = zmq.Context()
    # socket = context.socket(zmq.PUB)
    # socket.setsockopt(zmq.SNDHWM, 20)
    # socket.bind("tcp://*:%s" % PORT)
    # serial = SERIALS[camnum]
    multi_pyspin.start_acquisition(serial)
    topic = f'Cam {name}'
    print(f'Starting : {topic}')
    i = 0
    # with FFMPEG_VideoWriter('out.mp4', (1000, 1000), 5.0, codec='libx264') as video:
    while True:
        i += 1
        # serial = SERIALS(camnum)
        cam = multi_pyspin._get_cam(serial)
        image = cam.GetNextImage()
        img = image.GetNDArray()
        shape = img.shape
        if encoding is not None:
            img = cv2.imencode(encoding, img)[1]

        md = {'frameid': i, 'encoding': encoding, 'size': img.size, 'shape': shape}
        # print(f"{topic}, Frame: {md['frameid']}, Framesize {img.shape}") #, end='\r')
        print(f'\033[{cam_num+1};0f', end='')
        print(f"{topic}, {md}")  # , end='\r')

        socket.send_string(topic, zmq.SNDMORE)
        send_array(socket, img, framedata=md)

        if SHOW_CV_WINDOW:
            if encoding is not None:
                _frame = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
            _frame = cv2.cvtColor(_frame, cv2.COLOR_BAYER_BG2BGR)
            _frame = imutils.resize(_frame, width=1000, height=750)
            cv2.imshow(topic, _frame)
            cv2.waitKey(10)

        if STOP:
            break

    multi_pyspin.end_acquisition(serial)
    multi_pyspin.deinit(serial)


# This main

print("\033[2J", end='')
# port = str(PORT + cam_num)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.SNDHWM, 20)
socket.bind("tcp://*:%s" % PORT)

# # Install cameras
pub_threads = []
yaml_dicts = []
for i, serial in enumerate(list(multi_pyspin._SERIAL_DICT)):
    cam = multi_pyspin._get_and_validate_init_cam(serial)
    yaml_dict = multi_pyspin.setup(f'{cam.DeviceSerialNumber()}.yaml')
    yaml_dicts.append(yaml_dict)
    del cam   # this is so that camera will release smoothly art exit

for i, yaml_dict in enumerate(list(yaml_dicts)):
    pt = threading.Thread(target=publisher, args=(i, yaml_dict,))
    pt.start()
    pub_threads.append(pt)

# time.sleep(1)
# print("\033[2J", end='')

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
STOP = True
for pt in pub_threads:
    pt.join()

cv2.destroyAllWindows()

