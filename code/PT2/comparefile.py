import os


def compare_files(file1, file2):
    cmd = 'diff -u %s %s' % (file1, file2)
    stream = os.popen(cmd)
    output = stream.read()
    return output


file1 = './print_tokens.c'
# file1 = './source.alt/source.orig/tokens.h'
file2 = './versions.alt/versions.orig/v7/print_tokens.c'
different_lines = compare_files(file1, file2)

