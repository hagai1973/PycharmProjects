import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


game = QuizBrain(question_bank)
while game.still_has_question():
    (game.game_round())

print(f"You've completed the quiz")
print(f"Your final score was: {game.score}/{len(game.q_list)} ")



# question_bank = []
# num_items = len(data.question_data)
# question_name = ""
#
# for i in range(num_items):
#     question_name = "q_" + str(i)
#     question_name = Question(data.question_data[i].get("text"), data.question_data[i].get("answer"))
#     question_bank.append(question_name)
#
# print(question_bank)

# print(data.question_data[0].get("answer"))

# question_bank = [
#     Question(data.question_data[0].get("text"),data.question_data[0].get("answer"))
# ]
