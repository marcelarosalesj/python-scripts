from clarifai import rest
from clarifai.client import ClarifaiApi
from clarifai.rest import Image as ClImage
import pdb
import pprint


login = open("login1.txt", "r")
login = login.readlines()

for idx in range(0,len(login)):
	login[idx] = login[idx].split("=")[1].strip();

client_id = login[0]
client_secret = login[1]
access_token = login[2]

app = ClarifaiApi(client_id, client_secret)

file = open("prediction.txt", "a" )

result = app.tag_image_urls("http://proyecto1x1.com/wp-content/uploads/2017/01/img_6398.jpg")
pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
file.write("\n---------------------------------------------")
file.write("\n---------------------------------------------\n")
#file.write(str(result) + "\n")
result = app.tag_image_urls("http://proyecto1x1.com/wp-content/uploads/2017/01/48.jpg")
pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
file.write("\n---------------------------------------------")
file.write("\n---------------------------------------------\n")
#file.write(str(result) + "\n")
result = app.tag_image_urls("http://proyecto1x1.com/wp-content/uploads/2017/01/28947111905_ff4832692a_k.jpg")
pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
file.write("\n---------------------------------------------")
file.write("\n---------------------------------------------\n")
#file.write(str(result) + "\n")
result = app.tag_image_urls("http://proyecto1x1.com/wp-content/uploads/2017/01/p7281489.jpg")
pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
file.write("\n---------------------------------------------")
file.write("\n---------------------------------------------\n")
#file.write(str(result) + "\n")
result = app.tag_image_urls("http://proyecto1x1.com/wp-content/uploads/2017/01/palomilla.jpg")
pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
file.write("\n---------------------------------------------")
file.write("\n---------------------------------------------\n")
#file.write(str(result) + "\n")
result = app.tag_image_urls("http://proyecto1x1.com/wp-content/uploads/2017/01/dsc_0104_p.jpg")
pprint.PrettyPrinter(indent=4, stream=file).pprint(result)
file.write("\n---------------------------------------------")
file.write("\n---------------------------------------------\n")
#file.write(str(result) + "\n")

file.close()
