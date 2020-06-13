file1= open("C:\\python inputs.txt","r")

n = int(file1.readline())
str1 = list(map(int, file1.readline().split()))
print(str1)
str2=[]
count=0

for i in range(0,n):
    num=str1[i]
    while(num!=1):
        count+=1
        if (num%2==0):
            num/=2
        else:
            num=3*num+1
    str2.append(count)
    count=0
for i in range(0,n):
    print(str2[i],end=" ")