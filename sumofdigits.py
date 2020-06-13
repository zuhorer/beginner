n= list(map(int,input().split()))
a=[]
sum=0
for i in range (1,len(n),3):
    digit=str(n[i]*n[i+1]+n[i+2])
    dig=list(map(int,digit))
    for j in range (0,len(dig)):
        sum+=dig[j]
    a.append(sum)
    sum=0
for j in range(0,n[0]):
    print(a[j],end=" ")