car = {"brand": "VW", "color": "red", "max speed": 180}

# A
for value in car.values():
    print(value)
# B
car["number of wheels"] = 4
print(car)
# C
for key in car:
    print(f"Ma clé {key} a la valeur {car[key]}")

# D
def has_key(my_dict, key):
    return key in my_dict


print(has_key(car, "test"))
print(has_key(car, "number of wheels"))

# E
def has_value(my_dict, value):
    return value in my_dict.values()


print(has_value(car, 12))
print(has_value(car, "VW"))
