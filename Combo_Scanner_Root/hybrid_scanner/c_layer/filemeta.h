#ifndef FILEMETA_H
#define FILEMETA_H

typedef struct {
    long size_bytes;
    unsigned int permissions;
} FileMetadata;

FileMetadata get_file_metadata(const char* path);

#endif