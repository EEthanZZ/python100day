from operator import itemgetter
from question_model import Question
from data import question_data
from tabulate import tabulate


question_bank = []
for i in question_data:
    question_data = Question(i['text'], i['answer'])
    question_bank.append(i)

# print(question_bank)
header = question_bank[0].keys()
rows = [i.values() for i in question_bank]
print(tabulate(rows, header))
