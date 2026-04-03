#include <stdio.h>

//Define a struct 

typedef struct {
    int pid;
    int uid;
    int rss_kb;
} ProcessInfo;

// Function that returns a struct
ProcessInfo get_process_info(int pid) {
    ProcessInfo p;

    p.pid = pid;
    p.uid = pid % 1000;
    p.rss_kb = pid * 2;

    return p;
}