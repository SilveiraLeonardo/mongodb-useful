import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.deviasExampleDB
collection = db["test"]

# example 1
# {"_id":0, "name": "tim", "score": 5}
# post = {"name": "tim", "score": 5}
# collection.insert_one(post)

# example 2
# post1 = {"name": "leo", "score": 6}
# post2 = {"name": "tami", "score": 7}
# collection.insert_many([post1, post2])

# example 3
# results = collection.find({"name": "leo"})
# print(results) # returns: <pymongo.cursor.Cursor object at 0x7f7de2f1b3d0>
# # we need to loop through the results to get something meaningful
# for result in results:
# 	print(result)

# example 4
results = collection.find()
print(results) # returns: <pymongo.cursor.Cursor object at 0x7f7de2f1b3d0>
# we need to loop through the results to get something meaningful
for result in results:
	print(result)

# example 5
# results = collection.find()
# for result in results:
# 	print(result["name"])

# example 6
# results = collection.find({"name": "leo", "score": 6})
# print(results) # returns: <pymongo.cursor.Cursor object at 0x7f7de2f1b3d0>
# # we need to loop through the results to get something meaningful
# for result in results:
# 	print(result)

# example 7
# result = collection.find_one({"name": "leo"})
# print(result)

# example 8
# results = collection.delete_one({"name": "tami"})

# example 9 - update field
# results = collection.update_one({"name": "leo"}, {"$set":{"score":"8"}})

# example 10 - set new field
results = collection.update_one({"name": "tim"}, {"$set":{"profession":"teacher"}})