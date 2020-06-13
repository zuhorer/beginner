import string
file1= open("C:\\python inputs.txt","r")
n = int(file1.readline())
str2=[]
str3=[]
for i in range(0,n):
    str1= list(map(str,file1.readline().split()))
    tru=1
    for j in range(0,len(str1)):
        for k in range(0,len(str1[j])):
            if(65<ord(str1[j][k])<90)|((97<ord(str1[j][k])<122)):
                if(str1[j][k].islower()):
                    str2.append(str1[j][k])
                else:
                    str2.append(str1[j][k].lower())
    print(str2)
    if len(str2) % 2 != 0:
        str2.pop(int((len(str2) - 1) / 2))
        print(str2)
        for s in range(0,int(len(str2)/2)):
            if (str2[s]!=str2[len(str2)-s-1]):
                tru+=1
                break
        if(tru==1):
            str3.append("Y")
        else:
            str3.append("N")

    elif len(str2)%2==0:
        for s in range(0,int(len(str2)/2)):
            if (str2[s]!=str2[len(str2)-s-1]):
                tru+=1
                break
        if(tru==1):
            str3.append("Y")
        else:
            str3.append("N")
    for s in range(0,len(str2)):
        str2.pop()



for i in range(0,len(str3)):
    print(str3[i],end=" ")