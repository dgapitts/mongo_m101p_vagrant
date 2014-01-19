import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.students
grades = db.grades

try:
        doc=grades.find_one()

except:
        print "Unexpected error:", sys.exc_info()[0]

print doc
