# import kivy
# kivy.require('1.10.0')
# import time
# import os
# import sys
# import psutil
# import logging
#
# from kivy.app import App
# from kivy.uix.video import Video
# from kivy.config import Config
# from kivy.core.window import Window
# Config.set('graphics', 'position', 'custom')
# Config.set('graphics', 'left', 0)
# Config.set('graphics', 'top',  500)
# Config.set('graphics', 'resizable', 'False')
# #Config.set('graphics', 'borderless',  1)
# Config.set('graphics', 'width', 1127)
# Config.set('graphics', 'height', 636)
#
# class MyApp(App):
#
#     video = None
#     def build(self):
#         Window.bind(on_keyboard=self.on_keyboard)  # bind our handler
#         self.video = Video(source='Big_Buck_Bunny_1080_10s_2MB.mp4')
#         self.video.state='play'
#         #self.video.options = {'eos': 'loop'}
#         self.video.allow_stretch=True
#         self.video.pos_hint = {'top': 1.0}
#         self.video.bind(eos=self.VideoDone)
#         return self.video
#
#     def VideoDone(self, value, value2):
#         print ("video done", value, value2)
#
#     def on_stop(self):
#         # The Kivy event loop is about to stop, set a stop signal;
#         # otherwise the app window will close, but the Python process will
#         # keep running until all secondary threads exit.
#         print ('stopping and closing kivy')
#         #self.video.state='stop'
#
#
#     def on_keyboard(self, window, key, scancode, codepoint, modifier):
#         print (window, key, scancode, codepoint, modifier)
#         if codepoint == 'p':
#             print ('pausing with p pressed')
#             self.video.state='stop'
#         if codepoint == 's':
#             print ('starting with s pressed')
#             self.video.state='play'
#         if codepoint == 'r':
#             print ('re-starting with r pressed')
#             self.video.seek(0, precise=True)
#



if __name__ == '__main__':
    # print ("hi")
    # MyApp().run()
    #
    import kivy
    from os.path import dirname, join
    from kivy.app import App
    print(kivy.kivy_options["video"])
    from kivy.uix.videoplayer import VideoPlayer

    print(kivy.kivy_options["video"])
    class VideoPlayerApp(App):

        def build(self):
            curdir = dirname(__file__)
            filename = join(curdir, 'Big_Buck_Bunny_1080_10s_2MB.mp4')
            return VideoPlayer(source=filename, state='play')


    if __name__ == '__main__':
        VideoPlayerApp().run()