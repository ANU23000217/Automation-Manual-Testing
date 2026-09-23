'''
Write a Python program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''
binary = input()
b= binary.split(",")   # if you print b - o/p is ['0100', '0011', '1010', '1001]
for n in b:
    decimal = int(n, 2)   # converting decimal to binary with base 2
    if decimal%5==0:
        print(n)

'''
Write a Python program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

s1 = "Hello world! 123"
letter=0
digit=0
for ch in s1:
    if ch.isalpha():
        letter +=1
    elif ch.isdigit():
        digit +=1
print("LETTERS:", letter)
print("DIGITS:", digit)

-Without isalpha and isdigit--
s1 = "Hello world! 123"

letter = 0
digit = 0
for ch in s1:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        letter += 1
    elif '0' <= ch <= '9':
        digit += 1
print("LETTERS:", letter)
print("DIGITS:", digit)

'''
Write a program which can compute the factorial of a given numbers.The
results should be printed in a comma-separated sequence on a single
line.Suppose the following input is supplied to the program:8
Then, the output should be:40320
'''

f = int(input())
fact =1
for i in range(1, f+1):
    fact*=i
print(fact)
