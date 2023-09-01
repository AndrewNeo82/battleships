import random
import time

class Question:
    """
    Represents a quiz question.

    Args:
        question (str): The question text.
        options (list): A list of options for the question.
        answer (str): The correct answer to the question.

    Attributes:
        question (str): The question text.
        options (list): A list of options for the question.
        answer (str): The correct answer to the question.
    """
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def ask(self, timeout=60):
        """
        Ask the question and collect the user's answer within a specified timeout.

        Args:
            timeout (int, optional): The time limit in seconds to answer the question. Default is 60 seconds.

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        print(self.question)
        for option in self.options:
            print(option)

        user_answer = input("Your answer: ").upper()
        return user_answer == self.answer

questions = {
    "easy": [
        Question("What is the capital of France?",
                 ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
                 "A"),
        Question("Which planet is known as the Red Planet?",
                 ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                 "B"),
        Question("Who painted the Mona Lisa?",
                 ["A) Vincent van Gogh", "B) Leonardo da Vinci", "C) Pablo Picasso", "D) Michelangelo"],
                 "B"),
        Question("What is the largest mammal in the world?",
                 ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Lion"],
                 "B"),
        Question("Which gas do plants primarily use for photosynthesis?",
                 ["A) Oxygen", "B) Nitrogen", "C) Hydrogen", "D) Carbon Dioxide"],
                 "D"),
        Question("What is the capital of Japan",
                 ["A) Beijing", "B) Tokyo", "C) Seoul", "D) Bangkok"],
                 "B"),
        Question("Which famous scientist developed the theory of relativity?",
                 ["A) Isaac Newton", "B) Galileo", "C) Einstein", "D) Stephen Hawking"],
                 "C"),
        Question("Which ocean is the largest on Earth?",
                 ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
                 "C"),
        Question("What is the main function of the heart?",
                 ["A) Pump Blood", "B) Digestion", "C) Produce Hormones", "D) Filtering waste"],
                 "A"),
        Question("What is the process by which plants make their own food using sunlight?",
                 ["A) Respiration", "B) Transpiration", "C) Photosynthesis", "D) Combustion"],
                 "C"),
    ],
    "hard": [
        Question("In which year was the Python programming language first released?",
                 ["A) 1989", "B) 1991", "C) 2000", "D) 2005"],
                 "B"),
        Question("What is the smallest prime number?",
                 ["A) 0", "B) 1", "C)2", "D)3"],
                 "C"),
        Question("Which philosopher is known for his work Critique of Pure Reason?",
                 ["A) Friedrich Nietzsche", "B) Immanuel Kant", "C) Søren Kierkegaard", "D) Jean-Jacques Rousseau"],
                 "B"),
        Question("What is the largest species of shark?",
                 ["A) Great White", "B) Hammerhead Shark", "C) Whale Shark", "D) Tiger Shark"],
                 "A"),
        Question("In which year did the Berlin Wall fall, leading to the reunification of Germany?",
                 ["A) 1985", "B) 1989", "C) 1991", "D) 1995"],
                 "B"),
        Question("Which novel features the characters Winston Smith and Big Brother?",
                 ["A)Brave New World ", "B)1984 ", "C) Farenheit 451", "D) The Giver"],
                 "B"),
        Question("What is the rarest blood type among humans?",
                 ["A) A", "B)B ", "C)AB ", "D) O Negative"],
                 "D"),
        Question("Which artist painted The Persistence of Memory, featuring melting clocks?",
                 ["A)Salvador Dali ", "B) Pablo Picasso", "C) Vincent Van Gogh", "D)Leonardo Da Vinci "],
                 "A"),
        Question("What is the largest organ in the human body?",
                 ["A) Liver", "B)Brain ", "C) Skin", "D) Heart"],
                 "C"),
        Question("Which particle is responsible for carrying the electromagnetic force?",
                 ["A) Proton ", "B) Neutron", "C) Electron", "D) Photon"],
                 "D"),
    ]
}

def play_quiz(difficulty, username):
    """
    Plays the quiz. Randomizes the order of the questions and limits the quiz to 5 questions.

    Args:
        difficulty (str): The difficulty level of the quiz ("easy" or "hard").
        username (str): The player's username.
    """
    questions_list = questions[difficulty]
    random.shuffle(questions_list)
    questions_list = questions_list[:5]  # Select 5 random questions
    score = 0

    total_questions = len(questions_list)
    time_limit = 60  # 60 seconds for the entire quiz

    print("\n" + "="*60)
    print(f"Quiz started for {time_limit} seconds...")
    start_time = time.time()

    for question in questions_list:
        print("\n" + "="*60)
        print(f"Question: {questions_list.index(question) + 1}")
        print(f"Time remaining: {time_limit} seconds")

        if question.ask(time_limit):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        elapsed_time = time.time() - start_time
        time_limit -= int(elapsed_time)  # Subtract elapsed time from the time limit

        if time_limit <= 0:
            print("Time's up!")
            break

    print("\n" + "="*60)
    print(f"Quiz completed, {username}! Your score: {score}/{total_questions}")

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
    print("You have 60 seconds to complete the quiz.")

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
