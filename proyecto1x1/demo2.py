#
# This does basically the same that demo1.py does
#

from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import pdb
import pprint


# Photos under predictions 
#links = ["http://proyecto1x1.com/wp-content/uploads/2017/01/img_6398.jpg", "http://proyecto1x1.com/wp-content/uploads/2017/01/48.jpg",
#		"http://proyecto1x1.com/wp-content/uploads/2017/01/28947111905_ff4832692a_k.jpg", "http://proyecto1x1.com/wp-content/uploads/2017/01/p7281489.jpg", 
#		"http://proyecto1x1.com/wp-content/uploads/2017/01/palomilla.jpg", "http://proyecto1x1.com/wp-content/uploads/2017/01/dsc_0104_p.jpg" ]

links = ["http://proyecto1x1.com/wp-content/uploads/2017/01/img_6398.jpg", "http://proyecto1x1.com/wp-content/uploads/2017/01/48.jpg"]

# Authentication function
def authentication():
	login = open("login2.txt", "r")
	login = login.readlines()

	for idx in range(0,len(login)):
		login[idx] = login[idx].split("=")[1].strip();

	client_id = login[0]
	client_secret = login[1]
	access_token = login[2]

	app = ClarifaiApp(client_id, client_secret)

	return app

# Create Clarifai model
app = authentication()
model = app.models.get('general-v1.3')

# Create a file to store there the results
filename = input("Filename: ")
file = open(filename+".txt", "a" )

# Iterate through the links
for link in links:
	image = ClImage(url=link)
	# Predict and store into the file
	result = model.predict([image])
	pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
	file.write("\n\n---------------------------------------------\n\n")


# Close the file
file.close()

