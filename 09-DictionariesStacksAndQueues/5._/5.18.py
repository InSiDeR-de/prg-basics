import json

# Open the JSON file in read mode
with open('dogs.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)

# Print the JSON data
for dogs in data:
    if dogs['age']<5:
        for key , value in dogs.items():
            print(key,':',value)
        print()