import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.school
students=db.students


ids_scores_dict = {}
for ids_scores_cursor in students.find():
   #print ids_scores_cursor["_id"]
   #print ids_scores_cursor["scores"]
   ids_scores_dict[ids_scores_cursor["_id"]]=ids_scores_cursor["scores"]
for rec in ids_scores_dict:
   print ids_scores_dict[rec]
   #print rec['_id']
   #print rec['scores']
#for key in student_ids:
#   for rec in students.find({"_id"})   