# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.item() if}
import random

student_id = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

student = ["a", "b", "c", "d"]
n = 1
id = {i: n+student.index(i) for i in student}
print(id)

student_score = {i:random.randint(1, 100) for i in id}
print(student_score)
passed_score = {i: score for (i, score) in student_score.items() if score >30}
print(passed_score)