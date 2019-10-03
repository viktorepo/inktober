#To see a live verion of this (Using Python3) go to https://repl.it/@viktorepo/bait

import urllib2
import json
import random

#The Token is individual. I'm using mine for this example.
#To get yours, register at trefle.io
token = "MjV2Tjg2Q24zbFlyRmEyUWhwb2JVZz09"
page=random.randint(1,20) #there are 20 pages on the result of the GET Request
contents = urllib2.urlopen("http://trefle.io/api/plants?q=berry&token="+token+"&page="+str(page)).read()
id = json.loads(contents)[random.randint(1,30)].get('id')
plant=urllib2.urlopen("http://trefle.io/api/plants/"+str(id)+"?token="+token).read()
neo_plant=json.loads(plant)
keys=['common_name','scientific_name','family_common_name','duration']
berry = {}

for i in keys:
	if neo_plant.get(i) is not None:
		berry.update({i : neo_plant.get(i)})
print("Details of your berry:")
for k,v in berry.iteritems():
	print("{}: {}".format(k,v))