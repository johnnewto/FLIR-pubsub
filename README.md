# Boxfish-FLIR-Cameras
> This project allows the remote running of camera over an ethernet connection. It uses the pyZMQ 


## Installation

Clone or download the project from https://github.com/johnnewto/FLIR_pubsub  

If running a server then you will need to follow details in 
[UPBoard_setup](https://johnnewto.github.io/FLIR_pubsub/UPBoard_setup/)  and 
[FLIR_server_utils](https://johnnewto.github.io/FLIR_pubsub/FLIR_server_utils/)  

If running a client then you only need to copy or symlink the `FLIR_pubsub/FLIR_pubsub` directory as a local directory
Examples of clients are shown in `FLIR_pubsub/run`  
More details are described in 
[FLIR_client_utils](https://johnnewto.github.io/FLIR_pubsub/FLIR_client_utils/)

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

### Installing Jupyter Notebook

`pip install notebook`
