#1

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

#2

"""
x=int(input("Enter a number:"))
for i in range(1, 11):
    print(x," x ",i," = ",x*i)
"""

#3

"""
numbers = [12, 75, 150, 180, 145, 525, 50]
n=[]
for i in numbers:
    if i%5==0:
        if i>150 and i<=500:
            continue
        elif i<=150:
            n.append(i)
        else:
            break
print(n)
"""

#4
"""
x=int(input("Enter a number:"))
count=1
for i in range(1,10):
    a=x/(10**i)
    if a >= 1:
        count=count+1
        
    else:
        break

print(count)

"""





#5
"""
numbers = [12, 75, 150, 180, 145, 525, 50]
n=[]
for i in range(len(numbers)-1,-1,-1):
    n.append(numbers[i])
print(n)
"""

#6
"""
s = int(input ("Enter the Value: "))  
e = int(input ("Enter the Value: "))  
  

for number in range (s, e + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number) 
"""