#include <stdio.h>
int main()
{
	int i,j,n=0,m=0,money=0,k;
	for(i=1;i<=12;i++)
	{
		k=0;
		scanf("%d\n",&j);
		n+=300;
		n-=j;
		if(n<0)
		{
			printf("-%d",i);
			break;
		}
		else if(n>=100)
		{
			k=(n/100)*100;
			n-=k;
			money+=k;
		}
		m++;
	}
	if(m==12)
		printf("%d",n+money*120/100);
	return 0;
}
