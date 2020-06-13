n= list(map(int,input().split()))
a=[]
for i in range (1,len(n),2):
    if(n[i]<=n[i+1]):
        a.append(n[i])
    else:
        a.append(n[i+1])

for j in range(0,n[0]):
    print(a[j],end=" ")