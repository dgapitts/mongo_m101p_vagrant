import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.students
dummy = db.dummy

#> db.dummy.find().sort({value:-1}).limit(1).skip(3)
#{ "_id" : 2, "value" : 5 }

try:
   cursor=dummy.find()
   cursor=cursor.skip(3).limit(1).sort('value',pymongo.DESCENDING)
except:
   print "Unexpected error:", sys.exc_info()[0]

sanity = 0
for doc in cursor:
   print doc
   sanity += 1
   if (sanity > 10):
      break
