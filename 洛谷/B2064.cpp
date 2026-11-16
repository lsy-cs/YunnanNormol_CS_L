#include <stdio.h>
int fibo(int n)
{
	//int s;
	if(n==1)
		return 1;
	if(n==2)
		return 1;
	//s=fibo(n);
	//fibo(n-1);
	return (fibo(n-1)+fibo(n-2));
	//return s;
}
int main()
{
	int i,a,b;
	scanf("%d",&i);
	for(a=1;a<=i;a++)
	{
		scanf("%d",&b);
		printf("%d\n",fibo(b));
	}
	return 0;
}
