#include <stdio.h>
int main()
{
	int i,j,n,m=1;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n-i+1;j++)
		{
			if(m<10)
				printf("0%d",m);
			else
				printf("%d",m);
			m++;
		}
		printf("\n");
	}
	return 0;
}
