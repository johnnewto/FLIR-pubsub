from  boxfish_flir_cam import FLIR_client_utils
if __name__== "__main__":

    FLIR_client_utils.stereo_client(name1='FrontLeft', name2='FrontRight', url='localhost', video='video.avi', vcodec='mjpeg')