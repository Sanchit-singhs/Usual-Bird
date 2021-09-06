# to check whether a number is odd or even by user input
"""""
x = int(input("enter a number"))
y = x%2
if y == 0:
    print("x is even")
else:
    print("x is odd")
"""""
# to print numbers between 0 to 65
"""
import math
for x in range(0,65):
    print(x)
"""
# to print hi 10 times
"""""
i = 0
while i in range(10):
    print("hi")
    i = i+1
"""
# getting user defined candy
"""""
x = int(input("Enter the number of candy"))
i = 1
while i in range(x+1):
    print("candy")
    i = i+1
"""""
# break statement(jump out of the loop)
"""""
x = int(input("Enter the number of candy"))
available = 65
i = 1
while i <= x:
    if i > available:
        print('out of stock')
        break
    print("candy")
    i = i+1
"""""
# use of continue(skip)
"""
for x in range(101):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)
"""
# odd number between 0 to 100
"""""
for x in range(101):
    if x%2==0:
        continue
    print(x)
"""""
# pass statement
"""
for x in range(101):
    if x%2 == 0:
        pass
    else:
        print(x)
"""
# to print a pattern
"""
for x in range(5):
    print()
    for i in range(5):
        print("#", end="")
"""
"""
x = int(input("enter number of rows"))
for i in range(x):
    for x in range(i):
        print("#", end="")
    print()
"""
"""
x = int(input("enter any number"))
for i in range(x):
    for y in range(x-i):
        print("#", end="")
    print()
"""
# for else statement
"""
x = [1,2,3,4,6,18]
for i in x:
    if i%5 == 0:
        print(i)
        break
else:
    print("no element")
"""
# to check a number is a prime number or not
"""
x = int(input("enter the number"))
for i in range(2,x):
    if x % i == 0:
        print("Given number is not a prime number")
        break
else:
    print("prime number")
"""
# Creating an array
"""
import array as arr
x = arr.array('i', [7, 3, 84, 4])
print(x)
"""
"""
import array
# To create an array
arr = array.array('i', [])
x = int(input("enter the size of array"))
for i in range(x):
    y = int(input("enter the value"))
    arr.append(y)
print(arr)
# To check whether an element is present in an array
val = int(input("enter the value to search"))
k = 0
for w in arr:
    if w == val:
        print(k)
        break
    k = k + 1
else:
    print("not in array")
# To add value to the array
arr.append(int(input("enter the value")))
print(arr)
"""
"""
# To get fibonacci sequence
def fibonacci(x):
    a = 0
    b = 1
    print(0)
    print(1)
    for i in range(x):
        c = a + b
        a = b
        b = c
        print(c)
fibonacci(10)
"""
# To get a factorial of a number
"""
def fac(x):
    y = 1
    for i in range(1,x+1):
        y = y*i
    return y
print(fac(5))
"""
# Recursion
"""
def fac(x):
    if x == 0:
        return 1
    return x*fac(x-1)
print(fac(5))
"""
# Lambda function
"""
x = lambda a: a*a
print(x(5))
"""
