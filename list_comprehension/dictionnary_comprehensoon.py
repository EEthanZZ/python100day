# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.item() if}
import random
import pandas
# student_id = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
# }
#
# student = ["a", "b", "c", "d"]
# n = 1
# id = {i: n + student.index(i) for i in student}
# print(id)
#
# student_score = {i: random.randint(1, 100) for i in id}
# print(student_score)
# passed_score = {i: score for (i, score) in student_score.items() if score > 30}
# print(passed_score)

sentence = "How many charaters in this sentence"
x = sentence.split(" ")
sentence_cha = {i: len(i) for i in x}
print(sentence_cha)

# double the charaters length
d_sen_cha = {i: length*2 for i, length in sentence_cha.items()}
print(d_sen_cha)

stu_score = {
    "student": ["a", "b", "c"],
    "score": [10, 20, 30]
}

stu_data = pandas.DataFrame(stu_score)
print(stu_data)
for (k, v) in stu_data.iterrows():
    print(v["student"])
