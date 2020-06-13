file1= open("C:\\python inputs.txt","r")
n = int(file1.readline())
swap=0
pas=1
finalswap=0
final=[]
str = list(map(int, file1.readline().split()))
for i in range(0, n):
    for k in range (len(str)-1,i,-1):
        if (str[k-1]>str[k]):
            temp= str[k-1]
            str[k-1]=str[k]
            str[k]= temp
            swap+=1

    if (swap!=0):
        pas+=1
        finalswap+=swap
        swap=0


final.append(pas)

final.append(finalswap)

for i in range(0,len(final)):
    print(final[i],end=" ")