import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


try:
    cred = credentials.Certificate("key.json")
except ValueError:
    print("No key.json found, using default credentials")
except IOError:
    print("No key.json found, using default credentials")

firebase_admin.initialize_app(cred)

db = firestore.client()
