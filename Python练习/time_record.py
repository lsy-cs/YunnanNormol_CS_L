import time
start_time=time.time()
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i+j+k==100 and 3*i+2*j+k/2==100:
                print(i ,j ,k)
time.sleep(1)
end_time=time.time()
print("程序运行时间：",end_time-start_time,"秒")