
class QuizBrain():
    def __init__(self, questionList):
        self.question_number = 0
        self.question_list = questionList
        self.score = 0

    def if_still_have_q(self):
        return self.question_number < len(self.question_list)

    def next_q(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text}")
        self.check_anser(user_answer, current_q.answer)

    def check_anser(self, useranswer, quizanswer):
        if useranswer.lower() == quizanswer.lower():
            print("right")
            self.score += 1
        else:
            print("wrong")
        print(f'{self.score}/{self.question_number}')
