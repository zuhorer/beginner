n= list(map(int,input().split()))
a=[]
for i in range (1,len(n),3):
    if(n[i]<=n[i+1]):
        if(n[i]<=n[i+2]):
            a.append(n[i])
        else:
            a.append(n[i+2])
    else:
        if(n[i+1]<=n[i+2]):
            a.append(n[i+1])
        else:
            a.append(n[i+2])

for j in range(0,n[0]):
    print(a[j],end=" ")