import random

from domanda import Domanda


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
