from random import shuffle, randint
from time import time  # Pas obligatoire, je l'utilise pour timer


def stupid_sort(my_list: list):
    while not is_sorted(my_list):
        shuffle(my_list)


def is_sorted(my_list):
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            return False
    return True


numbers = [randint(-50, 50) for i in range(10)]
print("Avant le tri :", numbers)
start_time = time()
stupid_sort(numbers)
end_time = time()
total_time = end_time - start_time
print("Après le tri :", numbers)
print(f"Le tri a pris {total_time:.2f} secondes !")
