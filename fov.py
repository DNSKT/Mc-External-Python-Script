from pymem import *
from pymem.process import *
import keyboard

offsets = [0xD0, 0x260, 0x270, 0x298, 0x8C, 0x30, 0xA8]

fov =  float(input("fov: "))

pm = Pymem("javaw.exe")
address = pm.allocate(10)
gameModule = module_from_name(pm.process_handle, 'jvm.dll').lpBaseOfDll

def GetPointer(base, offsets):
    addr = pm.read_longlong(base+0x007E1AF0)
    print('Address : ', hex(addr))
    for offset in offsets:
        if offset != offsets[-1]:
            try:
                addr = pm.read_longlong(addr + offset)
            except Exception as e:
                print("Exception : ", e)
    
    return addr + offsets[-1]
print("press Q to execute")
while True:
    if keyboard.is_pressed("q"):
        pm.write_float(GetPointer(gameModule, offsets), fov)
        print("press R to reverse")
    elif keyboard.is_pressed("r"):
        pm.write_float(GetPointer(gameModule, offsets), float(110))