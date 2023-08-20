from pymongo import MongoClient
import os


def get_base():
    mongodb_username = os.getenv("MONGODB_USERNAME")
    mongodb_password = os.getenv("MONGODB_PASSWORD")
    mongodb_cluster_url = os.getenv("MONGODB_CLUSTER_URL")
    mongodb_database = os.getenv("MONGODB_DATABASE")
    
    connection_string = f"mongodb+srv://{mongodb_username}:{mongodb_password}@{mongodb_cluster_url}/{mongodb_database}?retryWrites=true&w=majority"
    
    client = MongoClient(connection_string)
    db = client[mongodb_database]
    return db