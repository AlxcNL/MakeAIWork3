from pymongo import MongoClient


class MongoAdapter:
    def __init__(self, mongoDB, collectionName):
        self.client = MongoClient(
            host="localhost:27017",
            serverSelectionTimeoutMS=3000,
            username="student",
            password="miw3",
        )

        self.dbName = mongoDB
        self.collectionName = collectionName

    def getClient(self):
        return self.client

    def getCollection(self):
        db = self.client[self.dbName]
        return db[self.collectionName]

    # Create and Update
    def insertOne(self, dictToInsert):
        collection = self.getCollection()
        collection.insert_one(dictToInsert)

    # Delete
    def deleteCollection(self):
        collection = self.getCollection()
        collection.drop()
