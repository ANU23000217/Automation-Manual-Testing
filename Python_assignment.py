'''
1. Write a function calculate(a, b, operation) that performs addition, subtraction, multiplication, or 
   division based on the supplied operation.
'''
def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid operation"
a = int(input())
b = int(input())
operation = input()
print(calculate(a,b, operation))

'''
2. Write a function sum_numbers(*args) that accepts any number of arguments and returns their sum.
'''
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_numbers(10, 20))
print(sum_numbers(10, 20, 30))
print(sum_numbers(1, 2, 3, 4, 5))



'''
3. Write a function employee(**args) that accepts employee information such as name, ID, department and salary, 
   then displays the information.
'''
def emp(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
emp(
    name="Anu",
    ID=101,
    department="AI & DS",
    salary=30000
)


'''
4. Write a function remove_duplicates(lst) that returns a list containing only unique elements while
   preserving their original order.
'''
def dup(lis):
    res= []
    for i in lis:
        if i not in res:
            res.append(i)
    return res
lis = list(map(int, input().split()))
print(dup(lis))


'''
5. Using a lambda function, sort a list of tuples based on the second element. Example: [(1,5), (2,3), (4,1)].
'''
num = [(1, 5), (2, 3), (4, 1)]
num.sort(key=lambda x: x[1])
print(num)