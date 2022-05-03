from random import choice


def select_random_char(my_str):
    try:
        return choice(my_str)
    except IndexError:  # IndexError si la chaîne est vide
        return ""


phrase = "Salut à tous, ceci est un exercice !"
print(select_random_char(phrase))
