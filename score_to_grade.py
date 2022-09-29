

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


# method 2

student_grade2 = {}
for i in student_scores:
    grade2 = student_scores[i]
    if grade2 > 90:
        student_grade2[i] = "S"
        grade2 = student_scores[i]
    elif grade2 > 80:
        student_grade2[i] = "A"
        grade2 = student_scores[i]
    elif grade2 > 70:
        student_grade2[i] = "B"
        grade2 = student_scores[i]
    elif grade2 > 60:
        student_grade2[i] = "C"
    else:
        student_grade2[i] = "D"
print(student_grade2)
