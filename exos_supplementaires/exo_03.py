def reverse_num(number):
    number_str = str(number)
    reversed_number = ""
    for i in range(len(number_str) - 1, -1, -1):
        reversed_number += number_str[i]
    return reversed_number


print(reverse_num(6321569))
