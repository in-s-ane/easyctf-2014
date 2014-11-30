#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

/* After running this, clean up the QR Code in an image editor + invert colors
 * Flag: pixelsmatterinQRs */

int main() {
    int image1 = open("1.bmp", O_RDONLY);
    int image2 = open("2.bmp", O_RDONLY);
    int clear = open("solution.bmp", O_CREAT | O_TRUNC, 0644);
    close(clear);
    int output = open("solution.bmp", O_CREAT | O_WRONLY | O_APPEND, 0644);
    unsigned char buf1;
    unsigned char buf2;
    unsigned char outputbuf;
    int same = 1;
    while (read(image1, &buf1, 1) > 0 && read(image2, &buf2, 1) > 0) {
        if (buf1 == buf2 && same) { // Hack to not alter the header of the file
            outputbuf = buf1;
        }
        else {
            same = 0;
            outputbuf = buf1 ^ buf2; // Runs XOR on the individual pixels
        }
        printf("%d\t%d\t%d\n", buf1, buf2, outputbuf);
        write(output, &outputbuf, 1);
    }
    return 0;
}
