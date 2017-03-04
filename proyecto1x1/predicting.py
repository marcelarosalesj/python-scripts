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

#links = ["http://proyecto1x1.com/wp-content/uploads/2017/02/025_na.jpg", "http://proyecto1x1.com/wp-content/uploads/2017/03/dsc01089-editar.jpg", "http://proyecto1x1.com/wp-content/uploads/2017/02/observo_mientras_observan-amanda-mora-klein.jpg"]
links = ["http://proyecto1x1.com/wp-content/uploads/2017/02/025_na.jpg"]

# Authentication function
def authentication():
	file = open("login2.txt", "r")
	login = file.readlines()

	for idx in range(0,len(login)):
		login[idx] = login[idx].split("=")[1].strip();
		#print(" "+login[idx])

	client_id = login[0]
	client_secret = login[1]
	access_token = login[2]

	# Close the file
	file.close()

	app = ClarifaiApp(client_id, client_secret)

	return app

# Create Clarifai model
app = authentication()

model = app.models.get('1x1')

#pdb.set_trace()
# Create a file to store there the results
#filename = input("Filename: ")
#file = open(filename+".txt", "a" )

file = open("prediction2.txt", "a")

# Iterate through the links
"""
pdb.set_trace()
for link in links:
	print link
	image = ClImage(url=link)
	# Predict and store into the file
	result = model.predict([image])
	pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
	file.write("\n\n---------------------------------------------\n\n")
"""

image = ClImage(url="http://proyecto1x1.com/wp-content/uploads/2017/02/025_na.jpg")
# Predict and store into the file
result = model.predict([image])
pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
file.write("\n\n---------------------------------------------\n\n")



# Close the file
file.close()

