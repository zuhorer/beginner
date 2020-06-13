import math
n = list(map(float, input().split()))
final=[]
for i in range(1,len(n)):
    cel=(n[i]-32)*(5/9)
    a=math.modf(cel)
    if a[0]>0:
        if a[0]>0.5:
            final.append(int(a[1])+1)
        else:
            final.append(int(a[1]))
    elif a[0]>0:
        if a[0]<-0.5:
            final.append(int(a[1])-1)
        else:
            final.append(int(a[1]))
    else:
        final.append(int(a[1]))

for j in range(0, len(final)):
    print(final[j],end=" ")


