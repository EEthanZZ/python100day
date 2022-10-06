from operator import itemgetter
from question_model import Question
from data import question_data
from tabulate import tabulate
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    ques_text = i['text']
    ques_ans = i['answer']
    question_data_new = Question(ques_text, ques_ans)
    question_bank.append(question_data_new)

# print(question_bank)
# header = question_bank[0].keys()
# rows = [i.values() for i in question_bank]
# print(tabulate(rows, header))

# print(tabulate(question_bank))

quiz = QuizBrain(questionList=question_bank)

while quiz.if_still_have_q():
    quiz.next_q()
