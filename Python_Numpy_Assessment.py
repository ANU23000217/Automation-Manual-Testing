#!/usr/bin/env python
# coding: utf-8

# ## NAME : ANU RADHA N
# ## REG NO: 212223230018

# In[1]:


import numpy as np


# In[3]:


'''
Question 1 – Student Marks Array
The marks obtained by five students in a subject are given as [78, 65, 89, 56, 92]. Create a NumPy array and display 
the array along with its basic properties.
'''
marks = np.array([78, 65, 89, 56, 92])
print("Marks:", marks)
print("Number of dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Data type:", marks.dtype)


# In[4]:


'''
Question 2 – Student Marks Access
The marks of five students are stored in a NumPy array as [72, 85, 64, 90, 76]. Write a program to access and display
specific student marks using NumPy indexing and slicing.
'''
marks = np.array([72, 85, 64, 90, 76])
print("Marks:", marks)
print("First student:", marks[0])
print("Third student:", marks[2])
print("Last student:", marks[-1])
print("First three students:", marks[0:3])
print("Second to fourth students:", marks[1:4])
print("Last two students:", marks[-2:])


# In[5]:


'''
Question 3 – Subject-wise Marks
The marks obtained by five students in three subjects are given below. Create a NumPy array to represent the data 
and reshape it into an appropriate matrix format.
[78, 85, 90, 65, 72, 80, 88, 91, 84, 56, 62, 70, 95, 89, 92]
'''
marks = np.array([
    78, 85, 90,
    65, 72, 80,
    88, 91, 84,
    56, 62, 70,
    95, 89, 92
])

matrix = marks.reshape(5, 3)
print("Original array:")
print(marks)
print("\nMarks Matrix:")
print(matrix)


# In[6]:


'''
Question 4 – Internal and External Marks
The internal and external examination marks of five students are stored in two NumPy arrays. 
Write a program to calculate the final marks of each student using NumPy array operations.
'''
internal = np.array([50,60,90,34, 88])
external = np.array([75, 88, 34, 55, 45])

final_marks = internal + external

print("Internal Marks:", internal)
print("External Marks:", external)
print("Final Marks:", final_marks)


# In[7]:


'''
Question 5 – Pass Percentage Analysis
The marks obtained by five students are [45, 78, 56, 32, 91]. Using NumPy Boolean masking, identify the students
who have secured 50 marks or above.
'''
marks = np.array([45, 78, 56, 32, 91])
passed = marks[marks >= 50]
print("Marks:", marks)
print("Students scoring 50 or above:", passed)


# In[9]:


'''
Question 6 – Average Marks
The marks of five students in three subjects are represented using a NumPy matrix.
Write a program to calculate the average marks of each student
'''
marks = np.array([
    [78, 85, 90],
    [65, 72, 40],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 90]
])

average = np.mean(marks, axis=1)
print("Marks:")
print(marks)
print("\nAverage marks of each student:")
print(average)


# In[10]:


'''
Question 7 – Class Performance Statistics
The marks obtained by five students are [67, 82, 91, 74, 58]. Using NumPy statistical functions, determine the total, 
average, highest, lowest, and standard deviation of the marks.
'''
marks = np.array([67, 82, 91, 74, 58])
print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Standard Deviation:", np.std(marks))


# In[12]:


'''
Question 8 – Subject-wise Performance
The marks of five students in three subjects are stored in a NumPy matrix. Write a program to calculate the 
total marks obtained in each subject using an appropriate axis operation
'''
marks = np.array([
    [78, 85, 45],
    [65, 72, 30],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 88]
])

sub_total = np.sum(marks, axis=0)
print("Marks:")
print(marks)
print("\nTotal marks in each subject:")
print(sub_total)


# In[15]:


'''
Question 9 – Student-wise Performance
The marks of five students in three subjects are stored in a NumPy matrix. Write a program to calculate the 
total marks obtained by each student using an appropriate axis operation.
'''
marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 66]
])
stu_total = np.sum(marks, axis=1)
print("Marks:")
print(marks)
print("\nTotal marks of each student:")
print(stu_total)


# In[14]:


'''
Question 10 – Student Ranking
The total marks obtained by five students are [245, 278, 219, 290, 256]. Use NumPy sorting and indexing operations 
to arrange the marks in order and determine the ranking of the students.
'''
marks = np.array([245, 278, 219, 290, 256])
sorted_marks = np.sort(marks)
ranking = np.argsort(marks)[::-1]
print("Original marks:", marks)
print("\nMarks in ascending order:")
print(sorted_marks)
print("\nStudent ranking:")
for rank, index in enumerate(ranking, start=1):
    print("Rank", rank, "- Student", index + 1, "-", marks[index])


# In[16]:


'''
Question 11 – Duplicate Marks Analysis
The marks obtained by five students are [85, 92, 85, 76, 92]. Use NumPy functions to identify
the unique marks obtained by the students.
'''
marks = np.array([85, 92, 85, 76, 92])
uni_marks = np.unique(marks)
print("Marks:", marks)
print("Unique marks:", uni_marks)


# In[17]:


'''
Question 12 – Missing Marks
The marks of five students are represented as [78, 85, np.nan, 92, 67], where np.nan represents a missing mark. 
Write a NumPy program to calculate the average marks without considering the missing value.
'''
marks = np.array([78, 85, np.nan, 92, 67])
avg = np.nanmean(marks)
print("Marks:", marks)
print("Average without missing value:", avg)


# In[19]:


'''
Question 13 – Grade Classification
The marks obtained by five students are [95, 82, 74, 61, 45]. Using NumPy conditional operations, 
classify the students into appropriate grade categories based on their marks.
'''
marks = np.array([95, 82, 74, 61, 45])

grades = np.select(
    [ marks >= 90, marks >= 80, marks >= 70, marks >= 60 ],
    
    [ "A", "B","C", "D" ],
    
    default="F"  )
print("Marks:", marks)
print("Grades:", grades)


# In[20]:


'''
Question 14 – Random Marks Generation
Generate marks for five students using NumPy's random number generation functionality.
Perform basic statistical analysis on the generated marks
'''
np.random.seed(10)
marks = np.random.randint(0, 204, 5)
print("Randomly generated marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Standard deviation:", np.std(marks))


# In[21]:


'''
Question 15 – Student Performance Analysis
The marks of five students in three subjects are stored in a NumPy array. 
Develop a program to perform a complete student performance analysis by calculating the total marks, average marks, 
highest marks, lowest marks, and identifying students who perform above the class average.
'''
marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84],
    [56, 62, 70],
    [95, 89, 92]
])
total = np.sum(marks, axis=1)

avg = np.mean(marks, axis=1)

highest = np.max(marks, axis=1)

lowest = np.min(marks, axis=1)

class_avg = np.mean(marks)

above_avg = np.where(avg > class_avg)[0]

print("Student Marks:")
print(marks)

print("\nTotal marks:")
print(total)

print("\nAverage marks:")
print(avg)

print("\nHighest marks:")
print(highest)

print("\nLowest marks:")
print(lowest)

print("\nClass average:", class_avg)

print("\nStudents above class average:")

for index in above_avg:
    print("Student", index + 1)


# In[ ]:




