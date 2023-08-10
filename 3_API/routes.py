from flask import Flask, jsonify, request
from flask_cors import cross_origin
from bson.objectid import ObjectId

import pymongo
import gridfs
import certifi

uri = "mongodb+srv://andreislavila:Lkm5SQZ2ys7n0yJ1@cluster0.dmi1jxq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
database = client["webdevws"]
fs = gridfs.GridFS(database)

userCollection = database["users"]
gamesCollection = database["games"]
highScoresCollection = database["scores"]

app = Flask(__name__)




@app.route('/registerUser/<username>/<password>', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_user(username, password):

    query = {'username': username}
    document = userCollection.find_one(query)
    
    if(document):
        print("Userul exista")
        return("Userul exista")
    else:
        # requested_id = 0
        # data = {
        #     'username': username,
        #     'password': password
        # }

        new_user = {'username': username, 'password': password}
        userCollection.insert_one(new_user)

        return jsonify(str(new_user))

        # requested_id = userCollection.insert_one(data).inserted_id
        # return jsonify(str(requested_id))




# ====================================



@app.route('/getImageById/<id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_image(id):
    out = fs.get(ObjectId(id))
    return out.read()







@app.route('/getGames', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_games():
    result = []
    for game in gamesCollection.find():
        result.append({'_id': str(game['_id']), 'title': game['title'], 'description': game['description'], 'image': str(game['image'])})

    return jsonify(result=result)






@app.route('/getScores', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_scores():
    result = []
    for score in highScoresCollection.find():
        result.append({'_id': str(score['_id']), 'game': str(score['game']), 'user': str(score['user']), 'score': score['score']})

    return jsonify(result=result)







@app.route('/getScoresByGameID/<game>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_scores_game_id(game):
    result = []

    query = {'game': ObjectId(game)}
    document = highScoresCollection.find(query)

    for score in document:
        result.append({'_id': str(score['_id']), 'game': str(score['game']), 'user': str(score['user']), 'score': score['score']})

    return jsonify(result=result)





@app.route('/addScore', methods=['POST', 'PUT'])
@cross_origin(supports_credentials=True)
def add_score():
    dict = request.form.to_dict()
    requested_id = 0

    data = {
        'game': ObjectId(dict['game']),
        'user': dict['user'],
        'score': int(dict['score'])
    }
    if request.method == 'POST':
        requested_id = highScoresCollection.insert_one(data).inserted_id

    if request.method == "PUT":
        highScoresCollection.update_one({'game': data['game'], 'user': data['user']}, {'$set': {'score': data['score']}})
        requested_id = dict['_id']

    return jsonify(id=str(requested_id))






@app.route('/getScoreById/<id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_score(id):
    result = []
    #game_id_obj = ObjectId(game)
    query = {'_id': ObjectId(id)}
    document = highScoresCollection.find_one(query)
    print(document)

    # for score in document:
    #      result.append({'_id': score['_id'], 'game': score['game'], 'user': score['user'], 'score': score['score']})

    return jsonify(result=document['score'])

if __name__ == "__main__":
    app.run()