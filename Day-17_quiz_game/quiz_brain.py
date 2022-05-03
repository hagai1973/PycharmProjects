class QuizBrain:
    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list

    def next_question(self, item):
        q = self.q_list[self.q_number].text
        q_response = input(f"Q.{self.q_number + 1}: {q} (True/False)?: \n").lower()
        if str(item.answer).lower() == q_response.lower():
            return True
        else:
            return False

    def game_round(self):
        if self.next_question(self.q_list[self.q_number]):
            print("good answer, lets continue")
            return True
        else:
            print("wrong answer, game over")
            return False
