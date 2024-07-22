"""Module storing FirestoreClient class
"""

import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreClient():
    
    def __init__(self, collection: str):
        """Initialiser method
        """
        cred = credentials.Certificate('./ServiceAccountKey.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        self._collection = db.collection(collection)
        
    def create(self, data: dict):
        """Add into collection a new named document with provided data
        """
        self._collection.document(data["id"]).set(data)
        
    def search(self, id: str) -> dict:
        """Search a document in the collection by using document ID
        """
        result = self._collection.document(id).get()
        if result.exists:
            return result.to_dict()
        else:
            return None
    
    def update(self, data: dict):
        """Update a named document with provided data
        """
        id = data["id"]
        del(data["id"])
        self._collection.document(id).update(data)
        
    def delete(self, id: str):
        """Delete a named document from collection by using document ID
        """
        self._collection.document(id).delete()