file1= open("C:\\python inputs.txt","r")

n = int(file1.readline())
str=[]
x=[0,0]
final=[]
for i in range(0,n):
    str = list(map(int, file1.readline().split()))

    a= float(str[3]-str[1])/(str[2]-str[0])
    b= int(str[1]-(a*str[0]))
    a=int(a)
    final.append("(")
    final.append(a)
    final.append(" ")
    final.append(b)
    final.append(") ")


for i in range(0,len(final)):
    print(final[i],end="")
