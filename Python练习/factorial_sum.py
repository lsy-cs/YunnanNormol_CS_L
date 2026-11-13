def fact(x):  # 将 fib 改为 fact，明确功能是阶乘
    y = 1
    for i in range(1, x + 1):  # 将 n 改为 x
        y = y * i
    return y

print("请输入n:")
n = int(input())
print("请输入m:")
m = int(input())
# 计算组合数
C = fact(n) // (fact(m) * fact(n - m))  # 用 // 确保结果为整数
print(C)