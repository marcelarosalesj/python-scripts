# retrived from http://machinelearningmastery.com/how-to-load-data-in-python-with-scikit-learn/

import numpy as np
import urllib
# URL for the Pima Indians Diabetes dataset (UCI Machine Learning Repository)
url = "http://goo.gl/j0Rvxq"
# download the file
raw_data = urllib.urlopen(url)
#import pdb; pdb.set_trace()
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset.shape)
#print(dataset)
# separate the data from the target attributes
X = dataset[:,0:7]
y = dataset[:,8]
