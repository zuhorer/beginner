import math
file1= open("C:\\python inputs.txt","r")
n= int(file1.readline())
final=[]
sum=0.0
for i in range (0,n):
    str1 = list(map(float, file1.readline().split()))
    for j in range(0,len(str1)-1):
        sum+=str1[j]
    temp= math.modf(sum/(len(str1)-1))
    if(temp[0]>=0.5):
        sum= temp[1]+1
    else:
        sum=temp[1]
    final.append(int(sum))
    print(final)
    sum=0
for i in range(0,len(final)):
    print(final[i],end=" ")