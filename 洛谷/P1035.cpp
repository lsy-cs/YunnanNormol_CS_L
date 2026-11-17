#include <stdio.h>
int main()
{
	int k,n=0;
	scanf("%d",&k);
	double i,S=0;
	for(i=1;S>k;i++)
	{
		S+=(1/i);
		n++;
	}
	printf("%.d",n);
	return 0;
}
