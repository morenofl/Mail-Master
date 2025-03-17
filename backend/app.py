from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['GET'])
def test_connection():
    return jsonify({"message": "Frontend successfully connected to Backend!"})


    
@app.route('/top-emails', methods=['GET'])
def get_top_emails():
    sample_data = {
        "top_emails": [
            {"email": "newsletter@xyz.com", "count": 45},
            {"email": "alerts@bank.com", "count": 30},
            {"email": "promo@store.com", "count": 20}
        ]
    }
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(debug=True)
