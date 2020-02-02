# FLIR camera server and client

## Server Installation
The server `FLIR-server.py`  requires python > 3.6.  
 Install the following prerequisites
``` 
sudo apt install python3-opencv
pip install opencv-contrib-python
pip install imutils
pip install PyYAML
pip install zmq
```
The server `FLIR-server.py` is typically run as a service. It polls all available cameras and configures them against the yaml file.  
To install the service  
`sudo cp flir-server.service /etc/systemd/system/flir-server.service`  

The service can be started and stopped with the following bash commands  
`sudo systemctl start flir-server.service  `  
`sudo systemctl stop flir-server.service  `  

To ensure it runs on boot enable the service  
`sudo systemctl enable flir-server.service` 

The server polls all installed cameras and trys to match them with corresponding yaml files
### Camera yaml files
Each camera will have a yaml file with the serial number as its file name
The first 3 entries determine serial number and camera name identifiers, and the link encoding of jpeg or not
The init section contains the FLIR camera initialisation settings  
__19312753.yaml__  
```yaml
serial: 19312753 
name: 'FrontRight'  
encoding: '.jpg'  # either null or '.jpg'
init:
    - AcquisitionFrameRateEnable:
        value: True
    - AcquisitionFrameRate:
        value: 2
#    - BinningHorizontal:
#        value: 1
#    - BinningVertical:
#        value: 1
#    - ExposureMode:
#        value: PySpin.ExposureMode_Timed
     - ExposureAuto:
         value: PySpin.ExposureAuto_Continuous
#     - ExposureTime:
#         value: 60000
     - GainSelector:
         value: PySpin.GainSelector_All
     - GainAuto:
         value: PySpin.GainAuto_Off
     - Gain:
         value: 6
     - BlackLevelSelector:
         value: PySpin.BlackLevelSelector_All
     - BlackLevel:
         value: 0
     - GammaEnable:
         value: True
 ```

if you wish to trigger the camera with a hardware digital signal then the following should be used  
```yaml
init:
    - TriggerMode:  
        value: PySpin.TriggerMode_On  
    - TriggerSource:
        value: PySpin.TriggerSource_Line3
    - TriggerOverlap:
        value: PySpin.TriggerOverlap_ReadOut
    - TriggerMode:
        value: PySpin.TriggerMode_On
    - AcquisitionFrameRateEnable:
        value: False   
```

```