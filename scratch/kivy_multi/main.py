'''
Basic Picture Viewer
====================

This simple image browser demonstrates the scatter widget. You should
see three framed photographs on a background. You can click and drag
the photos around, or multi-touch to drop a red dot to scale and rotate the
photos.

The photos are loaded from the local images directory, while the background
picture is from the data shipped with kivy in kivy/data/images/background.jpg.
The file kivy_multi.kv describes the interface and the file shadow32.png is
the border to make the images look like framed photographs. Finally,
the file android.txt is used to package the application for use with the
Kivy Launcher Android application.

For Android devices, you can copy/paste this directory into
/sdcard/kivy/kivy_multi on your Android device.

The images in the image directory are from the Internet Archive,
`https://archive.org/details/PublicDomainImages`, and are in the public
domain.

'''

import kivy
kivy.require('1.0.6')

from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2, time
import numpy as np
from scratch.kivy_multi.videostream import VideoStream, example_VideoCapture
from FLIR_pubsub.FLIR_videocapture import FlirCapture
from FLIR_pubsub.FLIR_client_utils import *

import multiprocessing
from multiprocessing import Process, freeze_support, Lock, current_process, Value, Array
from scratch.kivy_multi.flir_cam_controller \
    import NP_SharedMemory, fake_camera_process, flir_camera_process, SpinProcess
import timeit

class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)


class PicturesApp(App):

    def build(self):
        self.vs1 = VideoStream(src="rtsp://192.168.183.242:554", verbose=True).start()
        # self.vs2 = VideoStream(src="rtsp://192.168.183.242:554", verbose=True).start()
        # self.vs3 = VideoStream(src="rtsp://192.168.183.242:554", verbose=True).start()
        self.vs4 = VideoStream(src="test", name='test', videocapture=example_VideoCapture, verbose=True).start()
        # self.vcap = cv2.VideoCapture("rtsp://192.168.183.242:554")
        self.i = 0

        name = 'FrontLeft'
        url = 'localhost'

        # # shared memory
        self.sm_flir = NP_SharedMemory((2000, 3000, 3), name='camera_1')
        self.sm_flir.set_local_np_view()
        # sm2 = NP_SharedMemory((2000, 3000, 3), name='camera_2')
        # sm2.set_local_np_view()

        # self.proc_flir = SpinProcess(target=fake_camera_process, sharemem=self.sm_flir)
        self.proc_flir = SpinProcess(target=flir_camera_process, sharemem=self.sm_flir)
        # p2 = Process(target=demo_camera_process, args=(sm2,)).start()

        # the root is created in kivy_multi.kv
        root = self.root
        # self.img1 = Image()
        # root.add_widget(self.img1)


        # get any files into images directory
        curdir = dirname(__file__)
        self.stream_widget_list = []
        for filename in glob(join(curdir, 'images', '*')):
            try:
                # load the image
                picture = Picture(source=filename, rotation=randint(-30, 30))
                # add to the main field
                root.add_widget(picture)
                self.stream_widget_list.append(picture)
            except Exception as e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)

        Clock.schedule_interval(self.update_kivy, 1.0 / 30.0)
        # Clock.schedule_interval(self.wastetime, 1.0 / 100.0)


    def wastetime(self, dt):
        # time.sleep(0.01)
        start = time.monotonic()
        while time.monotonic() - start < 0.1:
            pass

    def on_pause(self):
        return True


    def stream2widget(self, vs, _widgit, bg=None):
        _buf = vs.read()
        # time.sleep(1)

        if _buf is None:
            buf = None
            pass
        elif isinstance(_buf, NP_SharedMemory):
            shape = (_buf._height.value, _buf._width.value, 3)
            buf = _buf.arr[:shape[0]*shape[1]*shape[2]]
            buf.shape = shape

        else:
            buf = _buf

        if isinstance(buf, np.ndarray) and buf.size > 100000:
            # if hasattr(buf, 'size') and buf.size > 100000:
            # convert it to texture
            # all ready flattened
            #
            if 1:
                # start = timeit.timeit()
                if len(buf.shape) == 3:
                    texture1 = Texture.create(size=(buf.shape[1], buf.shape[0]), colorfmt='bgr')
                    buf = cv2.flip(buf, 0).flatten()
                    # buf = buf.flatten()
                elif len(buf.shape) == 1:
                    texture1 = Texture.create(size=(3000, 2000), colorfmt='bgr')
                else:
                    raise RuntimeError(f'Received frame shape should be 1 or 3, got: {buf.shape}')

               # end1 = timeit.timeit()
                texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                # end2 = timeit.timeit()

                # display image from the texture
                if bg is not None:
                   bg.texture = texture1
                _widgit.children[0].texture = texture1
                # end = timeit.timeit()
                # print('Texture: ', end - start)
            else:
                _widgit.children[0].texture.blit_buffer(buf,
                                                        size=(frame.shape[1], frame.shape[0]),
                                                        colorfmt='bgr', bufferfmt='ubyte')


    def update_kivy(self, dt):
        '''display image from cam in kivy window'''
        self.stream2widget(self.vs1, self.stream_widget_list[0])
        self.i += 1
        if self.i % 1 == 0:
            # bodge to slow these down
            # self.stream2widget(self.vs2, self.stream_widget_list[1])
            # self.stream2widget(self.vs3, self.stream_widget_list[2])
            # self.stream2widget(self.vs4, self.stream_widget_list[3])
            self.stream2widget(self.proc_flir, self.stream_widget_list[4])
            pass

    def on_request_close(self, *args):
        self.textpopup(title='Exit', text='Are you sure?')
        return True

    def on_stop(self, *args):
        print('!!!! Running on_stop')
        self.proc_flir.release()
        self.vs1.release()
        self.vs4.release()

        return True

    def textpopup(self, title='', text=''):
        """Open the pop-up with the name.

        :param title: title of the pop-up to open
        :type title: str
        :param text: main text of the pop-up to open
        :type text: str
        :rtype: None
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='OK', size_hint=(1, 0.25))
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
        mybutton.bind(on_release=self.stop)
        popup.open()


import cv2, imutils
import os, sys, logging

if __name__ == '__main__':

    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)


    app = PicturesApp().run()


    print('Main: End of program')


    # time.sleep(2)
    print('Main: join')
    # p1.join()
    # p2.join()
    print('Main: bye')
    cv2.destroyAllWindows()