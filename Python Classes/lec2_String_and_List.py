# Python Slicing
'''
x="Hello World"
print(a[-1])
print(a[1:5])
print(a[::-1])
'''
#Python Input
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=a+b
print(c)
'''

#Length function and methods
'''
x="Hello World"

print(len(x))
print(x.upper())
print(x.lower())
'''

# List
'''
list = [1,"hello",3.3]
print(list[1][1])
'''
'''
my_list = [1,2,3,["hello",[["python"]]],4,5,6]
print(my_list[3][1][0][0])
'''

#List methods
'''
my_list = ['a','b']
my_list.append(1)
my_list.insert(2,1)
list1=my_list.copy()
print(list1)'''

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

"""
a=[1,2,3,4,5,6,7,8,9,10]
print(a[1::2])
for i in a:
    if i%2==0:
        print(i)"""