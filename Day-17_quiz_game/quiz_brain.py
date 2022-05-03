class Game:
    def __init__(self, question_number, question_list):
        self.q_number = question_number
        self.q_list = question_list

    def ask_question(self, item):
        q = item.text
        q_response = input(f"Q.{self.q_number}: {q} (True/False)?: \n").lower()
        if str(item.answer).lower() == q_response.lower():
            return True
        else:
            return False

    def game_round(self):
        if self.ask_question(self.q_list[self.q_number]):
            print("good answer, lets continue")
            return True
        else:
            print("wrong answer, game over")
            return False
