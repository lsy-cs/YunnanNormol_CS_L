#include <stdio.h>
int n=0;
char trans(char ch)
{
	//scanf("%c",&ch);
	ch=(ch+n-'a')%26+'a';
	return ch;
}
int main()
{   
	char ch;
	scanf("%d",&n);
	while(scanf("%c",&ch)==1)
		if(ch<='z'&&ch>='a')
			printf("%c",trans(ch));
	return 0;
}
