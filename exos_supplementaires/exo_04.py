import string
from random import choice


def generate_letters(amount):
    if amount < 0:
        raise ValueError("Vous ne pouvez pas générer un nombre négatif de lettres !")
    list_letters = list(string.ascii_letters)
    letters_generated = ""
    for i in range(amount):
        letters_generated += choice(list_letters)
    return letters_generated


print(generate_letters(4))
