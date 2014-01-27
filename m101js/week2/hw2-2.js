var MongoClient = require('mongodb').MongoClient, 
        request = require('request');

MongoClient.connect('mongodb://localhost:27017/weather', function(err, db) {

    var options = {sort:[['State',1],['Temperature',-1]]};
    var currentState;
    var cursor = db.collection('data').find({},{},options);
    cursor.each(function(err,doc){
        if(doc['State'] !== currentState){
                console.log('month high for ' + doc['State'] + ' was ' + doc['Temperature'] + '(_id:' + doc['_id'] + ')');
                currentState = doc['State'];
                doc["month_high"] = true;
                db.collection('data').save(doc,function(err,saved){
                                if(err) throw err;
                                console.dir('saved doc ' + saved);
                });
        }
    });
});
