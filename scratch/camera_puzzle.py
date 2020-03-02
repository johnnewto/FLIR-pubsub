'''
Shuffled Camera Feed Puzzle
===========================

This demonstrates using Scatter widgets with a live camera.
You should see a shuffled grid of rectangles that make up the
camera feed. You can drag the squares around to see the
unscrambled camera feed or double click to scramble the grid
again.
'''

import cv2
from scratch.rtsp.cv_videostream import CV_VideoStream

from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.properties import NumericProperty
from random import randint, random
from functools import partial
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout

from scratch.rtsp.cv_videostream import CV_VideoStream
import cv2
import numpy as np

class Puzzle(Image):

    blocksize = NumericProperty(250)

    def on_texture_size(self, instance, value):
        self.build()

    def on_blocksize(self, instance, value):
        self.build()

    def build(self):

        self.clear_widgets()
        self.allow_stretch = True
        texture = self.texture

        if not texture:
            return
        bs = self.blocksize
        tw, th = self.texture_size

        for x in range(int(tw / bs)):
            for y in range(int(th / bs)):
                bx = x * bs
                by = y * bs
                subtexture = texture.get_region(bx, by, bs, bs)
                # node = PuzzleNode(texture=subtexture,
                #                  size=(bs, bs), pos=(bx, by))
                node = Scatter(pos=(bx, by), size=(bs, bs))
                with node.canvas:
                    Color(1, 1, 1)
                    Rectangle(size=node.size, texture=subtexture)
                self.add_widget(node)


        self.shuffle()
        # self.update_nodes(self.texture)




    def update_nodes(self, dt):
        # texture = self.texture
        tw, th = self.texture_size
        # buf = np.array([int(random.random() * x * 255 / size) for x in range(size)])
        buf = np.ones(1280*720*3, dtype=np.int8)
        texture1 = Texture.create(size=(1280, 720), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

        # buf = np.ones([int(random.random() * x * 255 / size) for x in range(size)])
        print('update', max(buf), min(buf), np.mean(buf))
        # then blit the buffer
        # texture.blit_buffer(buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        bs = self.blocksize
        count = int(tw / bs) * int(th / bs)
        childindex = 0
        for x in range(int(tw / bs)):
            for y in range(int(th / bs)):
                bx = x * bs
                by = y * bs
                subtexture = texture1.get_region(bx, by, bs, bs)
                child = self.children[childindex]
                child.texture = subtexture
                childindex += 1

        # self.texture = texture1



    def shuffle(self):
        texture = self.texture
        bs = self.blocksize
        tw, th = self.texture_size
        count = int(tw / bs) * int(th / bs)
        indices = list(range(count))
        childindex = 0
        while indices:
            index = indices.pop(randint(0, len(indices) - 1))
            x = bs * (index % int(tw / bs))
            y = bs * int(index / int(tw / bs))
            child = self.children[childindex]
            a = Animation(d=random() / 4.) + Animation(pos=(x, y),
                                                       t='out_quad', d=.4)
            a.start(child)
            childindex += 1

    def on_touch_down(self, touch):
        # self.update_nodes()
        print("touchdown")
        # return True
        super(Puzzle, self).on_touch_down(touch)

    # def on_touch_down(self, touch):
    #     if touch.is_double_tap:
    #         self.shuffle()
    #         return True
    #     super(Puzzle, self).on_touch_down(touch)


class PuzzleApp(App):
    def build(self):
        self.vs = CV_VideoStream(src="rtsp://192.168.183.242:554", verbose=True).start()
        root = Widget()
        self.puzzle = Puzzle(source='images/aero1.jpg')

        self.texturebuffer = Texture.create(size=(1280, 720), colorfmt='bgr')

        slider = Slider(min=200, max=400, step=10, size=(800, 50),size_hint=(1,0.1) )
        slider.bind(value=partial(self.on_value, self.puzzle))

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.puzzle)
        layout.add_widget(slider)
        # layout.add_widget(button)

        Clock.schedule_interval(self.update_kivy, 1.0 / 30.0)
        # Clock.schedule_interval(self.puzzle.update_nodes, 1.0 / 5.0)

        return layout

    def on_value(self, puzzle, instance, value):
        value = int((value + 5) / 10) * 10
        puzzle.blocksize = value
        instance.value = value

    def update_kivy(self, dt):
        '''display image from cam in kivy window'''
        frame = self.vs.read()

        if hasattr(frame, 'size') and frame.size > 100000:
            # convert it to texture
            buf = cv2.flip(frame, 0)
            buf = buf.tostring()
            # self.texturebuffer.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # # display image from the texture
            # self.puzzle.texture = self.texturebuffer

            texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.puzzle.texture = texture1
            # self.puzzle.update_nodes(texture1)

if __name__ == '__main__':
    PuzzleApp().run()
