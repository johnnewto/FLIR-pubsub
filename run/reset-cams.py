import PySpin

_SYSTEM = PySpin.System.GetInstance()
# reSet cameras
cams = _SYSTEM.GetCameras()
for cam in cams:
    cam.Init()
    print('cam', cam.GetUniqueID())
    cam.DeviceReset.Execute()
    # cam.DeInit()

    # del cam

cams.Clear()
# _SYSTEM.ReleaseInstance()