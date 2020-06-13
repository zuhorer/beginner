file1= open('C:\python inputs.txt','r')
n= int(file1.readline())

str1= list(map(int,file1.readline().split()))
str3=[]
str4= ""
str5=[]
a=1
str6=[]
for i in range(0, n):
    str2= str(str1[i]*str1[i])

    while(a!=0):
        for j in range(0,len(str2)):
            str3.append(str2[j])

        while (len(str3)<8):
            str3.insert(0,'0')

        str4="".join(str3)

        str5.append(int(str4[2:6]))
        str2=str(int(str4[2:6])**2)
        for k in range(0,len(str5)-1):
            if(str5[len(str5)-1] == str5[k]):
                a=0
                str6.append(len(str5))
                str5.clear()
                break
        str3.clear()
    a=1
for i in range(0,n):
    print(str6[i],end=" ")

