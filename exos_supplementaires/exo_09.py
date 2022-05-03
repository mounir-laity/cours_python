def get_nb_lines(text_file):
    with open(text_file, "r") as file:
        for line_number, line in enumerate(file):
            pass
        return line_number + 1


print(get_nb_lines("test.txt"))
