from flask import Flask
from flask import request
import qbank
import json

QUESTION = 'question'
ACTION = 'action'
SUGGESTION = 'suggestion'
NEW = 'new'

host = '0.0.0.0'
portNumber = 12223
app = Flask(__name__)

@app.route('/<key>', methods=['GET'])
def keyGet(key):
    return _serverAllQuestions(key)

@app.route('/<key>', methods=['POST'])
def keyPost(key):
    question = request.form.get(QUESTION)
    action = request.form.get(ACTION)
    if action == SUGGESTION:
        qli = qbank.getSuggestions(key, question);
        return json.dumps(qli)
    elif action == NEW:
        qbank.append(key, question)
        return _serverAllQuestions(key)

@app.route('/<key>', methods=['PUT'])
def keyUpdate(key):
    question = request.form.get(QUESTION)
    qbank.setOccurance(key, question)
    return _serverAllQuestions(key)


@app.route('/<key>', methods=['DELETE'])
def keyDel(key):
    question = request.form.get(QUESTION)
    qbank.delete(key, question)
    return _serverAllQuestions(key)


def _serverAllQuestions(key):
    return json.dumps(qbank.getQuestions(key))

if __name__ == '__main__':
    app.run(host=host, port=portNumber, threaded=False)
