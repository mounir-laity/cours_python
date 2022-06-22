results = {"Bao": 15, "Shams": 13, "Mounir": 0, "Nacera": 8, "Sebastien": 17}
failed = {}
passed = {}
for key in results:
    if results[key] < 10:
        failed[key] = results[key]
    else:
        passed[key] = results[key]

print("The students that have failed are", failed)
print("The students that have passed are", passed)
