#include <stdio.h>
long long fact(int n)
{
	static long long r = 1;      
	if (n <= 1) return r;
	r*=n;                      
	return fact(n - 1);          
}

int main()
{
	int i;
	scanf("%d",&i);
	printf("%lld",fact(i));
	return 0;
}
