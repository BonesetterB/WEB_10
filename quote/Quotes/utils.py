from pymongo import MongoClient

def get_base():

    client=MongoClient(f"mongodb+srv://CityNine:{{PASSWORD}}@croaker.hbarqcq.mongodb.net/?retryWrites=true&w=majority")
    
    db=client.HMW_09

    return db