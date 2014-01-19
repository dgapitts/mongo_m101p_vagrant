import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.school
students=db.students

#> db.dummy.find().sort({value:-1}).limit(1).skip(3)
#{ "_id" : 2, "value" : 5 }

ids_scores_dict = {}
#for keys in students.find({},{"_id":1}):
for ids_scores_cursor in students.find({"_id":{'$gt':2}}):
   #print ids_scores_cursor["_id"]
   #print ids_scores_cursor["scores"]
   ids_scores_dict[ids_scores_cursor["_id"]]=ids_scores_cursor["scores"]
for rec_id in ids_scores_dict:
   print str(ids_scores_dict)
   new_scores=[]
   min_homework=0
   for sub_dict in ids_scores_dict[rec_id]:
      internal = {};
      if sub_dict[u'type'] != 'homework':
         #print str(new_scores[(sub_dict['type'])])
         internal[u'type']=sub_dict['type']
         internal[u'score']=sub_dict['score']
         new_scores.append(internal)
      else:
         if min_homework==0:
            min_homework=sub_dict['score']
         else:
            internal[u'type']='homework'
            if min_homework<sub_dict['score']:
               internal[u'score']=sub_dict['score']
               new_scores.append(internal)
            else:
               internal[u'score']=min_homework
               new_scores.append(internal)
      #print str(internal)

  
   print 'rec_id : ' + str(rec_id) 
   print 'array of scores : ' + str(new_scores)
   #db.students.update({'_id':rec_id,{'$set':{'scores': new_scores}},upsert=False, multi=False)
   db.students.update({'_id':rec_id},{'$set':{'scores': new_scores}},upsert=False, multi=False)
