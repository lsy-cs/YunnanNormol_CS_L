#include <stdio.h>
int main(void)
{
	int d,i;
	printf("请输入一个整数:");
	scanf("%d",&d);
	if(d==1)
		printf("1不是素数");
	else if(d<=0)
		printf("Error");
	else
	{
		for(i=2;i<=d;i++)
		{
			if(d%i==0)
			{
				if(i<d)
					
				{
					printf("%d不是素数",d);
					break;
				}
				else
					printf("%d是素数",d);
			}
		}
	}
	return 0;
}
