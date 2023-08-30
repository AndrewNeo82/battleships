import time


class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self, time_limit):
        print(self.question)
        for option in self.options:
            print(option)
        start_time = time.time()
        user_answer = input("Your answer: ").upper()
        elapsed_time = time.time() - start_time

        if elapsed_time > time_limit:
            print("Time's up!")
            return False

        return user_answer == self.answer


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
        Question("When was the Python programming language first released?",
                 ["A) 1989", "B) 1991", "C) 2000", "D) 2005"],
                 "B"),
        Question("What is the largest mammal?",
                 ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Lion"],
                 "C"),
        # Add more questions...
    ]
}


# Function to play the quiz
def play_quiz(difficulty, username):
    questions_list = questions[difficulty]
    score = 0

    for question in questions_list:
        print("\n" + "="*30)
        print(f"Question: {questions_list.index(question) + 1}")
        if question.ask(10 if difficulty == "easy" else 5):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\n" + "="*30)
    print(f"Quiz complete,{username}!Your score:{score}/{len(questions_list)}")


# Main game loop
def main():
    ascii_art = r"""
                    88
                        ""
 ,adPPYb,d8 88       88 88 888888888
a8"    `Y88 88       88 88      a8P"
8b       88 88       88 88   ,d8P'
"8a    ,d88 "8a,   ,a88 88 ,d8"
 `"YbbdP'88  `"YbbdP'Y8 88 888888888
         88
         88
    """
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
