import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.students
grades=db.grades

#> db.dummy.find().sort({value:-1}).limit(1).skip(3)
#{ "_id" : 2, "value" : 5 }

try:
   cursor=grades.find({"type":"homework"})
   cursor=cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])
except:
   print "Unexpected error:", sys.exc_info()[0]

sanity = 0
dict_del_key = {}
for doc in cursor:
   if sanity%2==1:
      del_key=doc['_id']
      dict_del_key['_id']=del_key
      #print del_key
      print dict_del_key
      grades.remove(dict_del_key)
   sanity += 1
