import pymongo
import sys
from sets import Set

connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.exam_q7
images=db.images
albums=db.albums


orphanIDs =  Set([])
safety=0
usedImages = Set([])


#GENERIC SET TEST OPERATIONS
#usedImages.add('test1')
#print usedImages
#usedImages.add('test2')
#print usedImages
#if 'test1' not in usedImages:
#   usedImages.add('test1')
#   print usedImages


for albums_cursor in albums.find({},{"images"}):
   for image_id in albums_cursor["images"]:
      if image_id not in usedImages:
         usedImages.add(image_id)
         #print "distinct image count : " + str(len(usedImages))
         #print "new image_id added : " + str(image_id)
      else:
         print "existing image_id added : " + str(image_id)
   #safety+=1
   #print "safety : " + str(safety)
   #if safety > 1000:
   #   break


print "distinct image count : " + str(len(usedImages))



for imagesIDs_cursor in images.find({},{"_id"}):
   #print imagesIDs_cursor["_id"]
   if imagesIDs_cursor["_id"] not in usedImages:
      orphanIDs.add(imagesIDs_cursor["_id"])
      images.remove({"_id":imagesIDs_cursor["_id"]})
      #print "orphan image ID added : " + str(imagesIDs_cursor["_id"]) 
      #safety+=1
      #if safety > 20:
      #   break

