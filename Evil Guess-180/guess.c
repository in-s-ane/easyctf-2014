#include <stdio.h>
#include <stdlib.h>
 
int main()
{
	/*printf("Welcome to the guessing game!\n");
	printf("Please enter your name: ");
	char * str=(char *)malloc(25);
	scanf("%20s",str);*/
        char *str = "Danny";
	printf("\nHello, %s\nPlease enter in a float to guess: ",str);
        float * bufA=(float *)malloc(12);
	float * guess=(float *)bufA;
	float * answer=(float *)(bufA+4);
        float num = rand()%1000+1;
        float den = rand()%1005+1;
	*answer=num/den;
	scanf("%lf",guess);
        printf("\n%f\n%f", num, den);
	printf("\na: %lf, b: %lf\n",*answer, *guess);
	if(*answer/(*guess)==1.0)
	{
		printf("\nThe flag is '<flag hidden>'\n");
	}else{
		printf("\nSorry, that is not the secret number\n");
	}
	free(bufA);
	//free(str);
}
