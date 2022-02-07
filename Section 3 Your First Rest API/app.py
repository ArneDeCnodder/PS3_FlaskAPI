from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

# temp data
stores = [
    {
        'name': 'Carrefour',
        'items': [
            {
                'name':'Kaas', 
                'price': 1.99 
            },
            {
                'name':'Brood', 
                'price': 2.20 
            },
            {
                'name':'Ham', 
                'price': 4.79 
            },
            {
                'name':'Boter', 
                'price': 2.56 
            },
        ]
    }
]

@app.route('/')
def home():
  return render_template('index.html')

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)
  

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': f'store with the name {name} not found'})
  

#get /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})
  

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message': f'store with the name {name} not found'})
  

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message': f'store with the name {name} not found'})

app.run(port=5000)