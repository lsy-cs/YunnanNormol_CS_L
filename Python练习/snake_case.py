n=int(input("输入行数n:"))
for i in range(0,n):
    print(2*(i-1)*" ")
    line=2*(n-i)*chr(65+i)
    print(line)

