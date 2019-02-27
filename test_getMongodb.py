#coding:utf8
from pymongo import MongoClient
import datetime

client = MongoClient("10.10.10.172",27017)
db=client.projects
project = "circle"
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

item = db[project].find_one({"name":"김정기"})
item["text"] = "나대지마라"
db[project].update_one({"name":"김정기"},{"$set":item},upsert=False)
#for doc in db[project].find():
	#print(doc.get("name",""))
	
	#print(doc.get("text",""))
	#tags = doc.get("tags",[])
	#for tag in tags:
	#	print("\t" + tag)
