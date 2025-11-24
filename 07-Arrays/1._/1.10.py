###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answer = 0
incorrect_answer = 0
for answer in test_results:
    if answer == True:
      correct_answer+=1
    else:
      incorrect_answer+=1

# calculates the number of incorrect answers
...

# calculates the percentage of correct answers
...

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answer)
print('Number of incorrect answers:', incorrect_answer)
print('Percentage of correct answers:', (incorrect_answer/question_number)*100,"%")

...
...