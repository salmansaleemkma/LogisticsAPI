from flask import Flask, jsonify, request
import couchdb
from flask.ext.cors import CORS

couch = couchdb.Server('https://mseatinewdedezedgdriesev:'
                       'ndg6i5qy8hHYoAfve4fsEdGj@'
                       'inventorybackend.cloudant.com')

bookings = couch['bookings']


def all_docs(database_name):
    docs = []
    for id in database_name:
        docs.append(database_name[id])
    return docs

app = Flask(__name__)
cors = CORS(app)


@app.route('/bookings', methods=['GET'])
def bookings_all():
    return jsonify({'bookings': all_docs(bookings)})


@app.route('/bookings/<doc_id>', methods=['GET'])
def bookings_doc(doc_id):
    return jsonify({'booking': bookings[doc_id]})


@app.route('/bookings', methods=['POST'])
def create_bookings():

    newdoc = {
        'charges':  request.json['booking']['charges'],
        'name':  request.json['booking']['name'],
        'from':  request.json['booking']['from'],
        'purpose':  request.json['booking']['purpose'],
        'requiredkms':  request.json['booking']['requiredkms'],
        'time':  request.json['booking']['time'],
        'to':  request.json['booking']['to']

    }
    bookings.save(newdoc)
    return jsonify({'booking': newdoc}), 201


@app.route('/bookings/<doc_id>', methods=['PUT'])
def update_bookings(doc_id):

    updatedoc = bookings[doc_id]

    updatedoc['charges'] = request.json['booking']['charges']
    updatedoc['name'] = request.json['booking']['name']
    updatedoc['from'] = request.json['booking']['from']
    updatedoc['purpose'] = request.json['booking']['purpose']
    updatedoc['requiredkms'] = request.json['booking']['requiredkms']
    updatedoc['time'] = request.json['booking']['time']
    updatedoc['to'] = request.json['booking']['to']

    bookings[doc_id] = updatedoc
    return jsonify({'booking': bookings[doc_id]})


@app.route('/bookings/<doc_id>', methods=['DELETE'])
def delete_booking(doc_id):

    doc = bookings[doc_id]
    bookings.delete(doc)

    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
