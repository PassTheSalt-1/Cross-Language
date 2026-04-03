import ctypes

#Mirror the C struct
class ProcessInfo(ctypes.Structure):
    _fields_ = [
        ("pid", ctypes.c_int),
        ("uid", ctypes.c_int),
        ("rss_kb", ctypes.c_int)
    ]

#Load shared C library object

lib = ctypes.CDLL("./libprocess.so")

## Explictly tell python the return type
lib.get_process_info.argtypes = [ctypes.c_int]
lib.get_process_info.restype = ProcessInfo

##Call the function

p = lib.get_process_info(42)

print("PID",p.pid)
print("UID",p.uid)
print("RSS_KB",p.rss_kb)
