def get_special_str(my_list):
    special_list = []
    for element in my_list:
        for char in element:
            if not char.isalnum():
                special_list.append(element)
                break
    return special_list


my_list = ["Mounir", "Un mot", "Salut", "Aujourd'hui", "Enlevez-moi !"]
print(get_special_str(my_list))
