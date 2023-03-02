from flask import Flask, request
from flask_cors import CORS, cross_origin
from tinydb import Query
from db import DB

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = DB()


@app.route('/', methods=['GET'])
def index():
    return 'Server running...'


@app.route('/add', methods=['POST'])
@cross_origin()
def addItem():
    data = request.get_json()
    db.items.insert(data)
    # print(request.get_data())
    return ''


@app.route('/animals', methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def addAnimal():
    if request.method == 'GET':
        return db.animals.all()
    elif request.method == 'POST':
        data = request.get_json()
        db.animals.insert(data)
        return f'{data.animal}'
    else:
        data = request.get_json()
        query = Query()
        db.animals.remove(query.animal == data['animal'])
        # print(data['animal'])
        return ''


if __name__ == '__main__':
    app.run()
