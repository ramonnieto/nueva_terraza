import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
from FirestoreDB import FirestoreClient

"""
cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Add documents with auto IDs
data = {
    'name': 'John Smith',
    'age': 40,
    'employed': True
}
db.collection('patients').add(data)

# Set documents with known IDs
data = {
    'name': 'Jane Doe',
    'age': 34,
    'employed': False
}
db.collection('patients').document().set(data)

db.collection('patients').document('janedoe').set(data)

# Merging
db.collection('patients').document('janedoe').set({'address': 'Madrid'}, merge=True)

db.collection('patients').document('janedoe').collection('movies').add({'name': 'Avengers'})

db.collection('patients').document('janedoe').collection('movies').document('HP').set({'name': 'Harry Potter'})

#  Read data

# Getting a doc with known ID
result = db.collection('patients').document('janedoe').get()
if result.exists:
    pprint(result.to_dict())
    
# Update data - known key
db.collection('patients').document('janedoe').update({'age': 50})

# Delete data - known key
db.collection('patients').document('janedoe').delete()

"""
    
dBclient = FirestoreClient("patients")
data = {
    'id': '12312342T',
    'name': 'Quique',
    'surname': 'Garcia',
    'age': 40
}
dBclient.create(data)
print(dBclient.get(data['id']))
    