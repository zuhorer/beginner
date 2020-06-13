file1= open("C:\\python inputs.txt","r")
n = int(file1.readline())

str = []
BMI= 0.0
final=[]

for i in range(0, n):
    str = list(map(float, file1.readline().split()))
    BMI = str[0]/(str[1]**2)
    if (BMI<18.5):
        final.append("under")

    elif((BMI>=18.5)&(BMI<25)):
        final.append("normal")

    elif ((BMI >= 25) & (BMI<30)):
        final.append("over")

    elif (BMI > 30):
        final.append("obese")


for j in range(0,n):
    print(final[j],end=" ")
