from pymongo import MongoClient

client = MongoClient('localhost')
db = client.tint_data

def createUser(username, oauth_token):
	user = {}
	user['username'] = username
	user['oauth_token'] = oauth_token
	db.users.insert(user)

def updateUser(username, oauth_token):
	db.users.update({'username': username}, {'$set': {'oauth_token': oauth_token}})

def getUser(username):
	return db.users.find_one({'username': username})

def getToken(username):
	return getUser(username)['oauth_token']

def userExists(username):
	return bool(getUser(username))

def getOAuthToken(username):
	return getUser(username)['oauth_token']
