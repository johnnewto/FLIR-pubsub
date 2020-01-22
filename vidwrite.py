import numpy as np

import skvideo.datasets
import skvideo.io

filename = skvideo.datasets.bigbuckbunny()

vid_in = skvideo.io.FFmpegReader(filename)
data = skvideo.io.ffprobe(filename)['video']
rate = data['@r_frame_rate']
T = np.int(data['@nb_frames'])

vid_out = skvideo.io.FFmpegWriter("corrupted_video.mp4", inputdict={
      '-r': rate,
    },
    outputdict={
      '-vcodec': 'libx264',
      '-pix_fmt': 'yuv420p',
})
for idx, frame in enumerate(vid_in.nextFrame()):
  print("Writing frame %d/%d" % (idx, T))
  if (idx >= (T/2)) & (idx <= (T/2 + 10)):
    frame = np.random.normal(128, 128, size=frame.shape).astype(np.uint8)
  vid_out.writeFrame(frame)
vid_out.close()


# import skvideo.io
# import numpy as np
#
# outputdata = np.random.random(size=(5, 480, 680, 3)) * 255
# outputdata = outputdata.astype(np.uint8)
#
# writer = skvideo.io.FFmpegWriter("outputvideo.mp4")
# for i in range(5):
#         writer.writeFrame(outputdata[i, :, :, :])
# writer.close()