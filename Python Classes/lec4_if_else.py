#1
#Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

"""
a=int(input("Enter a number"))
if a%5==0:
    print("Hello")
else:
    print("Bye")
"""
#2
#Write a program to check whether a number entered by user is even or odd.

"""
a=int(input("Enter a number"))
if a%2==0:
    print("even")
else:
    print("odd")
"""
#3
#Write a program to check whether a number is divisible by 7 or not.

"""
a=int(input("Enter a number"))
if a%7==0:
    print("Number is divisible")
else:
    print("Number is not divisible")
"""

#4
#Write a program to check whether a person is eligible for voting or not.

"""
a=int(input("Enter your age"))
if a>=18:
    print("Eligible")
else:
    print("Not Eligible")
"""

#5
#Write a program to display the last digit of a number.

"""
a=input("enter a number")
b=int(a[-1])
print(b)
"""

#6
#Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

"""
a=input("enter a number")
b=int(a[-1])

if b%3==0:
    print("Divisible")
else:
    print("Not Divisible")
"""

#7
#Write a program to calculate the electricity bill (accept number of unit from user)

"""
x=int(input("enter number"))
if x<=100:
    price=0
elif x>100 and x<=200:
    price=(x-100)
    price=price*5
elif x>200:
    price=500+(x-200)*10

print(price)
"""

#8
#Write a program to accept percentage from the user and display the grade

"""
marks=int(input("Enter total marks"))
if marks>90:
    print("Grade: A")
elif marks>80 and marks<=90:
    print("Grade: B")
elif marks>60 and marks<=80:
    print("Grade: C")
else:
    print("Grade: D")
"""

#9
#Write a program to check whether a user entered letter is present in the word

"""
a='Ansh'
b=input("Enter a letter")
if b in a:
    print("Letter is present")
else:
    print("Letter is not present")
"""

#10
#Write a program to accept the cost price of a bike and display the road tax to be paid

"""
x=int(input("Enter cost price"))
if x>100000:
    tax=15
elif x>50000 and x<=90:
    tax=10

else:
    tax=5
print(tax)
"""

#11
#Write a program to check whether an years is leap year or not.

"""
x=int(input("Enter a year"))
if x%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
"""

#12
#Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

"""
x=int(input("Enter a number from 1 ton 7:"))
if x==1:
    print("Monday")
elif x==2:
    print("Tuesday")
elif x==3:
    print("Wednesday")
elif x==4:
    print("Thursday")
elif x==5:
    print("Friday")
elif x==6:
    print("Saturday")
elif x==7:
    print("Sunday")
else:
    print("Invalid Number")
"""

#13
#Write a program to accept a number from 1 to 12 and display name ofthe month and days in that month like 1 for January and number of
# days 31 and so on
"""
x=int(input("Enter a number from 1 ton 12:"))
if x==1:
    print("Jan and number of days 31")

elif x==2:
    print("Feb and number of days 28")
elif x==3:
    print("March and number of days 31")
elif x==4:
    print("April and number of days 30")
elif x==5:
    print("May and number of days 31")
elif x==6:
    print("June and number of days 30")
elif x==7:
    print("July and number of days 31")
elif x==8:
    print("August and number of days 31")
elif x==9:
    print("Sept and number of days 30")
elif x==10:
    print("Oct and number of days 31")
elif x==11:
    print("Nov and number of days 30")
elif x==12:
    print("Dec and number of days 31")
else:
    print("Invalid Number")
"""

#14
#Accept any city from the user and display monument of that city.
"""
x=input("Enter a city name:")
if x=="Delhi":
    print("Red Fort")
elif x=="Agra":
    print("Taj Mahal")
elif x=="Jaipur":
    print("Jal Mahal")
else:
    print("No monument Present")
"""

#15
#Write a program to check whether a number entered is three digit number or not.
""""
x=input("Enter a three digit number")
if len(x)==3:
    print("It is three digit number")
else:
    print("It is not a three digit number")
"""

#16
#Write a program to find the largest number out of two numbers excepted from user.
"""
a=int(input("enter a number"))
b=int(input("Enter another number"))
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("both are equal")
"""

#17
#Write a program to find the lowest number out of two numbers excepted from user.
"""
a=int(input("enter a number"))
b=int(input("Enter another number"))
if a>b:
    print(b)
elif a<b:
    print(a)
else:
    print("both are equal")
"""


#18
#Write a program to check whether a number (accepted from user) is positive or negative.
"""
a=int(input("Enter another number"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("number is zero")
"""

#19
#Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
"""
a=int(input("Enter another number"))
if a%2==0 and a%3==0:
    print("the number is divisible")
else:
    print("not divisible")
"""

#20
#Accept the age of 4 people and display the youngest one?
"""
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
d=int(input("enter a number"))
if a<b and a<c and a<d:
    print(a)
elif b<a and b<c and b<d:
    print(b)
elif c<a and c<b and c<d:
    print(c)
else:
    print(d)
"""

#21
#Write a program to check whether a number is prime or not.
"""
a=int(input("Enter a number"))
for i in range(2,int(a/2)):
    if a%i==0:
        x=1
        break
    else:
        x=0

if a==0 or a==1:
    x=1

if x==1:
    print("The number is not prime")
else:
    print("number is prime")
"""
#22
#Write a program to check a character is vowel or not.
"""
x=input("enter something:")
if 'a' or 'e' or 'i' or 'o' or 'u' in x:
    print("vowel is present")
else:
    print("no vowels")
"""

#23
#Accept the following from the user and calculate the percentage of class attended

#After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam.
"""
working_days=int(input("Enter the total number of working day:"))
absent_days=int(input("Enter total absent days:"))
present_days=working_days-absent_days
percentage=(present_days/working_days)*100
print(percentage)
if percentage >= 75:
    print("You will be able to sit in the exam")
else:
    print("You will not be able to sit in the exam")
"""

#24
#A company decided to give bonus to employee according to following criteria

#Ask user for their salary and years of service and print the net bonus amount.
"""
sal=int(input("enter your salary:"))
years=int(input("enter years of service:"))

if years >10:
    bonus=(sal*10)/100
elif years >=6 and years <=10:
    bonus=(sal*8)/100
else:
    bonus=(sal*5)/100
print(bonus)
"""

#25
#Accept the marked price from the user and calculate the Net amount as(Marked Price – Discount) to pay
"""
mp=int(input("Enter a amount:"))
if mp>10000:
    net_amount=mp-(mp*0.2)
elif mp>7000 and mp<=10000:
    net_amount=mp-(mp*0.15)
else:
    net_amount=mp-(mp*0.1)
print(net_amount)
"""

#26
#Write a program to accept percentage and display the Category
"""
p=int(input("Enter total marks"))
if p<40:
    print("Failed")
elif p>=40 and p<55:
    print("Fair")
elif p>=55 and p<65:
    print("Good")
elif p>=65 and p<=100:
    print("Excellent")
"""

#27
#Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
"""
side1=int(input("Enter the length of side:"))
side2=int(input("Enter the length of side:"))
side3=int(input("Enter the length of side:"))
if side1 == side2 and side2==side3:
    print("equilateral Triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("isosceles Triangle")
else:
    print("scalene Triangle")
"""

#28
#Write a program to accept two numbers and mathematical operators and perform operation accordingly.
"""
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("Mathematical operations that can be perform")
print("1:addition")
print("2:subtraction")
print("3:multiplication")
print("4:division")
x=int(input("Enter the index of mathematical operations"))
if x==1:
    print(a+b)
elif x==2:
    print(a-b)
elif x==3:
    print(a*b)
else:
    print(a/b)
"""
#29
#Write a Python program to get next day of a given date.
"""
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
"""

#30
"""
age=int(input("Enter your age"))
gender=input("Enter your gender")
if gender=="M" or gender=="m":
    if age>=18 and age<30:
        daily_wage=700
    elif age>=30 and age<=40:
        daily_wage=800
else:
    if age>=18 and age<30:
        daily_wage=750
    elif age>=30 and age<=40:
        daily_wage=850
print(daily_wage)
"""

