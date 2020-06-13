n = list(map(int,input().split(" ")))


length=n[0]
sum=0
a=[]
for i in range (1,len(n)-1,2):
    sum=sum+(n[i])
    i+=1
    sum=sum+(n[i])
    i+=1
    a.append(sum)
    sum=0
for j in range (0,length):
    print(a[j],end=" ")

