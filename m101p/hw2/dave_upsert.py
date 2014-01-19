import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.dgapitts
students = db.students

def using_upsert():

    print "updating with upsert"

    try:

        # lets remove all stuff from students
        #students.remove({})
        students.drop()

        #create new students collection in the dgapitts mongo database 
        students.update({'_id':001}, {'_id':001,'name':'Dave','homework':[],'quiz':[],'final exam':None}, upsert=True)
        current = students.find_one({'_id':001})
        print "after creating initial student record : ", current

        #progressively add quiz scores 
        students.update({'_id':001}, {'_id':001,'name':'Dave','homework':[],'quiz':[90],'final exam':None}, upsert=True)
        students.update({'_id':001}, {'_id':001,'name':'Dave','homework':[],'quiz':[90,70],'final exam':None}, upsert=True)
        students.update({'_id':001}, {'_id':001,'name':'Dave','homework':[],'quiz':[90,70,80],'final exam':None}, upsert=True)
        current = students.find_one({'_id':001})
        print "and after adding 3 quiz results : ", current

        #and then the first homework assignment 
        students.update({'_id':001}, {'_id':001,'name':'Dave','homework':[75],'quiz':[90,70,80],'final exam':None}, upsert=True)
        current = students.find_one({'_id':001})
        print "and after adding 3 quiz results : ", current

        #switching to append and $set to add 100 and 75 to the 'homework' scores 
        current = students.find_one({'_id':001})
        print "before using append and $set oprations to append (100,75) : ", current
        print "and extracting just the homework : " + str(current['homework'])
        current['homework'].append(100)
        current['homework'].append(75)
        print "and after appending 2nd score : " + str(current['homework'])
        db.students.update({'_id':current['_id']},{'$set':{'homework': current['homework']}},upsert=False, multi=False)

        current = students.find_one({'_id':001})
        print "and now our query returns : ", current

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise




using_upsert()

