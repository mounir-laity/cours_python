def opti_bubble_sort(my_list):
    sorted = False
    for i in range(len(my_list) - 1, 0, -1):
        sorted = True
        for j in range(i):
            if my_list[j + 1] < my_list[j]:
                my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
                sorted = False
        if sorted:
            return


from random import randint
from time import time  # Pas obligatoire, je l'utilise pour timer

my_list = [
    randint(-50, 50) for i in range(20)
]  # génération de nombres aléatoires pour tester
print("Avant le tri :", my_list)
start_time = time()
opti_bubble_sort(my_list)
end_time = time()
total_time = end_time - start_time
print("Après le tri :", my_list)
print(f"Le tri a pris {total_time} secondes !")
