file1= open("C:\\python inputs.txt","r")
n = int(file1.readline())
str2=[]

for i in range (0,n):
    r=1.0
    str1 = list(map(float, file1.readline().split()))
    for j in range(0,int(str1[1])):
        r=(r+(str1[0]/r))/2
    str2.append(r)
for i in range(0,len(str2)):
    print(str2[i],end=" ")