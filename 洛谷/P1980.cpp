#include <stdio.h>
int main(void)
{
	int i,j=0,m,n;
	scanf("%d %d",&n,&m);
	m>=0&&m<=9;
	for(i=1;i<=n;i++)
	{
		if(i<10&&i==m)
			j++;
		if(i>=10&&i%10==m)
			j++;
		if(i>=10&&i/10==m)
			j++;
	}
	printf("%d",j);
	return 0;
}
