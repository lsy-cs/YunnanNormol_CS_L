y=int(input("请输入年份："))
condi=(y%4==0)&(y%100!=0)|(y%400==0)
if condi==True:
    print(y,"是闰年")
else:
    print(y,"不是闰年")   

