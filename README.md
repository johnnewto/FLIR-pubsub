# Boxfish-FLIR-Cameras
> This project allows the reomote running of camera over an ethernet connection. 


### Example of a Multiple Camera Server

```
from  boxfish_flir_cam import FLIR_server_utils
FLIR_server_utils.register()  

from pathlib import Path
if __name__== "__main__":

    yaml_dir= Path.cwd()/'common'
    FLIR_server_utils.server(yaml_dir)
```

## Install

Under Ubuntu you can symlink or copy the  `boxfish_flir_cam` directory to the project.

## How to use

Fill me in please! Don't forget code examples:




