import json

data = {
    "data1":
        {
            "age": 20,
            "phone": "+73539215818",
            "name": "Anna",
            "city": "Moscow"
        },
    "data2":
        {
            "age": 19,
            "phone": "+73539215818",
            "name": "Nika",
            "city": "Vienna"
        },
    "data3":
        {
            "age": 40,
            "phone": "+73539215818",
            "name": "Nikolay",
            "city": "Moscow"
        },
    "data4":
        {
            "age": 42,
            "phone": "+73539215818",
            "name": "Sasha",
            "city": "Dubai"
        }
}

with open("people.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
    print("JSON-файл успешно создан!")

with open("people.json", "r", encoding="utf-8") as file:
    people = json.load(file)

people_from_msk = []
for key, person in people.items():
    if person['city'] == "Moscow":
        people_from_msk.append(person)

ages = [person['age'] for person in people_from_msk]
average_age = sum(ages) / len(ages) if ages else 0

if average_age == int(average_age):
    average_age = int(average_age)

print('Люди, живущие в Москве:')
for person in people_from_msk:
    print(f"Имя: {person['name']}, Возраст: {person['age']}")

print(f"Средний возраст людей из Москвы: {average_age}")
