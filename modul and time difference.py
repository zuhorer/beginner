file1= open("C:\\python inputs.txt","r")
n= int(file1.readline())
final=[]
temp=[]
flag=0
for i in range(0,n):
    str= list(map(int,file1.readline().split()))
    final.append("(")
    for j in range(7,3,-1):
        if (str[j] > str[j-4]):
            if (flag == 1):
                temp.append(str[j]-str[j-4]-1)

            else:
                temp.append(str[j]-str[j-4])
            flag=0
        else:
            if(j!=5):
                if(flag == 1):
                    temp.append(59-(str[j-4]-str[j]))
                else:
                    temp.append(60-(str[j-4]-str[j]))
                flag =1
            else:
                if (flag == 1):
                    temp.append(23 - (str[j - 4] - str[j]))
                else:
                    temp.append(24 - (str[j - 4] - str[j]))

                flag = 1
    for k in range(3,-1,-1):
        final.append(temp[k])
        final.append(" ")
    temp *= 0
    final.pop()
    final.append(") ")


for i in range(0,len(final)):
        print(final[i],end="")