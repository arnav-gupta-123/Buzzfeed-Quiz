from quiz import Quiz
from question import Question
from result import Result

class Quiz_App:
    def __init__(self, quiz_title):
        self.quiz_title = quiz_title
        self.questions_list = []
        self.result_list = []
    
    def load_quiz(self):
      question_file = open("questions.txt", "r")
      i = 0
      reading_questions = question_file.readlines()
      while i < len(reading_questions):
        questions = reading_questions[i]
        answer_choices = reading_questions[i+1].strip("\n")
        answer_choices = answer_choices.split(",")
        correct_answer = reading_questions[i+2].strip("\n")
        point_value = reading_questions[i+3]
        question_object = Question(questions, answer_choices, correct_answer, point_value)
        i = i + 4
        self.questions_list.append(question_object)
      question_file.close()
      
      results_file = open("result.txt","r")
      j = 0
      reading_results = results_file.readlines()
      while j < len(reading_results):
        result_sentences = reading_results[j].strip('\n')
        points_scored = reading_results[j+1].strip('\n')
        result_object = Result(result_sentences, points_scored)
        j = j + 2
        self.result_list.append(result_object)
      results_file.close()
      
    def display_result(self):
      return NotImplementedError
    
    def main(self):
      new_quiz = Quiz(self.quiz_title, self.questions_list, self.result_list)
      new_quiz.main()

if __name__ == "__main__":
  quiz_name = "Which Starwars Character Are You?"
  app = Quiz_App(quiz_name)
  app.load_quiz()
  app.main()
