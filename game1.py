import random
import fileinput


class Question:

    def __init__(self, text, difficulty, correct_answer, incorrect_answers):
        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers


def read_questions_from_file(file_path):

    with open(file_path, 'r') as file:
        j = 1
        lines = file.readlines()
        difficolta = 0
        while j < len(lines):
            x = int(lines[j].strip())
            if difficolta <= x:
                difficolta = int(lines[j].strip())

            j += 8 if j + 8 < len(lines) and lines[j + 6].strip() == '' else 7


    all_q = [[] for i in range(0, difficolta+1)]


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


            # Skip the blank line (if present)
            i += 7 if i + 7 < len(lines) and lines[i + 6].strip() == '' else 6

    return all_q

# Example usage:
file_path = 'domande.txt'

all_q = read_questions_from_file(file_path)


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
            nome = input("inserisci il tuo nome")

            processing_foo1s = False
    # da vedere
            for line in fileinput.input('punti.txt', inplace=1):
                if line.endswith(str(punteggio)):
                    processing_foo1s = True
                    print(nome + ' ' + str(punteggio)),
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



if __name__ == "__main__":
    main()