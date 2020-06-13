file1= open("C:\\python inputs.txt","r")

n = int(file1.readline())

str= list(map(str, file1.readline().split()))
print(str)

sum=0
for i in range(0,n):
    str1=list(str[i])
    for j in range(0,len(str1)):

        sum+=int(str1[j])*(j+1)
    str[i]=sum
    sum=0
for i in range(0,n):
    print(str[i],end=" ")