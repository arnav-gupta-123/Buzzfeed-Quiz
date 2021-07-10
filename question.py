class Question:
    def __init__(self, text, answers, correct_answer, points):
        self.text = text
        self.answers = answers
        self.correct_answer = correct_answer
        self.points = int(points)

    def __str__(self):
      i = 0
      x = self.text
      while i < len(self.answers):
        x = x + "\n" + str(i + 1) + ":" + str(self.answers[i])
        i += 1
      return x
    
if __name__ == "__main__":
  question_text = "What is the best magical creature?"
  question_answers = ["Narwhals", "Unicorns", "Goblins", "Dragons"]
  correct_answer = "Dragons"
  points = 20
  question1 = Question(question_text, question_answers, correct_answer, points)
  print(question1)     
