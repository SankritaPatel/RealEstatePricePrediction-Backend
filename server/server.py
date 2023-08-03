from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)


# api_config = {
#     "origins":["https://localhost:5000"]
# }

# CORS(app, resources={
#     r"/*": api_config
# })

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        "locations": util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    #response.header("Access-Control-Allow-Headers", "X-Requested-With");
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft,bath,bhk)
    })
    response.headers.add('Access-Control-Allow-origin','*')
    return response
    

if __name__== "__main__":
    print("Starting Python Flask server For Home Price prediction....")
    util.load_saved_artifacts()
    app.run()