#Solutions
#Solution 1

#practicing f-string for headers
#practicing right adjust to right align numbers
print(f"{'Number':>20}{'Square':>20}{'cube':>20}")
for x in range (0,6):
    print(repr(x).rjust(20), repr(x*x).rjust(20), end= ' ')
    print(repr(x*x*x).rjust(20))


#Solution 2

ctemp1=(-40)
ctemp2=(0)
ctemp3=(40)
ctemp4=(100)
ftemp1=int((9/5*ctemp1)+32)
ftemp2=int((9/5*ctemp2)+32)
ftemp3=int((9/5*ctemp3)+32)
ftemp4=int((9/5*ctemp4)+32)
print("Tempurature:", "C=", ctemp1, "F=", ftemp1)
print("Tempurature:", "C=", ctemp2, "F=", ftemp2)
print("Tempurature:", "C=", ctemp3, "F=", ftemp3)
print("Tempurature:", "C=", ctemp4, "F=", ftemp4)


#Solution 3
numbers = input("Hi, please Input three integers seperated by space so that I may calculate their sum and average.")
numberList = numbers.split()

print("\n")

#Calculating sum of entered numbers
sum1 = 0
for num in numberList:
    sum1 += int(num)
print(f'The sum is {sum1: ,d}')


#Calculating average of entered numbers
average = sum1 / len(numberList)
print("The average is", "{:,.2f}".format(average))







