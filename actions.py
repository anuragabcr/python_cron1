from mongodb import mongodb 

def create_document(db_name, collection_name, document):
    db = mongodb[db_name]  
    collection = db[collection_name]  
    try:
        result = collection.insert_one(document)
        print(f"Document inserted successfully with ID: {result.inserted_id}")
        return result.inserted_id
    except pymongo.errors.PyMongoError as e:
        print(f"Error inserting document: {e}")
        return None

def find_documents(db_name, collection_name, query=None):
    db = mongodb[db_name]
    collection = db[collection_name]
    if query:
        return collection.find(query)
    else:
        return collection.find({}) 

def update_document(db_name, collection_name, document_id, update_data):
  try:
    db = mongodb[db_name]
    collection = db[collection_name]
    update_result = collection.update_one({"_id": document_id}, update_data)

    if update_result.matched_count == 1:
      updated_document = collection.find_one({"_id": document_id})
      return updated_document
    else:
      return None

  except Exception as e:
    print(f"Error updating document: {e}")
    return None

def delete_document(db_name, collection_name, document_id):
  try:
    db = mongodb[db_name]
    collection = db[collection_name]
    delete_result = collection.delete_one({"_id": document_id})
    
    return delete_result.deleted_count == 1

  except Exception as e:
    print(f"Error deleting document: {e}")
    return False

