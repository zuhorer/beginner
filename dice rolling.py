import math
file1=open("C:\\python inputs.txt","r")
n =int(file1.readline())
str=[]
for i in range(0,n):
    temp = math.modf(float(file1.readline())*6)
    str.append(temp[1])
for i in range(0,n):
    print(int(str[i]+1),end=" ")