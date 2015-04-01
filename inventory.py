from flask import Flask, jsonify, render_template, json
import couchdb

couch = couchdb.Server('http://salmansaleemk:BoostUp@salmansaleemk.iriscouch.com/')
inventory = couch['inventory']
yappdata = couch['yappdata']
bookings = couch['bookings']

def all_docs(database_name):
    docs= []
    for id in database_name:
        docs.append(database_name[id])
    return docs
    
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/inventory', methods=['GET'])
def inventory_all():
    return jsonify({'inventory':all_docs(inventory)})
    
@app.route('/inventory/<doc_id>', methods=['GET'])
def inventory_doc(doc_id):
    return jsonify({ 'inventory':inventory[doc_id]})
    
@app.route('/yappdata', methods=['GET'])
def yappdata_all():
    return jsonify({'yappdata':all_docs(yappdata)})
    
@app.route('/yappdata/<doc_id>', methods=['GET'])
def yappdata_doc(doc_id):
    return jsonify({ 'yappdata':yappdata[doc_id]})
    
@app.route('/bookings', methods=['GET'])
def bookings_all():
    return jsonify({'bookings':all_docs(bookings)})
    
@app.route('/bookings/<doc_id>', methods=['GET'])
def bookings_doc(doc_id):
    return jsonify({ 'booking' :bookings[doc_id]})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8081)