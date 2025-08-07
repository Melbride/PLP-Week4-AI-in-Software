people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)
