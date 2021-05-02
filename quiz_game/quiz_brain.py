class Quiz():

    def __init__(self, q_bank):
        self.question_bank = q_bank
        self.user_answer = bool()
        self.question_number = 0
        self.right_answers = 0

    def ask_question(self):
        while self.still_has_question():
            question = self.question_bank[self.question_number]
            print(f"Current Score: {self.right_answers}/{self.question_number}")
            self.question_number += 1
            self.user_answer = True if input(f"Q.{self.question_number}: {question.q_text} (True/False)") == 't' else False
            self.check_answer(question)

    def check_answer(self, question):
        if question.q_answer == str(self.user_answer):
            self.right_answers += 1
            print("Seikou!\n")
        else:
            print("Batsu...\n")

    def still_has_question(self):
        return self.question_number < len(self.question_bank)
