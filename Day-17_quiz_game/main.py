import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# q1 = Question("2+2=4", "True")
#
# print(f"question:  {q1.text}, answer: {q1.answer}")


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

game = QuizBrain(question_bank)
print(game.game_round())





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
