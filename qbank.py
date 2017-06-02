import sqlite3
import json
import qcomp

#dict indices
QUESTION = 'question'
OCCURANCE = 'occurance'

# JSON Schema for the json entries in the DB
#
# [
#   {
#       "text":"Question blah blah"
#       "occurance": 2
#   }
# ]
#
#

class Question:
    def __init__(self, text, occurance):
        self.text = text
        self.occurance = occurance

    def incrOccurance(self, incrBy = 1):
        self.occurance += incrBy

    def decrOccurance(self, decrBy = 1):
        self.occurance -= decrBy

conn = sqlite3.connect('qbanks.sqlite')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS qbank(
        key VARCHAR(20) NOT NULL PRIMARY KEY UNIQUE,
        questions TEXT
    );
''')

def _extractQuestions(qlist):
    qns = []
    for entry in qlist:
        qns.append(entry[QUESTION])
    return qns





#########################################################
############ IMPORTANT!!!!!!!!! #########################
######## POSSIBILITY OF SQL INJECTION ###################
########## WHEREVER "key" is USED #######################
#########################################################
################# VALIDATE HERE #########################

def _fetchQFromDB(key):
    key = key.lower()
    cur.execute('''SELECT questions FROM qbank WHERE key = ?''', (key,) )
    qlist = json.loads(cur.fetchone()[0] )
    return qlist

def _commitQToDB(key, qlist):
    key = key.lower()
    toDump = json.dumps(qlist)
    cur.execute('''UPDATE qbank SET questions = ? WHERE key = ?''', (toDump,key))
    conn.commit()

########################################################
########################################################
########################################################
########################################################


def getSuggestions(key, newQuestion, numSuggestions = 4):
    qlist = _fetchQFromDB(key)
    qns = _extractQuestions(qlist)
    qnsScore = [qcomp.compareStr(newQuestion, q) for q in qns]
    qnsCombined = list(zip(qns, qnsScore))
    qnsCombined = sorted(qnsCombined, key = lambda x: x[1], reverse=True)
    qnsCombined = qnsCombined[:numSuggestions]
    return [q for q,n in qnsCombined]

def getQuestions(key):
    qlist = _fetchQFromDB(key)
    return qlist

def append(key, question):
    key = key.lower()
    qlist = _fetchQFromDB(key)
    qlist.append({QUESTION: question, OCCURANCE:1 })
    _commitQToDB(key, qlist)

def set(key, question, occurance):
    qlist = _fetchQFromDB(key)
    for entry in qlist:
        if entry[QUESTION] == question:
            entry[OCCURANCE] = occurance
    _commitQToDB(key, qlist)

def updateQuestion(key, oldQuestion, newQuestion):
    qlist = _fetchQFromDB(key)
    for entry in qlist:
        if entry[QUESTION] == oldQuestion:
            entry[QUESTION] = newQuestion
            break
    _commitQToDB(key, qlist)

def delete(key, question):
    qlist = _fetchQFromDB(key)

    for i in range(len(qlist)):
        if qlist[i][QUESTION] == question:
            del qlist[i]
            break
    _commitQToDB(key, qlist)
