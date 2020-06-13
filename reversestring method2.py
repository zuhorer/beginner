file1= open("C:\\python inputs.txt","r")
n= int(file1.readline())

for i in range(0, n):
    str0 = list(map(str, file1.readline().split()))

def swap(str1,n):
    str2=[]
    for j in range(0,len(str1)):
        str2.append(str1[1][j])
        for j in range(0,2*n):
                temp=str2[j]
                str2[j]=str2[(2*n)-1-j]
                str2[len(str2) - 1 - j]=temp
        

