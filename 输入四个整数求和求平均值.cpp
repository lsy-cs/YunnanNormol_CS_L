#include <stdio.h>

int main() {
	int a, b, c, d;
	int sum;
	double average;
	
	printf("请输入四个整数：");
	scanf("%d %d %d %d", &a, &b, &c, &d);
	
	sum = a + b + c + d;
	average = sum / 4.0;   // 注意用 4.0，保证进行浮点除法
	
	printf("和：%d\n", sum);
	printf("平均值：%.1f\n", average);
	
	return 0;
}


