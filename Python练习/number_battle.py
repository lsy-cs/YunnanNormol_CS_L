n=int(input())
#a=[0]*n
a=input().split()
b=c=0
for i in range(0,n):
    a[i]=int(a[i])
    if(a[i]>a[b]):
        b=i
    elif(a[i]<a[c]):
        c=i
print(a[b])
print(a[c])
print(b+1)    

        
        