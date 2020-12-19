class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text}\n[ true or false ]").lower()
        return current_question.answer == user_answer

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
