__author__ = 'aje'


#
# Copyright (c) 2008 - 2013 10gen, Inc. <http://10gen.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

import sys
import re
import datetime,time
import pymongo



connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.blog
posts = db.posts


for i in range(10):

    # Build a new post
    print 'title'+str(i)
    post = {"title": 'title'+str(i),
            "author": 'author'+str(i),
            "body": 'post'+str(i),
            "permalink":'permalink'+str(i),
            "tags": 'tags_array'+str(i),
            "comments": [],
            "date": datetime.datetime.utcnow()}
    time.sleep(1)


    # now insert the post
    try:
        # XXX HW 3.2 Work Here to insert the post
        posts.insert(post)
        print "Inserting the post"
    except:
        print "Error inserting post"
        print "Unexpected error:", sys.exc_info()[0]


