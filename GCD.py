file1 = open("C:\\python inputs.txt","r")
n = int(file1.readline())
str1= []
str2=[]
for i in range(0,n):
    str1= list(map(int, file1.readline().split()))
    print(str1)
    a=str1[0]
    b=str1[1]
    lcm=0
    while(str1[0] != str1[1]):
        if(str1[0] > str1[1]):
            str1[0] -= str1[1]
        elif(str1[1] > str1[0]):
            str1[1] -= str1[0]
    lcm= (a*b)/str1[1]
    str2.append("(")
    str2.append(str1[1])
    str2.append(" ")
    str2.append(int(lcm))
    str2.append(") ")
for i in range(0,len(str2)):
    print(str2[i],end="")



