from pymongo import MongoClient, database
import os


class MongoServices(object):

    DATABASE = None

    # TODO: Write the function insertMany
    # TODO: Write the function removeMany

    @staticmethod
    def initialize() -> database.Database:
        MONGO_USER = os.environ.get("MONGO_USER")
        MONGO_PASS = os.environ.get("MONGO_PASS")

        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster-study.xtphu.mongodb.net/admin?readPreference=primary&authSource=admin&authMechanism=SCRAM-SHA-1"

        data_base_name = 'financial-control'
        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(CONNECTION_URL)

        # Create the database for our example (we will use the same database throughout the tutorial
        MongoServices.DATABASE = client[data_base_name]

    @staticmethod
    def insert(collection, data):
        id_cod = MongoServices.DATABASE[collection].insert(data)
        return id_cod

    @staticmethod
    def find(collection, query):
        return MongoServices.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return MongoServices.DATABASE[collection].find_one(query)

    @staticmethod
    def delete(collection, query):
        MongoServices.DATABASE[collection].remove(query)


# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#     from dotenv import find_dotenv, load_dotenv
#     load_dotenv(find_dotenv())
#     # Get the database
#     MongoServices.initialize()

#     item_details = MongoServices.find("accounts", {})
#     for item in item_details:
#         # This does not give a very readable output
#         print(item)

#     data = {
#         "testStr": "test",
#         "testNumber": 1234
#     }
#     print(MongoServices.insert("test", data))
