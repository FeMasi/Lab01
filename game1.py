import random

class Question:
    def __init__(self, text, difficulty, correct_answer, incorrect_answers):
        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

def read_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            text = lines[i].strip()
            difficulty = int(lines[i + 1].strip())
            correct_answer = lines[i + 2].strip()
            incorrect_answers = [lines[j].strip() for j in range(i + 3, i + 6)]
            question = Question(text, difficulty, correct_answer, incorrect_answers)
            questions.append(question)
            # Skip the blank line (if present)
            i += 7 if i + 7 < len(lines) and lines[i + 6].strip() == '' else 6
    return questions

# Example usage:
file_path = 'domande.txt'
all_questions = read_questions_from_file(file_path)

# Accessing the properties of the first question:
print("Question Text:", all_questions[0].text)
print("Difficulty Level:", all_questions[0].difficulty)
print("Correct Answer:", all_questions[0].correct_answer)
print("Incorrect Answers:", all_questions[0].incorrect_answers)

def display_question(question):
    print("\nQuestion:", question.text)
    print("Difficulty Level:", question.difficulty)
    print("\nOptions:")
    all_answers = [question.correct_answer] + question.incorrect_answers
    random.shuffle(all_answers)
    for i, answer in enumerate(all_answers, start=1):
        print(f"{i}. {answer}")
    return all_answers.index(question.correct_answer) + 1

def main():
    file_path = 'domande.txt'
    all_questions = read_questions_from_file(file_path)

    while True:
        random_question = random.choice(all_questions)
        chosen_option = display_question(random_question)

        try:
            player_choice = int(input("\nEnter your choice (1-4): "))
            if 1 <= player_choice <= 4:
                if player_choice == chosen_option:
                    print("Correct! 🎉")
                else:
                    print(f"Sorry, the correct answer was option {chosen_option}.")
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
