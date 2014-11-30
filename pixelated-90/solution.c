#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int image1 = open("1.bmp", O_RDONLY);
    int image2 = open("2.bmp", O_RDONLY);
    int clear = open("solution.bmp", O_CREAT | O_TRUNC, 0644);
    close(clear);
    int output = open("solution.bmp", O_CREAT | O_WRONLY | O_APPEND, 0644);
    unsigned char buf1;
    unsigned char buf2;
    unsigned char outputbuf;
    while (read(image1, &buf1, 1) > 0 && read(image2, &buf2, 1) > 0) {
        outputbuf = buf1 & buf2;
        printf("%d\t%d\t%d\n", buf1, buf2, outputbuf);
        write(output, &outputbuf, 1);
    }
    return 0;
}
