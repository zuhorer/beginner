file1= open("C:\\python inputs.txt","r")
n = int(file1.readline())
a={}
str1=[]
str2=[]
a["("]=")"
a["["]="]"
a["{"]="}"
a["<"]=">"
for i in range (0,n):
    str1= list(map(str,file1.readline().split()))
    for j in range(0,len(str1)):
        for k in range(0,len(str1[j])):
            str2.append(str1[j][k])
    for j in range(0, len(str1)):

print(str2)
