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

## Define the function signature
lib.get_processes.argtypes = [ctypes.POINTER(ProcessInfo), ctypes.c_int]
lib.get_processes.restype = None

#ALLOCATE THE BUFFER OR CREATE THE MEMORY
count = 5
ProcessArray = ProcessInfo * count
buffer = ProcessArray()


##Call the function
lib.get_processes(buffer, count)

process_list = [] 

for i in range(count):
    p = buffer [i]
    process_list.append({
        "pid":p.pid,
        "uid":p.uid,
        "is_root":(p.uid == 0),
        "rss_kb":p.rss_kb
    })

def format_table(process_list:list) -> str:
    lines = []
    pid_width = max(len("PID"),
                max(len(str(p["pid"])) for p in process_list)
    )
    # name_width = max(len("NAME"),
    #             max(len(p["name"]) for p in process_list)
    # )

    uid_width = max(len("UID"),
                max(len(str(p["uid"])) for p in process_list)
    )
    rss_width = max(len("RSS_WIDTH"),
                max(len(str(p["rss_kb"])) for p in process_list)
    )

    header = (
        f"{'PID':<{pid_width}}  "
        # f"{'NAME':<{name_width}}  "
        f"{'UID':<{uid_width}}  "
        f"{'RSS_KB':<{rss_width}}  "
    
    )
    lines.append(header)
    lines.append("-" * len(header))

    for process in process_list:
        row = (
            f"{process['pid']:<{pid_width}}  "
            # f"{process['name']:<{name_width}}  "
            f"{process['uid']:<{uid_width}}  "
            f"{process['rss_kb']:<{rss_width}}"
        )
        lines.append(row)

    return "\n".join(lines)

print(format_table(process_list))