file1= open('C:\\python inputs.txt', "r")
n = int(file1.readline())
q=[]
for i in range(0,n):
    q.append(file1.readline())

count=[]
c=0
for i in range(0,n):
    for j in q[i]:
        if (j== "a")|(j== "e")|(j== "i")|(j== "o")|(j== "u")|(j== "y"):
            c+=1
    count.append(c)
    c=0
for k in range(0,n):
    print(count[k],end=" ")