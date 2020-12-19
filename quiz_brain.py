class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        print(f"Q{self.question_number}: {current_question.text}\n[ true or false ]")
        return current_question.answer

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right")
            print("Current score: ", self.score)
        else:
            print("You got it wrong.")
        return self.score
