import ctypes
from dataclasses import dataclass

#Mirror the C struct



class ProcessInfo(ctypes.Structure):
    _fields_ = [
        ("pid", ctypes.c_int),
        ("uid", ctypes.c_int),
        ("rss_kb", ctypes.c_int),
    ]

class Policy(ctypes.Structure):
    _fields_ = [
        ("enforce_non_negative_rss", ctypes.c_bool),
        ("normalize_uid", ctypes.c_bool),
    ]

@dataclass

class PyProcess:
    pid: int
    uid: int
    rss_kb: int

    @property
    def is_root(self):
        return self.uid == 0

#Load shared C library object



def format_table(process_list:list) -> str:
    lines = []
    pid_width = max(len("PID"),
                max(len(str(p.pid)) for p in process_list)
    )
    # name_width = max(len("NAME"),
    #             max(len(p["name"]) for p in process_list)
    # )

    uid_width = max(len("UID"),
                max(len(str(p.uid)) for p in process_list)
    )
    rss_width = max(len("RSS_KB"),
                max(len(str(p.rss_kb)) for p in process_list)
    )

    header = (
        f"{'PID':<{pid_width}}  "
        # f"{'NAME':<{name_width}}  "
        f"{'UID':<{uid_width}}  "
        f"{'RSS_KB':<{rss_width}}  "
    
    )
    lines.append(header)
    lines.append("-" * len(header))

    for p in process_list:
        row = (
            f"{p.pid:<{pid_width}}  "
            # f"{process['name']:<{name_width}}  "
            f"{p.uid:<{uid_width}}  "
            f"{p.rss_kb:<{rss_width}}"
        )
        lines.append(row)

    return "\n".join(lines)


def main():
    process_list = [] 

    lib = ctypes.CDLL("./process_lib/target/release/libprocess_lib.so")

    ## Define the function signature
    lib.get_processes.argtypes = [ctypes.POINTER(ProcessInfo), ctypes.c_int, Policy]
    lib.get_processes.restype = None

    ##Create policy instance
    policy = Policy(
        True,
        True
    )

    #ALLOCATE THE BUFFER OR CREATE THE MEMORY
    count = 5
    ProcessArray = ProcessInfo * count
    buffer = ProcessArray()


    ##Call the function
    lib.get_processes(buffer, count, policy)
    for i in range(count):
        p = buffer[i]
        process_list.append(
            PyProcess(p.pid,p.uid,p.rss_kb)
        )
    print(format_table(process_list))
   

if __name__ == "__main__":
    main()
    