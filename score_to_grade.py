

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above

# TODO-1: Create an empty dictionary called student_grades.


# TODO-2: Write your code below to add the grades to student_grades.


# 🚨 Don't change the code below
student_grade = {}
grade = ''

for key in student_scores:
    if 70 > student_scores[key] > 60:
        grade = 'C'
    elif 80 > student_scores[key] > 70:
        grade = 'B'
    elif 90 > student_scores[key] > 80:
        grade = 'A'
    elif 100 > student_scores[key] > 90:
        grade = 'S'
    else:
        grade = 'D'
    student_grade[key] = grade
# a = 0
# for key in student_grade:
#     key = student_scores[0]
#     grade = student_scores[key]
#     a += 1
print(student_grade)
