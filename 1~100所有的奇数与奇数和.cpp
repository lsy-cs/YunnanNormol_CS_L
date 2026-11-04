#include <stdio.h>
int main(void)

{
	int count = 0,i=1;   
	printf("1-100以内的所有奇数为：");
	printf("\n");   
	for ( i = 1; i <= 100; i++)		
	{   		
		if(i%2!=0)
		{
			printf("%4d", i);                 
			count++;                      
			if (count % 6 == 0)
			{
				printf("\n");
			}
		}
	}  	
	int sum=0;	
	for(i=1;i<=100;i+=2)		
	{		
		sum+=i;		
    }
	printf("\n");
	printf("奇数之和：%d\n", sum);
	return 0;
}


