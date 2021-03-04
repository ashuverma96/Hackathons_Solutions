from flask import Flask, jsonify

from flask import Flask
app = Flask(__name__)

@app.route('/find_symbols_in_names', methods=['Post'])

def match_symbol():
    chemicals = ['Amazon', 'Microsoft', 'Google']
    symbols = ['I', 'Am', 'cro', 'Na', 'le', 'abc']
    import re
    combined = []

    for s in symbols:
        for c in chemicals:
            r = re.search(s, c)
            if r:
                combined.append(re.sub(s, "[{}]".format(s), c))

    return jsonify({"result" : combined})

if __name__ == "__main__":
    app.run(debug=True)
