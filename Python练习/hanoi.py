def hanoi(n,A,B,C):
    global t
    if n==1:
        print(n,"从",A,"->",C)
        t=t+1
    else:
        hanoi(n-1,A,C,B)
        print(n, "从", A, "->", C)
        hanoi(n-1,B,A,C)
        t=t+1
t=0
n=int(input("输入n:"))
hanoi(n, "A", "B", "C")
print("移动了",t,"次")