#!/usr/bin/env python3

# Stray Kids Quiz Console App
# Cada pregunta tiene como respuesta a uno de los integrantes

import random
import sys

def main():
    questions = [
        ("¿A quién identifica el peluche de conejo con nariz de chanco?", "Changbin"),
        ("¿Quién es conocido por su personaje 'Wolf Chan'?", "Bang Chan"),
        ("¿Qué integrante es famoso por su personaje 'Skzoo BbokAri'?", "Felix"),
        ("¿Quién es reconocido por su energía hiperactiva y risa icónica?", "Lee Know"),
        ("¿Qué integrante suele ser llamado 'Sunshine' por su personalidad brillante?", "Han"),
        ("¿Quién es el maknae del grupo?", "I.N"),
        ("¿Qué integrante es conocido por cocinar muy bien en los contenidos del grupo?", "Seungmin"),
        ("¿Quién forma parte del trío de productores 3RACHA junto a Chan y Changbin?", "Han"),
        ("¿Qué integrante ama especialmente los gatos y tiene varios en casa?", "Lee Know"),
        ("¿Quién es famoso por decir 'hey, yo! it's Felix'?", "Felix"),
        ("¿Qué integrante tiene una voz profunda y muy reconocida?", "Felix"),
        ("¿Quién suele ser llamado 'Dwaekki' por sus fans?", "Changbin"),
        ("¿Qué integrante tiene el personaje 'PuppyM' en Skzoo?", "Seungmin"),
        ("¿Quién es el líder de Stray Kids?", "Bang Chan"),
        ("¿Qué integrante tiene un lunar debajo del ojo?", "Hyunjin"),
        ("¿Quién es conocido por su disciplina y constancia?", "Seungmin"),
        ("¿Qué integrante suele cantar baladas con mucha emoción?", "I.N"),
        ("¿Quién tiene un gran talento para el rap y forma parte de 3RACHA?", "Changbin"),
        ("¿Qué integrante es conocido por su dulzura y amabilidad con STAY?", "Han"),
        ("¿Quién suele hablar inglés con acento australiano?", "Bang Chan"),

        # Nuevas 20 preguntas
        ("¿Qué integrante es conocido por su personaje Skzoo llamado 'Leebit'?", "Lee Know"),
        ("¿Quién es famoso por sus pecas naturales?", "Felix"),
        ("¿Qué integrante suele tocar guitarra en los lives nocturnos?", "Bang Chan"),
        ("¿Quién tiene el apodo 'Squirrel' por su energía?", "Han"),
        ("¿Qué integrante es extremadamente ordenado y organizado?", "Seungmin"),
        ("¿Quién es famoso por su high note en varias canciones?", "I.N"),
        ("¿Qué integrante suele decir 'Skz world domination'?", "Bang Chan"),
        ("¿Quién practica taekwondo y tiene cinturón negro?", "Lee Know"),
        ("¿Qué integrante es muy versátil en rap, vocal y producción?", "Han"),
        ("¿Quién tiene el personaje Skzoo 'Jiniret'?", "I.N"),
        ("¿Qué integrante tiene el apodo 'Binnie'?", "Changbin"),
        ("¿Quién es muy cercano a los fans en Bubble?", "Seungmin"),
        ("¿Qué integrante tiene un tono de voz naturalmente dulce?", "Han"),
        ("¿Quién es conocido por su humor sarcástico?", "Lee Know"),
        ("¿Qué integrante hace 'food reviews' y ama la comida?", "Felix"),
        ("¿Quién fue aprendiz por más de 7 años antes de debutar?", "Bang Chan"),
        ("¿Qué integrante es considerado de los más fuertes físicamente?", "Changbin"),
        ("¿Quién suele hablar muy rápido cuando se emociona?", "Han"),
        ("¿Qué integrante suele ser tímido pero muy cálido al conocerlo?", "I.N"),
        ("¿Quién tiene una de las sonrisas más luminosas del grupo?", "Felix"),
    ]

    random.shuffle(questions)

    score = 0
    total = len(questions)

    print("\nBienvenido al Quiz de Stray Kids!\nResponde con el nombre del integrante.\n")

    for i, (q, ans) in enumerate(questions, start=1):
        print(f"Pregunta {i}/{total}:")
        print(q)
        user = input("> ").strip()

        if user.lower() == ans.lower():
            print("✔ Correcto!\n")
            score += 1
        else:
            print(f"✘ Incorrecto. La respuesta era: {ans}\n")

    print(f"Tu puntaje final es: {score}/{total}")


if __name__ == "__main__":
    main()
