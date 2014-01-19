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


cursor = []         # Placeholder so blog compiles before you make your changes
l = []

cursor=posts.find()
cursor=cursor.sort('date',pymongo.DESCENDING)
cursor=cursor.limit(10)


for post in cursor:
    post['date'] = post['date'].strftime("%A, %B %d %Y at %I:%M:%S%p") # fix up date
    print post['date']
    if 'tags' not in post:
        post['tags'] = [] # fill it in if its not there already
    if 'comments' not in post:
        post['comments'] = []

    l.append({'title':post['title'], 'body':post['body'], 'post_date':post['date'],
              'permalink':post['permalink'],
              'tags':post['tags'],
              'author':post['author'],
              'comments':post['comments']})

print l
