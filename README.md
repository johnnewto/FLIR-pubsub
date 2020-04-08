# Boxfish FLIR Cameras Library
> This project allows the remote running of camera over an ethernet connection 


### Description
It uses the pyZMQ to allow the remote running of camera over an ethernet connection using the 
[Publish/Subscribe](https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html) 
messaging pattern. This has proved to be more efficient in bandwidth over the `Request/Reply pattern`.  
There are server and client examples including an example of how stereo camera pairs can be configured and synchronised recordings made.

### Documentation
This library and documentation had been generated with __fastai nbdev__  
nbdev is a library that allows you to fully develop a library in Jupyter Notebooks, putting all your code, 
tests and documentation in one place.  
https://nbdev.fast.ai/

## Installation

Clone or download the project from https://github.com/johnnewto/FLIR_pubsub  

If running a server then you will need to follow details in 
[UPBoard_setup](https://johnnewto.github.io/FLIR_pubsub/UPBoard_setup/)  and 
[FLIR_server_utils](https://johnnewto.github.io/FLIR_pubsub/FLIR_server_utils/)  

If running a client then you only need to copy or symlink the `FLIR_pubsub/FLIR_pubsub` directory as a local directory
Examples of clients are shown in `FLIR_pubsub/run`  
More details are described in 
[FLIR_client_utils](https://johnnewto.github.io/FLIR_pubsub/FLIR_client_utils/)

Normally it is best to setup a virtual environment, call it flir, and install the requirements with   
`pip install -r requirements.txt`

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
