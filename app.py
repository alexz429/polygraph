from flask import Flask, request, jsonify
from src.textual_entailment import TextualEntailment

app = Flask(__name__)
t = TextualEntailment()

@app.route('/')
def hello_word():
    return 'first api call'

@app.route('/analyze', methods=["GET"])
def testpost():
    input_json = request.get_json(force=True)
    result = t.run(input_json['premise'], input_json['hypothesis'])
    dictToReturn = {'is_factual':result}
    return jsonify(dictToReturn)