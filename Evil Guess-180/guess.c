#include <stdio.h>
#include <stdlib.h>

int main()
{
        int bufA=(int)malloc(12); // Casts pointer to memory as an int
        //printf("Pointer to bufA: %d \t Pointer dereferenced: %d\n", bufA, *((int *) bufA));
        float * guess=(float *)bufA;
        float * answer=(float *)(bufA+4);
        //printf("Pointer to guess: %d \t Pointer dereferenced: %d\n", guess, *guess);
        //printf("Pointer to answer: %d \t Pointer dereferenced: %d\n", answer, *answer);
        *answer=(rand()%1000+1)/(float)(rand()%1005+1);
        printf("Answer: %.20f\n", *answer); // Need lotsa precision to get this to work
        printf("\nPlease enter in a float to guess: ");
        scanf("%lf",guess);
        printf("\nanswer: %.10f, guess: %.10f\n",*answer, *guess); // Print out answer and guess with lotsa precision
        if(*answer/(*guess)==1.0)
        {
                printf("\nThe flag is '<flag hidden>'\n");
        }else{
                printf("\nSorry, that is not the secret number\n");
        }

        printf("%d\n", bufA);
        free(bufA);
}
