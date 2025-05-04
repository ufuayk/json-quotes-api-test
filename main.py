from flask import Flask, jsonify
import csv
import random

app = Flask(__name__)

def load_quotes(filename='quotes.csv'):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

quotes = load_quotes()

@app.route('/quote', methods=['GET'])
def get_quote():
    selected = random.choice(quotes)
    return jsonify(selected)

if __name__ == '__main__':
    app.run(debug=True)