#coding:utf8
import redis

r= redis.Redis(host="10.10.10.172", port=6379)

#for i in range(100000):
#        r.set("공부좀해"+str(i),i+100000)

#r.set("rendercount",0)
#for i in range(10000000):
#	print r.get("rendercount")
#	r.incr("rendercount")
#	print r.get("rendercount")

r.set("jeongsunyong","01091083062")
