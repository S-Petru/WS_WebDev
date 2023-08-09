import pymongo
import certifi
import gridfs

uri = "mongodb+srv://andreislavila:Lkm5SQZ2ys7n0yJ1@cluster0.dmi1jxq.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

database = client["webdevws"]
fs = gridfs.GridFS(database)

userCollection = database["users"]
userList = [{"username": "usr1", "password": "1234"},
            {"username": "usr2", "password": "1234"},
            {"username": "usr3", "password": "1234"},
            {"username": "usr4", "password": "1234"},
            {"username": "usr5", "password": "1234"},
            {"username": "usr6", "password": "1234"}
]

userIDs = userCollection.insert_many(userList)
print(userIDs.inserted_ids)

gamesCollection = database["games"]
gameList = [
    {"title": "Balloon Madness", "description": "Challenge your precision and reflexes in this addictive balloon-popping game!", "image": ""},
    {"title": "Endless Runner", "description": "Dash through a dynamic world, dodge obstacles, and set new high scores in this exhilarating endless runner game!", "image": ""},
    {"title": "Coming Soon", "description": "[Coming Soon]", "image": ""}
]

try:
    file1 = open("balloons.avif", "rb")
    content1 = file1.read()
    out1 = fs.put(content1, filename="balloons.avif")
    gameList[0]["image"] = out1


    try:
        file2 = open("runner.jpg", "rb")
        content2 = file2.read()
        out2 = fs.put(content2, filename="runner.jpg")
        gameList[1]["image"] = out2
        
        try:
            file3 = open("comingSoon.jpg", "rb")
            content3 = file3.read()
            out3 = fs.put(content3, filename="comingSoon.jpg")
            gameList[2]["image"] = out3

            gamesIDs = gamesCollection.insert_many(gameList)
            print(gamesIDs.inserted_ids)
            # print("G0>>", gamesIDs.inserted_ids[0])
            # print("G1>>", gamesIDs.inserted_ids[1])
            # print("G2>>", gamesIDs.inserted_ids[2])

            highScoresCollection = database["scores"]
            highScoresList = [
                 {"game": "", "user": "", "score": 22},
                 {"game": "", "user": "", "score": 33},
                 {"game": "", "user": "", "score": 11},
                 {"game": "", "user": "", "score": 44},
                 {"game": "", "user": "", "score": 55},
                 {"game": "", "user": "", "score": 88}
            ]


            # De facut cu un for probabil===      
            #  probabil foloseam si asta str(gamesIDs.inserted_ids[0]) 
            # sa elimin nevoia de a folosi in routes  from bson.objectid import ObjectId

            highScoresList[0]["game"] = gamesIDs.inserted_ids[0]
            highScoresList[0]["user"] = userIDs.inserted_ids[0]

            highScoresList[1]["game"] = gamesIDs.inserted_ids[1]
            highScoresList[1]["user"] = userIDs.inserted_ids[1]

            highScoresList[2]["game"] = gamesIDs.inserted_ids[1]
            highScoresList[2]["user"] = userIDs.inserted_ids[2]

            highScoresList[3]["game"] = gamesIDs.inserted_ids[0]
            highScoresList[3]["user"] = userIDs.inserted_ids[3]

            highScoresList[4]["game"] = gamesIDs.inserted_ids[1]
            highScoresList[4]["user"] = userIDs.inserted_ids[4]

            highScoresList[5]["game"] = gamesIDs.inserted_ids[0]
            highScoresList[5]["user"] = userIDs.inserted_ids[5]

            highScoresCollection.insert_many(highScoresList)
        except:
            print("Err at upload3")

    except:
            print("Err at upload2")

except: 
    print("Err at upload1")


# === Incarcare / Descarcare imagini din DB

# try:
#     file = open("balloons.avif", "rb")
#     content = file.read()
#     out = fs.put(content, filename="balloons.avif")
#     print(out)
#     try:
#         out2 = fs.get(out)
#         file2 = open("balloons2.avif", "wb")
#         bytearray = out2.read()
#         file2.write(bytearray)
#     except:
#         print("Err at download")
# except:
#     print("Err at upload")
