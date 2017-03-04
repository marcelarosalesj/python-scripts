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
#print("Authentication...")
print "Authentication..."
app = authentication()
#print("  done.")
print "  done."

#print("Create images...")
print "Create images..."
import pdb; pdb.set_trace()
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/01/img_6398.jpg", concepts=['hombre', 'tatuaje', 'retrato'])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/01/48.jpg", concepts=['blanco y negro', 'ventana', 'blur'])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/01/image-2017-01-03.jpg", concepts=["mujer", "persona", "paisaje", "color", "retrato"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/02/rebecca-massey-war-desert-editorial.jpg", concepts=["mujer", "persona", "paisaje", "arena", "cielo", "color"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/01/04380003.jpg", concepts=["luz", "neon", "azul", "rojo", "interior", "cuarto"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2017/01/amigos.jpg", concepts=["exterior", "perro", "animales", "plantas", "negro"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2016/12/uyuppie_19.jpg", concepts=["luz", "exterior", "dia", "desierto", "arena", "cielo"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2016/10/fuimos-memoria_abel-nervaez.jpg", concepts=["arboles", "tierra", "agua", "azul", "cielo", "dia", "exterior", "bosque"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2016/08/22599440633_b4863a9dbe_o.jpg", concepts=["bus", "personas", "blanco y negro", "mujer", "hombre", "urbano", "dia"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2016/06/img_0580.png", concepts=["personas", "metro", "urbano", "color", "mujer"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2016/04/2015-10-24-08.59.19-1.jpg", concepts=["paisaje", "urbano", "arquitectura", "lineas", "edificio"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2016/02/la-casa-del-tiempo-4.jpg", concepts=["interior", "flores", "cuarto", "cisne", "naturaleza muerta", "color"])
app.inputs.create_image_from_url(url="http://proyecto1x1.com/wp-content/uploads/2016/02/Captura-de-pantalla-2016-02-08-a-las-11.07.22.png", concepts=["cuerpo", "manos"])
#print("  done.")
print "  done."

#print("Create model...")
print "Create model..."
model = app.models.create('1x1', concepts=['man', 'tattoo', 'portrait','black and white', 'window', 'blur'])
model = app.models.get('1x1')
#print("  done.")
print "  done."

#print("Training...")
print "Training..."
model.train()
#print("  done.")
print "  done."



