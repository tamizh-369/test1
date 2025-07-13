import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("D:/Projects/test-35fdd-firebase-adminsdk-fbsvc-64e7dd6fab.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Print leaderboard sorted by score
users = db.collection('leaderboard').order_by('score', direction=firestore.Query.DESCENDING).stream()
found = False
for user in users:
    print(f"{user.id}: {user.to_dict()['score']}")
    found = True
if not found:
    print("No users in leaderboard.")
