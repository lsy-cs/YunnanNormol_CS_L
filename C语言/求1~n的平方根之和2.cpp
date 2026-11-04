#include  <stdio.h>

#include <math.h>

int main(void)

{
	int n,i;
	double sum;
	printf("请输入一个正整数n：");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		sum+=sqrt(i);
	}
	printf("1~%d的平方根之和为：%.2lf",n,sum);
	return 0;    
}


