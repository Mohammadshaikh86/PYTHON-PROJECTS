import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return answer.lower() == self.correct_answer.lower()

    def display(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

questions = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
    Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
    Question("Who painted the Mona Lisa?", ["Van Gogh", "Da Vinci", "Picasso", "Rembrandt"], "Da Vinci"),
    Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
    Question("In which year did World War II end?", ["1943", "1944", "1945", "1946"], "1945"),
]

def run_quiz(questions, num_questions=5):
    score = 0
    random.shuffle(questions)
    selected_questions = questions[:num_questions]

    for i, question in enumerate(selected_questions, start=1):
        print(f"\nQuestion {i}:")
        question.display()
        
        while True:
            user_answer = input("Enter your answer (1-4): ")
            if user_answer in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        
        selected_answer = question.options[int(user_answer) - 1]
        
        if question.is_correct(selected_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {question.correct_answer}")

    print(f"\nQuiz completed! Your score: {score}/{num_questions}")
    percentage = (score / num_questions) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Perfect score! Excellent job!")
    elif percentage >= 80:
        print("Great job! You did very well.")
    elif percentage >= 60:
        print("Good effort! Keep practicing to improve.")
    else:
        print("You might want to study a bit more. Don't give up!")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("You'll be asked 5 multiple-choice questions.")
    print("Choose the correct answer by entering the corresponding number.")
    input("Press Enter to start the quiz...")
    
    run_quiz(questions)
