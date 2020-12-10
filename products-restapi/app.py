from flask import Flask, jsonify
from product import products 


app = Flask(__name__)



@app.route('/ping')
def ping():
    return jsonify({"message":'pong !'})

if __name__=='__mail__':
    app.run(debug=True, port =4000)