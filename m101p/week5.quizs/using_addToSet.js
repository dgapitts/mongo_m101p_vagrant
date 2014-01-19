use agg
db.products.aggregate([
    {$group:
     {
	 _id: {
	     "maker":"$manufacturer"
	 },
	 categories:{$addToSet:"$category"}
     }
    }
])

use test
db.zips.aggregate([
    {$group:
     {
	 _id: {
	     "city":"$city"
	 },
	 categories:{$addToSet:"$_id"}
     }
    }
])

