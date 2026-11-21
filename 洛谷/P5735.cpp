#include <stdio.h>
#include <math.h>
double dis(double x1,double y1,double x2,double y2)
{
	double s,a,b;
	a=pow(x2-x1,2);
	b=pow(y2-y1,2);
	s=sqrt(a+b);
	return s;
}
int main()
{
	double x1,y1,x2,y2,x3,y3,a,b,c,C;
	scanf("%lf %lf\n",&x1,&y1);
	scanf("%lf %lf\n",&x2,&y2);
	scanf("%lf %lf\n",&x3,&y3);
	a=dis(x1,y1,x2,y2);
	b=dis(x1,y1,x3,y3);
	c=dis(x2,y2,x3,y3);
	C=a+b+c;
	printf("%.2lf",C);
	return 0;
}
