def remove_duplicates(my_list):
    already_seen = []
    for element in my_list:
        if element in already_seen:
            pass
        else:
            already_seen.append(element)
    return already_seen


# Ou, plus simplement :
# def remove_duplicates(my_list):
#     return list(set(my_list))


my_list = [1, 3, 5, "oui", 5, "non", 4, 2, 3, "oui", "Non"]
print(remove_duplicates(my_list))
