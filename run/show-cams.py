"""
Show connected cameras
"""

import PySpin

if __name__ == '__main__':
    _SYSTEM = PySpin.System.GetInstance()
    cams = _SYSTEM.GetCameras()
    for cam in cams:
        cam.Init()
        print('cam serial number', cam.GetUniqueID())

