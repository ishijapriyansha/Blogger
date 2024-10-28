import pymongo
uri='mongodb://127.0.0.1:27017'
client=pymongo.MongoClient(uri)
dbname=client['test']  #database-test
db = dbname['blogs']  #collection-blogs

