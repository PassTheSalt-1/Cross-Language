#include "filemeta.h"
#include <sys/stat.h>

FileMetadata get_file_metadata(const char* path) {
    struct stat st;
    FileMetadata meta = {0, 0};

    if (stat(path, &st) == 0) {
        meta.size_bytes = st.st_size;
        meta.permissions = st.st_mode;
    }

    return meta;
}