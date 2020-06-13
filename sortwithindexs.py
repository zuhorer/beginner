file1= open("C:\\python inputs.txt","r")
n = int(file1.readline())
str1=list(map(int, file1.readline().split()))
str2=dict((str1[i],i+1)for i in range(0,n))
temp=0
for i in range(0,n):
    for j in range(0,i):
        if (str1[i]<str1[j]):
            temp=str1[i]
            str1[i]=str1[j]
            str1[j]=temp
print(str1)
for i in range(0,n):
    print(str2[str1[i]],end=" ")

