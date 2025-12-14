import json
import os

# File to store voting data
voting_file = 'voting.json'

# Read the contents of the json file
if os.path.exists(voting_file):
    with open(voting_file, 'r', encoding='utf-8') as file:
        votes = json.load(file)
else:
    votes = {}

# Vote for a person
person_name = input('Name of the person you are voting for: ')

# Update votes
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save voting data to json file
with open(voting_file, 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent=4, ensure_ascii=False)

print(f"Vote for {person_name} has been recorded!")
print("\nCurrent voting results:")
for name, vote_count in votes.items():
    print(f"{name}: {vote_count}")