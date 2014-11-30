#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Here is the answer!\n");
    float answer=(rand()%1000+1)/(float)(rand()%1005+1);
    printf("%f\n", answer);
    return 0;
}
