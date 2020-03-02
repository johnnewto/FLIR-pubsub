# import the necessary packages
from threading import Thread

import cv2, time
from FLIR_pubsub.FLIR_client_utils import *

class Flir_VideoStream:
	""" Maintain live FLIRCam feed without buffering. """

	def __init__(self, src=0, name="FlirVideoStream", verbose = False):
		"""
		    src: the path to an RTSP server. should start with "rtsp://"
		    name: give it a name
		    verbose: print log or not
		"""
		self.name = name # initialize the thread name
		self.fps = 0.0   # measured fps

		self._src = src
		self._verbose = verbose
		self._stream = None
		self._frame = None  # returned images from stream

		# initialize the variable used to indicate if the thread should be stopped
		self._stopped = False
		self._fps = FPS()


	def start(self):
		"""start the thread to read frames from the video stream"""
		if self._verbose:
			print(f"[INFO] connecting to Cam: {self._src}")

		self._stopped = False
		self._thread = Thread(target=self.update, name=self.name, args=())
		self._thread.daemon = True
		self._thread.start()
		self._fps.start()
		return self


	def connect(self):
		if self.isOpened():
			self._stream.release()

		self._stream = cv2.VideoCapture(self._src)
		if self._verbose:
			if self._stream.isOpened():
				print(f"[INFO] connected to Cam: {self._src}")
			else:
				print(f"[INFO] Failed to connect Cam: {self._src}")
				time.sleep(1)

	def update(self):
		"""keep looping infinitely until the thread is stopped"""
		while not self._stopped:

			if self._stream is not None and self._stream.isOpened():
				(self.grabbed, self._frame) = self._stream.read()
				if self.grabbed:
					self._fps.update()
					self.last = datetime.datetime.now()
					time.sleep(0.01)
			else:
				self.connect()
				time.sleep(0.01)
			# 	time.sleep(1)
			if self._fps.elapsed() > 5:
				self._fps.stop()
				self.fps = self._fps.fps
				print(self.fps)
				if self._fps.numFrames == 0:
					self.connect()

				self._fps.start()

		# Thread has stopped
		if self._verbose:
			print(f"[INFO] Connection closed Cam: {self._src}")

	def read(self):
		# return the frame most recently read
		return self._frame

	def stop(self):
		# indicate that the thread should be stopped or closed
		self._close()

	def close(self):
		# indicate that the thread should be stopped or closed
		self._close()

	def _close(self):
		if self.isOpened():
			self._stream.release()
		self._stopped = True
		# wait until stream resources are released (producer thread might be still grabbing frame)
		# Todo this code does not always work, Thread is a daemon so closes anyhow
			# if not self._thread._is_stopped:
			# 	self._thread.join()
			# else:
			# 	pass

	def isOpened(self):
		try:
			return self._stream is not None and self._stream.isOpened()
		except:
			return False

import datetime

class FPS:
	'''Calculate the frames per second'''
	def __init__(self):
		# store the start time, end time, and total number of frames
		# that were examined between the start and end intervals
		self._start = None
		self._end = None
		self.numFrames = 0
		self.fps = 0.0

	def start(self):
		# start the timer
		self._start = datetime.datetime.now()
		self._end = None
		self.numFrames = 0
		return self

	def stop(self):
		# stop the timer
		self._end = datetime.datetime.now()
		self.fps = self.numFrames / self.elapsed()

	def update(self):
		# increment the total number of frames examined during the
		# start and end intervals
		self.numFrames += 1
		# return self._numFrames


	def elapsed(self):
		# return the total number of seconds between the start and
		# end interval
		# if self._end is None:
		self._end = datetime.datetime.now()
		# 	ret = (self._end - self._start).total_seconds()
		# 	self._end = None
		# else:
		# 	ret = (self._end - self._start).total_seconds()

		return (self._end - self._start).total_seconds()


	def poll_fps(self):
		# compute the (approximate) frames per second without stopping
		# if self._end is not None:
		#     return self._numFrames / self.elapsed()
		# else:
		self.numFrames += 1
		self._end = datetime.datetime.now()
		self.fps = self.numFrames / self.elapsed()
		return self.fps

		# self._end = None

	# def fps(self):
	# 	# compute the (approximate) frames per second, must be stopped first
	# 	return self._numFrames / self.elapsed()
