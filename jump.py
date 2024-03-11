# ---------------------------------------------------------------------------
from pymem import *
from pymem.process import *

offsets = [0x8, 0xDC8, 0x10, 0x88, 0xAC, 0xF0]

pm = Pymem('javaw.exe')
address = pm.allocate(10)
gameModule = module_from_name(pm.process_handle, 'jvm.dll').lpBaseOfDll

print("[!] Successfully Injected! ")

def GetPointer(base, offsets):
    addr = pm.read_longlong(base+0x007E17D8)
    print("Address > ",hex(addr))
    for offset in offsets:
        if offset != offsets[-1]:
            try:
                addr = pm.read_longlong(addr + offset)
            except Exception as e:
                print("Exceptions > 0x",e)
    return addr + offsets[-1]

while True:
    pm.write_int(GetPointer(gameModule, offsets), 65537)
