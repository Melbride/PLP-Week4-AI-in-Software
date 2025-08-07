# Manual implementation of sorting a list of dictionaries by 'age'
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)
