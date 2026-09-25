'''
1. A college maintains the daily attendance details of its students in the form of a list containing student IDs. 
Some students may have attended multiple sessions on the same day. The administration wants to identify the longest 
continuous sequence of sessions in which no student ID is repeated. Develop a solution that determines the maximum 
length of such a sequence.
'''

def stuatt(arr):
    uni = set()
    left =0
    max_len=0
    for right in range(len(arr)):
        if arr[right] in uni:
            uni.remove(arr[left])
            left+=1
        uni.add(arr[right])
        max_len = max(max_len, right-left+1)
    return max_len

arr = list(map(int,input().split()))
print(stuatt(arr))


'''
2. Online Shopping Price Analysis
An online shopping application stores the prices of products viewed by a customer during a browsing session. 
The customer wants to identify a continuous range of products that provides the maximum possible total discount value. 
Given the discount values, determine the maximum value that can be obtained from any continuous range.
'''

def priceprod(arr):
    curr_sum = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_val = max(max_val, curr_sum)
    return max_val
arr = list(map(int, input().split()))
print(priceprod(arr))


'''
3. Rainwater Collection System
A city installs buildings of different heights along a straight road. During rainfall, water gets collected between 
taller buildings. The engineering team needs to calculate the total amount of water that can remain trapped after 
heavy rainfall based on the heights of the buildings.
'''

def trap(arr):
    left = 0
    right = len(arr) - 1
    left_max = 0
    right_max = 0
    total = 0
    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                total += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                total += right_max - arr[right]
            right -= 1
    return total
arr = list(map(int, input().split()))
print(trap(arr))


'''
4. Employee Performance Analysis
A company stores the monthly performance scores of an employee for several months. 
The scores may contain both positive and negative values depending on the employee's performance. 
Management wants to identify the continuous period during which the employee achieved the highest overall performance.
'''
def scores(arr):
    curr_sum = arr[0]
    max_val = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_val = max(max_val, curr_sum)
    return max_val
arr = list(map(int, input().split()))
print(scores(arr))

'''
5. Product Sales Analysis
A retail company stores the daily sales quantity of a product for several consecutive days. 
Due to seasonal changes, some days may have negative adjustments. The company wants to identify the period that produced 
the highest multiplication of sales-related values. Develop a solution to determine this maximum product.
'''

def prod(arr):
    curr_max = arr[0]
    curr_min = arr[0]
    res = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            curr_max, curr_min = curr_min, curr_max
        curr_max = max(arr[i], curr_max * arr[i])
        curr_min = min(arr[i], curr_min * arr[i])
        res = max(res, curr_max)
    return res
arr = list(map(int, input().split()))
print(prod(arr))

'''
6. Customer Purchase History
An e-commerce application stores the product IDs purchased by a customer in chronological order. 
The same product may appear multiple times. The system needs to determine the longest sequence of consecutive purchases
 in which every product ID is unique.
'''

def proid(arr):
    uni = set()
    left = 0
    max_len =0
    for right in range(len(arr)):
        if arr[right] in uni:
            uni.remove(arr[left])
            left+=1
        uni.add(arr[right])
        max_len = max(max_len, right+left-1)
    return max_len
arr = list(map(int, input().split()))
print(proid(arr))

'''
7. Bank Transaction Analysis
A bank stores transaction amounts for a customer's account. A continuous group of transactions may add up to a specific
target amount. The auditing system needs to determine how many different continuous transaction groups produce exactly 
the specified amount.
'''

def transaction(arr, target):
    count = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == target:
                count += 1
    return count
arr = list(map(int, input().split()))
target = int(input())
print(transaction(arr, target))

'''
8. Employee Skill Grouping
A company receives a list of employee skill codes represented as strings. Employees having the 
same set of characters in their skill codes belong to the same skill category, even if the characters appear in a 
different order. The HR system needs to organize employees into appropriate skill groups.
'''
def emp(words):
    groups = {}
    for ch in words:
        key = ''.join(sorted(ch))
        if key not in groups:
            groups[key] = []
        groups[key].append(ch)
    return list(groups.values())
words = input().split()
print(emp(words))

'''
9. Network Packet Analysis
A network monitoring system receives packet identifiers in chronological order. 
The system must determine the longest sequence of consecutive packets whose identifiers form a continuous numerical sequence,
 regardless of their original order in the incoming data.
'''

def packet(arr):
    nums = set(arr)
    max_len = 0
    for num in nums:
        if num - 1 not in nums:
            curr = num
            curr_len = 1
            while curr + 1 in nums:
                curr += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len
arr = list(map(int, input().split()))
print(packet(arr))


'''
10. Hospital Appointment Scheduling
A hospital receives appointment requests represented by starting and ending times. Some appointments overlap with each other. 
The scheduling system needs to combine overlapping appointment periods so that the final schedule contains only non-overlapping
time ranges.
'''

def hosp(intervals):
    intervals.sort()
    res = []
    for interval in intervals:
        if not res:
            res.append(interval)
        else:
            prev = res[-1]
            if prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                res.append(interval)
    return res
intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
print(hosp(intervals))