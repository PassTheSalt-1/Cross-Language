#include <stdio.h>

//Define a struct 

typedef struct {
    int pid;
    int uid;
    int rss_kb;
} ProcessInfo;

//fill buffer with dummy data

void get_processes(ProcessInfo *buffer, int count) {
    for (int i = 0; i < count; i++) {
        buffer[i].pid = 1000 + 1;
        buffer[i].uid = i % 2 == 0 ? 0 : 1000; // alternate root/non-root
        buffer[i].rss_kb = (i + 1) * 512;
    }
}