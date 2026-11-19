#include <stdio.h>
int n;
int peach(int d)
{
	if(d==1) return 1;
	return (peach(d-1)+1)*2;
}

int main()
{
	
	scanf("%d",&n);
	printf("%d",peach(n));
	return 0;
}
