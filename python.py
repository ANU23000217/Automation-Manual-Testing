'''
1.	Print all prime numbers between input range (Ex input 20 50, prints all prime numbers between 20 and 50).
'''

st = int(input())
e = int(input())
for i in range(st, e+1):
    isprime= True
    if i < 2:
        isprime= False
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            isprime=False
            break
    else:
        print("Prime nos: ", i) 

'''
2.	Factorial using recursion
'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)
n = int(input())
print(fact(n))

'''
3.	Square of numbers using lambda
'''
x=int(input())
sq = lambda x : x**2 
print(sq(x))

'''
4.	Find the second largest element in a list
'''
def sec_lar(arr):
    largest = float('-inf')
    second = float('-inf')
    for n in arr:
        if n >largest:
            second = largest
            largest = n
        elif n >second or n!=largest:
            second = n
    return second
arr = list(map(int, input().split()))
print(sec_lar(arr))

'''
5.	Count frequency of characters in a string
'''
def frequency(str):
    freq = {}
    for ch in str:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch] =1
    return freq
str = input()
print(frequency(str))


'''
6.	Calculate area of a circle using math library.
'''
import math
radius = int(input())
area = math.pi*radius**2     #area = 3.14*radius**2
print("Area of circle", area)


'''
7.	Reverse a string without using built‑in reverse
'''

str = input()
reverse =""
for ch in str:
    reverse = ch+reverse
print(reverse)

'''
8.	Remove duplicates from a list
'''
li = list(map(int, input().split()))
seen = set()
uni = set()
for c in li:
    if c in seen:
        uni.add(c)
    else:
        seen.add(c)    
print(seen)


'''
9.	Merge two dictionaries
'''

dict1 = eval(input())
dict2 = eval(input())
print(dict1 | dict2) 

'''
10.	Fibonacci series using recursion
'''
def fib(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
n = int(input())
print(fib(n))
