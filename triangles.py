file1= open("c:\\python inputs.txt", "r")

n= int(file1.readline())
str=[]
final=[]
for i in range(0,n):
    str= list(map(int, file1.readline().split()))
    if(str[0]+str[1]<=str[2])|(str[0]+str[2]<=str[1])|(str[1]+str[2]<=str[0]):
        final.append('0')
    else:
        final.append('1')
for i in range(0,n):
    print(final[i],end=" ")
