import math
a,b,c=eval(input("请输入a,b,c三条边:"))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("三角形的面积是:",S)
