import random
class Domanda:
    def __init__(self, testo, punteggio, risposta_corretta, risposta_2, risposta_3_, risposta_4):
        self.testo = testo
        self.punteggio = punteggio
        self.risposta_corretta = risposta_corretta
        self.risposta_2 = risposta_2
        self.risposta_3 = risposta_3_
        self.risposta_4 = risposta_4


def display_question(question):
    print("\nQuestion:", question.text)
    print("Difficulty Level:", question.difficulty)
    print("\nOptions:")
    all_answers = [question.risposta_corretta] + [question.risposta_2] + [question.risposta_3] + [question.risposta_4]
    random.shuffle(all_answers)
    for i, answer in enumerate(all_answers, start=1):
        print(f"{i}. {answer}")
    return all_answers.index(question.correct_answer) + 1


def read_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            testo = lines[i].strip()
            punteggio = int(lines[i + 1].strip())
            risposta_corretta = lines[i + 2].strip()
            risposta_2 = lines[i+3].strip()
            risposta_3 = lines[i + 4].strip()
            risposta_4 = lines[i + 5].strip()
            question = Domanda(testo, punteggio, risposta_corretta, risposta_2, risposta_3, risposta_4)
            questions.append(question)
            # Skip the blank line (if present)
            i += 7 if i + 7 < len(lines) and lines[i + 6].strip() == '' else 6
    return questions


# Example usage:
file_path = 'domande.txt'
all_questions = read_questions_from_file(file_path)

print("Question Text:", all_questions[0].testo)
print("Difficulty Level:", all_questions[0].punteggio)
print("Correct Answer:", all_questions[0].risposta_corretta)
print("Incorrect Answers:", all_questions[0].risposta_2)
print("Incorrect Answers:", all_questions[0].risposta_3)
print("Incorrect Answers:", all_questions[0].risposta_4)

