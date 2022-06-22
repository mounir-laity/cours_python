phrase = input("Entrez une phrase :\n")
occurences = {}
for letter in phrase:
    if letter not in occurences:
        occurences[letter] = 1
    else:
        occurences[letter] += 1
print(occurences)
