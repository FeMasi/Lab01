import random

class Question:
    def __init__(self, text, difficulty, correct_answer, incorrect_answers):
        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers

def read_questions_from_file(file_path):
    all_q = []
    with open(file_path, 'r') as file:
        j = 1
        lines = file.readlines()
        difficolta = 0
        while j < len(lines):
            if difficolta < lines[j].strip():
                difficolta = lines[j].strip()
            j += 7 if j + 7 < len(lines) and lines[j + 6].strip() == '' else 6

    for i in range (difficolta):
        all_q[i] = []

    questions_0 = []
    questions_1 = []
    questions_2 = []
    questions_3 = []
    questions_4 = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0



        while i < len(lines):
            text = lines[i].strip()
            difficulty = int(lines[i + 1].strip())
            correct_answer = lines[i + 2].strip()
            incorrect_answers = [lines[j].strip() for j in range(i + 3, i + 6)]
            question = Question(text, difficulty, correct_answer, incorrect_answers)
            all_q[question.difficulty].append(question)
            # provare a rimuovere i successivi if, in teoria all_q è una lista di liste con all'interno le domande, così funziona anche con file con difficoltà superiore a 4
            if question.difficulty == 0:
                questions_0.append(question)
            elif question.difficulty == 1:
                 questions_1.append(question)
            elif question.difficulty == 2:
                questions_2.append(question)
            elif question.difficulty == 3:
                questions_3.append(question)
            elif question.difficulty == 4:
                questions_4.append(question)

            # Skip the blank line (if present)
            i += 7 if i + 7 < len(lines) and lines[i + 6].strip() == '' else 6
    all_q.append(questions_0)
    all_q.append(questions_1)
    all_q.append(questions_2)
    all_q.append(questions_3)
    all_q.append(questions_4)
    return all_q

# Example usage:
file_path = 'domande.txt'
all_q = read_questions_from_file(file_path)
all_questions_0 = read_questions_from_file(file_path)[0]
all_questions_1 = read_questions_from_file(file_path)[1]
all_questions_2 = read_questions_from_file(file_path)[2]
all_questions_3 = read_questions_from_file(file_path)[3]
all_questions_4 = read_questions_from_file(file_path)[4]

# Accessing the properties of the first question:
print("Question Text:", all_questions_0[0].text)
print("Difficulty Level:", all_questions_0[0].difficulty)
print("Correct Answer:", all_questions_0[0].correct_answer)
print("Incorrect Answers:", all_questions_0[0].incorrect_answers)

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
    punteggio = 0
    file_path = 'domande.txt'
    all_questions = read_questions_from_file(file_path)
    livello_difficolta = 0
    while True:
        if livello_difficolta > 4:
            print("Hai vinto")
            break


        random_question = random.choice(all_questions[livello_difficolta])
        chosen_option = display_question(random_question)

        try:
            player_choice = int(input("\nEnter your choice (1-4): "))
            if 1 <= player_choice <= 4:
                if player_choice == chosen_option:
                    print("Correct! 🎉")
                    livello_difficolta += 1
                    punteggio += 1
                    continue
                else:
                    print(f"Sorry, the correct answer was option {chosen_option}.")
                    livello_difficolta = 0
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() != 'y':
            break

    f = open("punti.txt", "w")
    nome = input("inserisci il tuo nome")


if __name__ == "__main__":
    main()