file1= open("C:\\python inputs.txt","r")
n= int(file1.readline())
str1 = list(map(float, file1.readline().split()))
result=0
def arraychecksum(n,str1):
    for i in range(0,n):
        result+=str1[i]
        result*=113
        result%=10000007
    return (result)
print(int(result))