from flask import Flask, jsonify, render_template, json, request
import couchdb
from flask.ext.cors import CORS

couch = couchdb.Server('http://admin:GameHalt@salmansaleemk.iriscouch.com/')

bookings = couch['bookings']

def all_docs(database_name):
    docs = []
    for id in database_name:
        docs.append(database_name[id])
    return docs
    
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/bookings', methods=['GET'])
def bookings_all():
    return jsonify({'bookings':all_docs(bookings)})
    
@app.route('/bookings/<doc_id>', methods=['GET'])
def bookings_doc(doc_id):
    return jsonify({ 'booking' :bookings[doc_id]})
    
@app.route('/bookings', methods=['POST'])
def create_bookings():
    
    newdoc = {
        'charges': request.json['booking']['charges'],
        'name':request.json['booking']['name'],
        'from':request.json['booking']['from'],
        'purpose':request.json['booking']['purpose'],
        'requiredkms':request.json['booking']['requiredkms'],
        'time':request.json['booking']['time'],
        'to':request.json['booking']['to']
        }
    bookings.save(newdoc)
    return jsonify({'booking': newdoc}), 201


if __name__ == '__main__':
    app.run(debug=True)
    