def dict_carres(number):
    carres = {}
    for i in range(1, number + 1):
        carres[i] = i * i
    return carres


print(dict_carres(7))
