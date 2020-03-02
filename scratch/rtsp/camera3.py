__author__ = 'JN'

import imutils, time
from scratch.rtsp.cv_videostream import CV_VideoStream

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button

import cv2



class KivyApp(App):
	def __init__(self, **kwargs):
		super(KivyApp, self).__init__()
		# self.capture = cv2.VideoCapture("rtsp://192.168.183.242:554")
		print("[INFO] sampling THREADED frames from webcam...")
		self.vs = CV_VideoStream(src="rtsp://192.168.183.242:554", verbose=True).start()

	def build(self):
		self.img1=Image(source='../images/aero1.jpg')
		layout = BoxLayout()
		layout.add_widget(self.img1)
		self.allow_stretch = True

		# button = Button(size_hint=(None, None), text='plop',
		# 				on_press=self.animate)
		#
		# layout.add_widget(button)


		Clock.schedule_interval(self.update_cv, 1.0/30.0)

		# Clock.schedule_interval(self.update_kivy, 1.0/30.0)
		return layout

	def animate(self, instance):
		# create an animation object. This object could be stored
		# and reused each call or reused across different widgets.
		# += is a sequential step, while &= is in parallel
		animation = Animation(pos=(100, 100), t='out_bounce')
		animation += Animation(pos=(200, 100), t='out_bounce')
		animation &= Animation(size=(500, 500))
		animation += Animation(size=(100, 50))

		# apply the animation on the button, passed in the "instance" argument
		# Notice that default 'click' animation (changing the button
		# color while the mouse is down) is unchanged.
		animation.start(instance)

	def update_kivy(self, dt):
		'''display image from cam in kivy window'''
		frame = self.vs.read()

		if hasattr(frame, 'size') and frame.size > 100000:
			# convert it to texture
			buf = cv2.flip(frame, 0)
			buf = buf.tostring()
			texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
			texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
			# display image from the texture
			self.img1.texture = texture1

	def update_cv(self, dt):
		'''display image from cam in opencv window'''
		frame = self.vs.read()
		# frame = imutils.resize(frame, width=400)
		if hasattr(frame, 'size'):
			if frame.size > 100000:
				cv2.imshow("CV frame", frame)
				cv2.waitKey(1)
		else:
			pass

	def on_stop(self):
		self.vs.stop()
		print(f"[INFO] App {self.name} is now stopped:")
		cv2.destroyAllWindows()

if __name__ == '__main__':

	app = KivyApp()
	app.run()
	print('Bye')


