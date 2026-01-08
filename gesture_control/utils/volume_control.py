from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(direction):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current = volume.GetMasterVolumeLevelScalar()
    if direction == "up":
        volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)
    elif direction == "down":
        volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)
