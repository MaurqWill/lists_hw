# Problem Statement:
# You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Task 1: Given the list of grades:

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.

# Task 2: Calculate the average grade and display it.

# Task 3: Replace any grade below 80 with the value Failed.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

grade_sum = sum(grades)
num_grades = len(grades)
average = grade_sum / num_grades
print(average)

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
        print(grades)

# Initialize an empty list to store failed grades
# failed_grades = []

# # Iterate over the grades and collect failed grades
# for grade in grades:
#     if grade < 80:
#         failed_grades.append(grade)
#         print(grades)

# for i in range(len(grades)):
#     if grades[i] < 80:
#         grades[i] = "Failed"
#         print(grades)
        

# You have two lists of student names. One list contains the names of students who have submitted their assignments,
# and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out which students both submitted their assignments and attended the class.

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]


submitted_and_attended = set(submitted).intersection(attended)
print("Students that submitted assignments and attended class:", submitted_and_attended)

identical_lists = set(submitted) == set(attended)
print("Are the lists identical?", identical_lists)

for student in attended[:]:
    if student not in submitted:
        attended.remove(student)

print("updated list:", attended)

# another method....this creates a new list without actually removing students

# attended = [student for student in attended if student in submitted]
# print(attended)

# Advanced Slicing Techniques

# You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# Extract the temperatures for the second week (7 days) of the month. Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

# Task 2: Extract all the temperatures above 100.

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 
                94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print(temperatures[7:14])

for i in temperatures:
    if i >= 100:
        print(i)

temperatures.reverse()
print(temperatures[5:10])

# Deep Dive into Python Lists

#  Given the lists:

# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]

# Filter out students who have grades below 80. Print the name, grade and activiy. 
# Expected Outcome "Jane", 78, "Art"

# Task 2: For the remaining students, add students name in a new list named students_approved. 
# Expected Outcome: students_approved = ["John", "Doe", "Smith"]

# Task 3: Print the list students_approved

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(students)):
    if grades[i] < 80:
        print(students[i], grades[i], activities[i])

# another way to do this is using the zip function
# zip function add lists/tuples together by index
# ex: 
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
# c = (1, 2, 3)

# x = zip(a, b, c)
#use the tuple() function to display a readable version of the result:

# print(tuple(x))

# for student, grade, activity in zip(students, grades, activities):
#     if grade < 80:
#         print(student, grade, activity)

students_approved = []
for i in range(len(students)):
    if grades[i] >= 80:
        students_approved.append(students[i])
        print(students_approved)









