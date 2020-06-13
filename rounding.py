import math
n= list(map(float, input().split()))
length=int(n[0])
final=[]
for i in range(1, len(n),2):
    mod= n[i]/n[i+1]
    a= math.modf(mod)
    if(a[0]>0):
        if (a[0]>=0.5):
            final.append(int(a[1]+1))
        else:
            final.append(int(a[1]))
    elif(a[0]<0):
        if (a[0]<=-0.5):
            final.append(int(a[1]-1))
        else:
            final.append(int(a[1]))
    else:
        final.append(int(a[1]))





for j in range(0,length):
    print (final[j], end=" ")
