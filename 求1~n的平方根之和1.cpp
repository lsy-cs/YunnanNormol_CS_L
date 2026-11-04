#include  <stdio.h>

#include <math.h>

int main(void)

{
	int n,i;
	double x;
	printf("请输入一个正整数n：");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		x+=sqrt((double)i);
	}
	printf("1~%d的平方根之和为：%.2lf",n,x);
	return 0;	
}


