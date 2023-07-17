import json

banned_words = []

with open('cenz.txt') as r:
    for line_r in r:
        word = line_r.lower().split('\n')[0]
        if word !='':
            banned_words.append(word)

with open('cenz.json', 'w') as e:
    json.dump(banned_words, e)



