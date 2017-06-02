from flask import Flask

host = '0.0.0.0'
portNumber = 12223
app = Flash(__name__)

@app.route('/<key>', methods=['GET'])
def keyGet(key):
    return _serverAllQuestions(key)

@app.route('/<key>', methods=['POST'])
def keyGet(key):
    return _serverAllQuestions(key)


@app.route('/<key>', methods=['DELETE'])
def keyGet(key):
    return _serverAllQuestions(key)


def _serverAllQuestions(key):
    return json.dumps(getQuestions)

if __name__ == '__main__':
    app.run(host=host, port=portNumber, threaded=True)
