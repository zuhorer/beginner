
file1= open("C:\\python inputs.txt","r")
n= int(file1.readline())
str2=[]
str3=[]
str4=[]
str5=""
for i in range(0,n):
    str1=list(map(str,file1.readline().split()))
    s= int(str1[0])
    for j in range(0, len(str1[1])):
        str2.append(str1[1][j])
    if(s<0):

        count=s
        while(count!=0):
            str3.append(str2[count])
            str2.pop(count)
            count+=1
        for l in range(s,0):
            str2.insert(0,str3[-l-1])

        str4.append(str5.join(str2))

        str5=""


    else:
        count=s
        while(count!=0):

            k=0
            str3.append(str2[k])
            str2.pop(k)
            count-=1
        for l in range(0,s):
            str2.append(str3[l])
        str4.append(str5.join(str2))
        str5=""
    for j in range(0,len(str3)):
        str3.pop()
    for j in range(0, len(str2)):
        str2.pop()
for i in range(0,n):
    print(str4[i],end=" ")