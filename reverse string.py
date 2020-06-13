file1= open("C:\\python inputs.txt","r")
str1 = list(map(str, file1.read().split()))
str2=[]
for i in range(0,len(str1)):
    for j in range(0,len(str1[i])):
        str2.append(str1[i][j])
    str2.append(" ")
print(str2)
str2.pop()
for i in range(len(str2)-1,-1,-1):
    print(str2[i],end="")