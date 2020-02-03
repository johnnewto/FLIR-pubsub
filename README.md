# Boxfish-FLIR-Cameras
> This project allows the remote running of camera over an ethernet connection. It uses the pyZMQ 


## Install

Under Ubuntu you can symlink or copy the  `boxfish_flir_cam` directory to the project.
Then create a server and client as described in the 

## How to use

### Example of a Multiple Camera Server

```
from  FLIR_pubsub import FLIR_server_utils
FLIR_server_utils.register()  

from pathlib import Path
if __name__== "__main__":

    yaml_dir= Path.cwd()/'common'
    FLIR_server_utils.server(yaml_dir)

```

For more details see [FLIR_server_utils](https://johnnewto.github.io/FLIR_pubsub/FLIR_server_utils/)

### Example of a Camera Client

```
from  FLIR_pubsub import FLIR_client_utils
if __name__== "__main__":

    FLIR_client_utils.stereo_client(name1='FrontLeft', name2='FrontRight', url='localhost', video='video.avi', vcodec='mjpeg')
```

For more details see [FLIR_client_utils](https://johnnewto.github.io/FLIR_pubsub/FLIR_client_utils/)

