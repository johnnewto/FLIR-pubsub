# FLIR camera server and client

## Server Installation

### Camera yaml files
Each camera will have a yaml file with the serial number as its file name
The first 3 entries determine serial number and camera name identifiers, and the link encoding of jpeg or not
The init section contains the FLIR camera initialisation settings
`19312753.yaml`  
    `---  
    
    serial: 19312753 
    name: 'FrontRight'  
    encoding: '.jpg'  # either null or '.jpg'
    init:
        - LineSelector:
            value: PySpin.LineSelector_Line2
        - LineMode:
            value: PySpin.LineMode_Output
        - V3_3Enable:
            value: False
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
             value: True`

The server FLIR-server.py is typically run as a service. It polls all available cameras and configures them against the yaml file.