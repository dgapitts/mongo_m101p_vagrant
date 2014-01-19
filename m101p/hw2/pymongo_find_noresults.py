import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.students
grades = db.grades

query = {'media.oembed.type':'video'}
projection = {'media.oembed.url':1, '_id':0}

try:
   cursor=grades.find(query, projection)
except:
   print "Unexpected error:", sys.exc_info()[0]

for doc in cursor:
   print doc
   sanity += 1
   if (sanity > 10):
      break
