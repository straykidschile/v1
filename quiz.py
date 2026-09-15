#!/usr/bin/env python3
"""Quiz interactivo sobre los integrantes de Stray Kids.

Ejecuta: python3 quiz.py
"""
import random
import argparse
from questions import QUESTIONS


def normalize(s: str) -> str:
    return ''.join(ch for ch in s.lower() if ch.isalnum())


def is_correct(user_input: str, aliases: list) -> bool:
    nu = normalize(user_input)
    for a in aliases:
        if nu == normalize(a):
            return True
    return False


def run_quiz(num_questions: int = None, shuffle: bool = True):
    qs = QUESTIONS.copy()
    if shuffle:
        random.shuffle(qs)
    if num_questions is None:
        num_questions = len(qs)
    num_questions = min(num_questions, len(qs))

    score = 0
    asked = 0
    print("Quiz de Stray Kids — escribe 'salir' para terminar. Responde con el nombre del integrante.")
    print(f"Se harán hasta {num_questions} preguntas. ¡Suerte!\n")

    for q in qs[:num_questions]:
        asked += 1
        print(f"Pregunta {asked}: {q['question']}")
        ans = input("Respuesta: ").strip()
        if ans.lower() in ('salir', 'exit', 'quit'):
            print("Saliendo del quiz...\n")
            break
        if is_correct(ans, q.get('aliases', [q['answer']])):
            print("✅ Correcto!\n")
            score += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta: {q['answer']}\n")

    print("--- Resultado ---")
    print(f"Preguntas respondidas: {asked}")
    print(f"Aciertos: {score}")
    if asked:
        pct = score / asked * 100
        print(f"Precisión: {pct:.1f}%")


def main():
    parser = argparse.ArgumentParser(description='Quiz sobre Stray Kids')
    parser.add_argument('--n', type=int, default=None, help='Número de preguntas a realizar')
    parser.add_argument('--no-shuffle', dest='shuffle', action='store_false', help='No mezclar preguntas')
    args = parser.parse_args()

    run_quiz(num_questions=args.n, shuffle=args.shuffle)


if __name__ == '__main__':
    main()
