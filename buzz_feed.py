import json
import random

path = 'lang_quiz.json'

def ask_question(question):
    print(question['Question'])

    choices = question['Choices']
    values = list(range(len(choices)))

    joined = list(zip(choices, values))
    random.shuffle(joined)
    choices, values = zip(*joined)
    
    for i, c in enumerate(choices, 97):
        print(chr(i) + ') ' + c)
        
    choice = input('> ')

    return values[ord(choice) - 97]

# Go!
with open(path, 'r') as f:
    text = f.read()
    
data = json.loads(text)

categories = data['categories']
questions = data['questions']

scores = [0] * len(categories)

for q in questions:
    category_index = ask_question(q)
    scores[category_index] += 1

max_index = scores.index(max(scores))

print('You are ' + categories[max_index] + '!')
