import random

class Question:
    """
    Represents a quiz question with its options and correct answer.
    """

    def __init__(self, question, options, answer):
        """
        Initializes a Question instance.

        Args:
            question (str): The question text.
            options (list of str): List of answer options.
            answer (str): The correct answer.
        """
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self, _):
        """
        Asks the question, displays options, takes user's answer, and checks if it's correct.

        Args:
            _ (int): Not used.

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        print(self.question)
        for option in self.options:
            print(option)
        user_answer = input("\nYour answer: ").upper()
        return user_answer == self.answer.upper()  # Convert both answers to uppercase

# Define the questions and answers
questions = {
    "easy": [
        Question("What is the capital of France?",
                 ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
                 "A"),
        Question("Which planet is known as the Red Planet?",
                 ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                 "B"),
        # Add more questions...
    ],
    "hard": [
        Question("In which year was the Python programming language first released?",
                 ["A) 1989", "B) 1991", "C) 2000", "D) 2005"],
                 "B"),
        Question("What is the largest mammal?",
                 ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Lion"],
                 "C"),
        # Add more questions...
    ]
}

def play_quiz(difficulty, username):
    """
    Plays the quiz game.

    Args:
        difficulty (str): Difficulty level of the quiz.
        username (str): User's username.
    """
    questions_list = questions[difficulty]
    random.shuffle(questions_list)  # Randomize the order of questions
    score = 0

    for question in questions_list:
        print("\n" + "="*30)
        print(f"Question: {questions_list.index(question) + 1}")
        if question.ask(None):  # No time limit
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\n" + "="*30)
    print(f"Quiz completed, {username}! Your score: {score}/{len(questions_list)}")

def main():
    """
    Main game loop to run the quiz game.
    """
    ascii_art = (
    )
    print(ascii_art)
    print("Welcome to the Quiz Game!")

    username = input("Enter your username: ")

    while True:
        print("\nSelect difficulty:")
        print("1. Easy")
        print("2. Hard")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            play_quiz("easy", username)
        elif choice == "2":
            play_quiz("hard", username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
