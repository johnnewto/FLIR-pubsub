# import the necessary packages
from threading import Thread

import cv2, time
from imutils.video import FPS

class VideoStream:
	""" Maintain live RTSP feed without buffering. """
	INACTIVITY_TIMEOUT = 5
	CONNECTION_TIMEOUT = 5
	FPS_TIMEOUT = 5

	def __init__(self, src=0, name="xx_VideoStream", videocapture=cv2.VideoCapture, verbose = False ):
		"""
		    src: the path to an RTSP server. should start with "rtsp://"
		    name: give it a name
		    verbose: print log or not
		"""
		self._src = src
		self.name = name # initialize the thread name
		self.videocapture = videocapture
		self._verbose = verbose

		self.fps = 0.0   # measured fps
		self._stream = None
		self._frame = None  # returned images from stream
		self._thread = None
		# initialize the variable used to indicate if the thread should be stopped
		self._stopped = False
		self._fps = FPS()
		self._lastaccess = time.time()
		self._lastgrab = time.time()
		self._fpstime = time.time()

	def start(self):
		"""connect to videostream and start the thread to read frames from the videostream"""
		# self.connectVC()
		if self._thread is None:
			self._stopped = False
			self._thread = Thread(target=self.update, name=self.name, args=())
			self._thread.daemon = True
			self._thread.start()
			self._fps.start()
			return self

	def connectVC(self):
		if self._stream is not None and self._stream.isOpened():
			self._stream.release()

		# self._stream = cv2.VideoCapture(self._src)
		self._stream = self.videocapture(self._src)   #  FFMPEG will wait for 30 seconds if there is not connection found
		if self._verbose:
			if self._stream.isOpened():
				print(f"[INFO] connected to video capture: {self._src}")
				print(f"[INFO]CV_VideoCapture Backend: {self._stream.getBackendName()}")
			else:
				print(f"[INFO] Failed to connect video capture: {self._src}")
				time.sleep(1)

	def update(self):
		"""Start thread, keep looping infinitely until the thread is stopped"""
		if self._verbose: print(f"[INFO] Starting Thread: {self._src}")
		self._lastaccess = time.time()
		self._lastgrab = time.time()
		self._fpstime = time.time()

		while not self._stopped:

			if self._stream is not None and self._stream.isOpened():
				# grab camera data
				(self.grabbed, self._frame) = self._stream.read()
				if self.grabbed:
					self._fps.update()
					self._lastgrab = time.time()
					time.sleep(0.01)
			else:
				print ('re-connecting')
				self.connectVC()
				time.sleep(0)
			# 	time.sleep(1)


			if time.time() - self._lastgrab > VideoStream.CONNECTION_TIMEOUT:
				print(f"[INFO] Lost connection, retrying to reconnect to video capture: {self._src}")
				self.connectVC()
			if time.time() - self._lastaccess > VideoStream.INACTIVITY_TIMEOUT:
				print(f"[INFO] Stopping Camera thread due to inactivity: {self._src}")
				break
			if time.time() - self._fpstime > VideoStream.FPS_TIMEOUT:
				self._fps.stop()
				self.fps = self._fps.fps
				self._fps.start()

		# Thread has stopped
		self._thread = None
		if self._verbose:
			print(f"[INFO] Thread stopped Cam: {self._src}")



	def read(self):
		# return the frame most recently read
		self.start()
		self._lastaccess = time.time()
		return self._frame

	def stop(self):
		# indicate that the thread should be stopped or closed
		self._close()

	def close(self):
		# indicate that the thread should be stopped or closed
		self._close()

	def release(self):
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

import numpy as np

class example_VideoCapture():
	""" test sudo instance of videocapture for test purposes"""
	def __init__(self, src=None):
		self.src = src
		self._open = True
		self._gen = self.frames()

	def getBackendName(self):
		return "Numpy array"


	def frames(self):
		shape = (1000, 1500, 3)
		img = np.zeros(shape, dtype=np.uint8)
		i = 0
		while True:
			time.sleep(0.1)
			img = img + 1
			cv2.putText(img, f"RTSP frame: {i}",
						(shape[1] // 20, shape[0] // 2), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 5)
			i += 1
			time.sleep(0.1)
			yield (True, img)

	def read(self):
		val = next(self._gen)
		return val

	def release(self):
		self._open = False

	def isOpened(self):
		return self._open

if __name__ == '__main__':
	from scratch.kivy_multi.flir_cam_controller import NP_SharedMemory, VideoCapture
	import scratch.kivy_multi.flir_cam_controller as fcc
	# tst = Test_VideoCapture()
	# while True:
	# 	a,b = tst.read()
	# 	tst.read()

	vs1 = VideoStream(src="rtsp://192.168.183.242:554", videocapture=cv2.VideoCapture, verbose=True).start()
	vs2 = VideoStream(src="test", name='test', videocapture=example_VideoCapture, verbose=True).start()
	vs3 = VideoStream(src="test", name='fake_camera_process', videocapture=fcc.VideoCapture, verbose=True).start()

	vs3 = VideoCapture(src=fake_camera_process, sharemem=sm2)
	go = True
	while (1):
		try:
			if go:
				frame = vs1.read()
				if frame is not None:
					cv2.imshow('VIDEO1', frame)
				else:
					time.sleep(0.1)

				frame = vs2.read()
				if frame is not None:
					cv2.imshow('VIDEO2', frame)
				else:
					time.sleep(0.1)

			k = cv2.waitKey(10)

			if k == 27 or k == 3:
				break  # esc to quit
			elif k == ord('g'):
				print("Main: Start")
				go = True
			elif k == ord('s'):
				print("Main: Stop")
				go = False
		except KeyboardInterrupt:
			print("Main: KeyboardInterrupt")
			break

	cv2.destroyAllWindows()