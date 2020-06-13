file1= open("C:\\python inputs.txt","r")
n= int(file1.readline())

str1= [n]
i=0
s = list(map(str, file1.readline().split()))
while(s):
    if(s != 0):
        for j in range(0,2):
            str1.append(s[j])
    s *= 0
    s = list(map(str, file1.readline().split()))

for i in range(2, len(str1)-1,2):
    str1[i]=int(str1[i])

t=len(str1)-1
j=0
while(j<t):
    if(str1[j]=="*"):

        temp=str1[j-1]*str1[j+1]
        str1.pop(j)
        str1.pop(j)
        t -= 2
        if (temp>int(str1[t])):
            str1[j-1]=temp%int(str1[t])
        else:
            str1[j - 1] = temp
        j -= 1

    elif(str1[j] == "+"):
        temp = str1[j - 1] + str1[j + 1]
        str1.pop(j)
        t -= 1
        str1.pop(j)
        t -= 1
        if (temp > int(str1[t])):
            str1[j - 1] = temp % int(str1[t])
        else:
            str1[j - 1] = temp
        j-=1
    j+=1


if(str1[1]=="%"):
    str1[0]%=int(str1[2])
    str1.pop(1)
    str1.pop(1)

print (str1)