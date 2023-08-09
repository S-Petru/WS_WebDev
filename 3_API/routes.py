from flask import Flask, jsonify
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
    # print("Received game ID:", game)
    result = []

    game_id_obj = ObjectId(game)
    query = {'game': game_id_obj}
    document = highScoresCollection.find(query)

    for score in document:
        # print("Found score:", score)
        result.append({'_id': str(score['_id']), 'game': str(score['game']), 'user': str(score['user']), 'score': score['score']})

    return jsonify(result=result)

if __name__ == "__main__":
    app.run()