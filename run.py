import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self, _):
        print(self.question)
        for option in self.options:
            print(option)
        
        user_answer = input("\nYour answer: ").upper()
        return user_answer == self.answer

# ... (rest of the code)



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

# Function to play the quiz
def play_quiz(difficulty, username):
    questions_list = questions[difficulty]
    random.shuffle(questions_list)  # Randomize the order of questions
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
    print(f"Quiz completed, {username}! Your score: {score}/{len(questions_list)}")

# Main game loop
def main():
    ascii_art = (
        r" ______   _______ _    _ _   _  _____ " "\n"
        r"|  ____| |__   __| |  | | \ | |/ ____|" "\n"
        r"| |__       | |  | |  | |  \| | (___  " "\n"
        r"|  __|      | |  | |  | | . ` |\___ \ " "\n"
        r"| |____     | |  | |__| | |\  |____) |" "\n"
        r"|______|    |_|   \____/|_| \_|_____/ " "\n"
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
