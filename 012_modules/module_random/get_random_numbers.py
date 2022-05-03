import random


def get_random_numbers(amount):
    my_list = [i for i in range(1, 101)]
    results = []
    for i in range(amount):
        random_number = random.choice(my_list)
        while random_number in results:
            random_number = random.choice(my_list)
        results.append(random_number)
    return results


print(get_random_numbers(4))
