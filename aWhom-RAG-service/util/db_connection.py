from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
    
def getting_persona(db_pass, cluster_name, collection_name, user_id):
    uri = f"mongodb+srv://dndyd0206:{db_pass}@ha-rag-meta.nd2p6.mongodb.net/?retryWrites=true&w=majority&appName=HA-RAG-META"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        
    db_name = client[cluster_name]
    collection = db_name[collection_name]
    
    selected_row = collection.find({"user_id": user_id})
    return selected_row[0]['generated_persona']