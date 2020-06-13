file1= open("C:\\python inputs.txt","r")
str1 = list(map(int, file1.readline().split()))
m=str1[0]
n=str1[1]
str2= list(map(int, file1.readline().split()))
a={}
temp=0
str3= []
for i in str2:
    if i in str3:
        a[i]=int(a[i])+1

    else:
        a[i]= '1'
        str3.append(i)
print(a)

for i in range(0,len(str3)):
    for j in range (0,i):
        if(str3[i]<str3[j]):
            temp= str3[j]
            str3[j]= str3[i]
            str3[i]=temp
print(str3)


for i in str3:
    print(a[i],end=" ")


