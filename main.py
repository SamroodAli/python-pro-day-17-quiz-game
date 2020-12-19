from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    correct_answer = quizbrain.next_question()
    user_answer = input("Enter your answer [ true or false ]: \n").lower()
    quizbrain.check_answer(user_answer, correct_answer)

print("You have completed the quiz")
print(f"Your final score was: {quizbrain.score}/{quizbrain.question_number}")
