from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# /mystery1 - reverse a string
@app.route('/mystery1', methods=['POST'])
def mimic_mystery1():
    data = request.json
    text = data.get("text", "")
    reversed_text = text[::-1]
    return jsonify({"reversed": reversed_text})

# /mystery2 - square a number
@app.route('/mystery2', methods=['POST'])
def mimic_mystery2():
    data = request.json
    number = data.get("number", 0)
    return jsonify({"square": number * number})

# /data - Base64 encode a string (matches blackbox /data)
@app.route('/data', methods=['POST'])
def mimic_data():
    data = request.json.get("data", "")
    encoded = base64.b64encode(data.encode()).decode()
    return jsonify({"result": encoded})

if __name__ == '__main__':
    app.run(debug=True)
