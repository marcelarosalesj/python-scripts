#
# Demo3 tries to train a Clarifai Model
# Update:
# I'm not sure, but I think this works... 
# Here I can see the model preview.clarifai.com

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
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/01/img_6398.jpg", concepts=['man', 'tattoo', 'portrait'])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/01/48.jpg", concepts=['black and white', 'window', 'blur'])
model = app.models.create('1x1', concepts=['man', 'tattoo', 'portrait','black and white', 'window', 'blur'])
model = app.models.get('1x1')
model.train()

# Close the file
file.close()

