n = list(map(float, input().split()))
a=[]
for i in range (1,len(n), 3):
    sum= (n[i+2]/2)*(2*n[i]+(n[i+2]-1)*n[i+1])
    a.append(int(sum))
for j in range(0,len(a)):
    print(a[j],end=" ")
