#include <stdio.h>
int main(void)
{
	int a,b,c,d;
	int max,min;
	printf("请输入四个整数，用空格隔开：");
	scanf("%d %d %d %d",&a,&b,&c,&d);
	max=a;
	if(b>max) max=b;
	if(c>max) max=c;
	if(d>max) max=d;
	min=a;
	if(b<a) min=b;
	if(c<a) min=c;
	if(d<a) min=d;
	printf("最大值： %d，最小值： %d\n",max,min);
	return 0;
}


