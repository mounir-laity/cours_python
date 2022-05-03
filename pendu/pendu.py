from random import randint


def get_random_word():
    chosen_word = None
    with open("mots.txt", "r") as file:
        num_lines = sum(1 for line in file)
        chosen_index = randint(1, num_lines)
    with open("mots.txt", "r") as file:
        for index, word in enumerate(file):
            if index == chosen_index:
                chosen_word = word.strip()
    return chosen_word


def propose_letter(letter, word, propositions):
    positions = []
    if letter in propositions:
        return None
    for i in range(len(word)):
        if letter.upper() == word[i].upper():
            positions.append(i)
    return positions


def get_potence():
    potence = []
    with open("pendu.txt", "r") as file:
        element = ""
        for line in file:
            if line != "!\n":
                element += line
            else:
                potence.append(element)
                element = ""
    return potence


def list_equal_str(my_list, word):
    if my_list is None or word is None or len(my_list) != len(word):
        return False
    for i in range(len(my_list)):
        if my_list[i].lower() != word[i].lower():
            return False
    return True


if __name__ == "__main__":
    potence = get_potence()
    potence_index = 0
    tries = len(potence) - 1
    word_to_find = get_random_word()
    discovered = ["_" for i in range(len(word_to_find))]
    print(f"Le mot à trouver contient {len(word_to_find)} lettres")
    propositions = []
    while tries > 0:
        print(potence[potence_index])
        for letter in discovered:
            print(letter, end=" ")
        print()
        print("Lettres proposées : ", end=" ") if len(propositions) > 0 else print(
            "", end=" "
        )
        for letter in propositions:
            print(letter, end=", ")
        letter = input("Entrez une lettre : ")
        if not len(letter) == 1 or not letter.isalpha():
            print("Entrez une seule lettre !")
        else:
            positions = propose_letter(letter, word_to_find, propositions)
            if positions is None:
                continue
            elif len(positions) == 0:
                potence_index += 1
                tries -= 1
            else:
                for position in positions:
                    discovered[position] = letter
                if list_equal_str(discovered, word_to_find):
                    print(f"BRAVO !, Le mot est bien {word_to_find}")
                    input("Appuyez sur entrée pour quitter...")
                    exit()
            propositions.append(letter)
    print(potence[-1])
    print("GAME OVER ! Le mot était", word_to_find)
    input("Appuyez sur entrée pour quitter...")
