
"""
list1=[1,1,0,1,1,1,0,1,1,1,1]
i=0
x=[]
for a in list1:    
    if(a==1):
        i=i+1
    else:
        if a==0:
            
            i=0
        else:
            continue
    x.append(i)
print(max(x))
 """
#2
"""
list1=[1,1,0,1,1,1,0,1,1,1,1]
i=0
temp=0
for a in list1:
    if(a==1):
        i=i+1
    else:
        if a==0:
            i=0 
    if i>temp:
        temp=i

print(temp) 
"""

#Step function can be used in range
"""
for i in range(1,10,2):
    print(i)
"""

#print the sum of list
"""
data=[22,45,78,44,21]
s=0
for i in data:
    s=s+i
print(s)
"""
"""
n=int(input("Enter a number:"))
for i in range(0,n+1):
    print("*"*i)
"""

#Factorial
"""
n=int(input("Enter a number:"))
f=1
for i in range(1,n+1):
    f=f*i
print(f)
"""
#5
"""
l1=[1,1,2,3,4,4,5,5]
b = set(l1)
d={}
for i in b:
    d[i]=l1.count(i)
print(d)
"""

#6
"""
l=[2,3,4,4,4,5]
a=[]
x=int(input("Enter a number:"))
for i in range(0,len(l)):
    if x==l[i]:
        a.append(i)
    else:
        continue
print(min(a))
print(max(a))
"""

#7
"""
x=[1,8,2,9,21]
y=int(input("Enter a number:"))
for a in x:
    for b in x:
        if a+b==y:
            print(a,"and",b)
            
"""

#8
#Best Question

num=int(input("Enter a number of students:"))
d={}
for i in range(0,num):
    m={}
    name=input("Enter a name:")
    math=int(input("Enter marks in math:"))
    phy=int(input("enter marks in phy:"))
    chem=int(input("Enter marks in chem:"))
    m["math"]=math
    m["phy"]=phy
    m["chem"]=chem
    d[name]=m
    x=[]
    x.append(m.get("math"))
    x.append(m.get("phy"))
    x.append(m.get("chem"))
    
print(d)
    
n1=input("enter a name:")
print(d[n1])
a=d[n1].values()
total=sum(a)
avg=total/3
print(avg)
highest=max(a)
l2=[]
#Tricky part
for key,value in d[n1].items():
    if value == highest:
         l2.append(key)

print(l2)
"""
count=0
n=int(input("Enter a number:"))
for i in range(n+1,0,-1):
    print(count*" ",i*"*")
    count+=1
"""

"""
a=20
b=10
a-=b
b+=a
print(a)
print(b)
"""

