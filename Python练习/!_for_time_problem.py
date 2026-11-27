import time
start=time.time()
aum=num=1
for i in range(1,101):
    aum*=i
    num=num+(1/aum)
print(num)
time.sleep(1)
end=time.time()
print(end-start,"秒")