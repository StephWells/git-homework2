#Solutions
#Solution 1

#practicing f-string for headers
#practicing right adjust to right align numbers
print(f"{'Number':>20}{'Square':>20}{'cube':>20}")
for x in range (0,6):
    print(repr(x).rjust(20), repr(x*x).rjust(20), end= ' ')
    print(repr(x*x*x).rjust(20))


#Solution 2

ftemp1=(-40)
ftemp2=(0)
ftemp3=(40)
ftemp4=(100)
celsius1=int((ftemp1-32)*5/9)
celsius2=int((ftemp2-32)*5/9)
celsius3=int((ftemp3-32)*5/9)
celsius4=int((ftemp4-32)*5/9)
print("Tempurature:", "F=", ftemp1, "C=", celsius1)
print("Tempurature:", "F=", ftemp2, "C=", celsius2)
print("Tempurature:", "F=", ftemp3, "C=", celsius3)
print("Tempurature:", "F=", ftemp4, "C=", celsius4)


#Solution 3
numbers = input("Hi, please Input three integers seperated by space so that I may calculate their sum and average.")
numberList = numbers.split()

print("\n")

#Calculating sum of entered numbers
sum1 = 0
for num in numberList:
    sum1 += int(num)
print("The sum is", sum1)


average = sum1 / len(numberList)
print("The average is", average)






