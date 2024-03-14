from pymem import *
from pymem.process import *
import keyboard

offsets = [0x48, 0xDC8, 0x10, 0x88, 0xAC, 0x204, 0x8A8]

pm = Pymem("javaw.exe")
address = pm.allocate(10)
gameModule = module_from_name(pm.process_handle, 'jvm.dll').lpBaseOfDll

def GetPointer(base, offsets):
    addr = pm.read_longlong(base+0x007E17B8)
    print('Address : ', hex(addr))
    for offset in offsets:
        if offset != offsets[-1]:
            try:
                addr = pm.read_longlong(addr + offset)
            except Exception as e:
                print("Exception : ", e)
    
    return addr + offsets[-1]

while True:
    if keyboard.is_pressed("q"):
        pm.write_double(GetPointer(gameModule, offsets), 0.900)
