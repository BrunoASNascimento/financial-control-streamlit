from pymongo import MongoClient, database
import os


def get_database() -> database.Database:
    MONGO_USER = os.environ.get("MONGO_USER")
    MONGO_PASS = os.environ.get("MONGO_PASS")

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster-study.xtphu.mongodb.net/admin?readPreference=primary&authSource=admin&authMechanism=SCRAM-SHA-1"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['financial-control']


# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#     from dotenv import find_dotenv, load_dotenv
#     load_dotenv(find_dotenv())
#     # Get the database
#     dbname = get_database()
#     print(type(dbname))
#     item_details = dbname['accounts'].find()
#     for item in item_details:
#         # This does not give a very readable output
#         print(item)
