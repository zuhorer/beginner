n= list(map(int, input().split()))
length= n[0]
sum=0
for i in range(1, length+1):
    sum+=n[i]
print (sum)