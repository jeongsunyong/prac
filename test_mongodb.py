from pymongo import MongoClient
import datetime

client  = MongoClient("10.10.10.162", 27017)
db = client.projects
project = "circle"
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
human = {"name" :"sunyong",
	"name_eng" :"sunyong",
	"phone" :"01091083062",
	"email" :"sunyong0321@naver.com",
	"date" :date,
	"age":37,
	"subinfo":{
		"password":"********",
		"etc":"*******",
	}
}
db[project].insert_one(human)

