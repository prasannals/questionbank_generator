QUESTION = 'question'
OCCURANCE = 'occurance'

qlist = []

fname = input('Enter filename : ')
print()

while True:
    question = input('Enter question : ')
    if(question == 'quit' ):
        break
    try:
        occ = int(input('Enter occurance : '))
    except:
        print('Not an int. Exiting')
        break
    qlist.append({QUESTION: question, OCCURANCE: occ})

import json
toDump = json.dumps(qlist)

with open(fname, 'w') as f:
    f.write(toDump)
