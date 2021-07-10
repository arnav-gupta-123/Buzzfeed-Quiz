from question import Question

class Quiz:
    def __init__(self, title, questions, results):
      self.title = title
      self.questions = questions
      self.results = results
      self.score = 0

    def ask_question(self, index):
      print(self.questions[index])

    def record_answer(self, index):
      user_input = int(input("Enter the number of your response here: "))
      while user_input > len(self.questions[index].answers) or user_input <= 0:
        print()
        print("That response is unacceptable. Please enter a number from 1 to " + str(len(self.questions[index].answers)))
        print()
        user_input = int(input("Enter the number of your response here: "))
      if self.questions[index].correct_answer == self.questions[index].answers[user_input - 1]:
        self.score += self.questions[index].points

    def record_points(self):
      return NotImplementedError

    def calculate_result(self):
      i = 0
      while i < len(self.results) and self.score >= self.results[i].points:
        i += 1
      print()
      print('You got ' + str(self.score) + ' points. ' + str(self.results[i-1]) + ".")
    
    def main(self):
      i = 0
      print(self.title)
      while i < len(self.questions):
        print()
        self.ask_question(i)
        print()
        self.record_answer(i)
        i += 1
      self.calculate_result()
      
if __name__ == "__main__":
  quiz_title = "Do you own a magical menagerie?"

  question_text = "What is the best magical creature?"
  question_answers = ["Narwhals", "Unicorns", "Goblins", "Dragons"]
  correct_answer = "Dragons"
  points = 20
  question1 = Question(question_text, question_answers, correct_answer, points)

  question_text = "What is the best feature of a magical creature?"
  question_answers = ["Fire!", "Hooves", "Flight", "Mesmerizing Eyes"]
  correct_answer = "Hooves"
  points = 13
  question2 = Question(question_text, question_answers, correct_answer, points)

  questions = [question1, question2]
  
  quiz = Quiz(quiz_title, questions, [])
  quiz.main()
  #Call functions to test them using the format above
