file1= open("C:\\python inputs.txt","r")
n = int(file1.readline())
temp=0
final=[]
for i in range(0,n):
    str = list(map(int, file1.readline().split()))
    for j in range(0,3):

        for k in range(0,3):
            if(str[k]>str[j]):
                temp = str[k]
                str[k] = str[j]
                str[j] = temp
    final.append(str[1])
for i in range(0,n):
    print(final[i],end=" ")