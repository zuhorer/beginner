file1= open("C:\\python inputs.txt","r")
str1= list(map(int, file1.readline().split()))
str1.pop()
temp=0
swap=0
pas=0
result=0
for i in range(1,len(str1)):
    if (str1[i]<str1[i-1]):
        swap+=1
        temp=str1[i]
        str1[i]=str1[i-1]
        str1[i-1]=temp
    else:
        pas+=1
for i in range(0, len(str1)):
    result += str1[i]
    result *= 113
    result %= 10000007
print(swap,result)