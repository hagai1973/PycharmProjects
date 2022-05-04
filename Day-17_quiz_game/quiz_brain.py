class QuizBrain:
    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def next_question(self, item):
        q = self.q_list[self.q_number].text
        question_answer = self.q_list[self.q_number].answer
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {q} (True/False)?: \n").lower()
        return self.check_answer(user_answer, question_answer)

    def game_round(self):
        greating = "let's continue"
        if self.q_number == len(self.q_list) - 1:
            greating = "Quiz completed"
        if self.next_question(self.q_list[self.q_number]):
            print(f"Good job, your score is: {self.score}/{len(self.q_list)}, {greating}")
            # return True
        else:
            print(f"Wrong answer...your score is: {self.score}/{len(self.q_list)}, lets continue")
            # return False
        print("\n")

    def check_answer(self, user_answer, question_answer):
        print(f"the correct answer is {question_answer}")
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def still_has_question(self):
        return self.q_number < len(self.q_list)
