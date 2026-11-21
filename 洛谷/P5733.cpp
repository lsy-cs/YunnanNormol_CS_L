#include <stdio.h>
char trans(char a)
{
	if(a>='a'&&a<='z')
	{
		a-=32;
		return a;
	}
	else if(a>='A'&&a<='Z')
		return a;
	else
		return a;
}
int main()
{
	char ch;
	while (scanf("%c", &ch) == 1)
	{
		if (ch == '\n') break;     
		putchar(trans(ch));
	}
	
	return 0;
}
