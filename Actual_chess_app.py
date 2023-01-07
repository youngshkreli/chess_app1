'''
INPUT: location of image of cropped chess board
OUTPUT: fen code

1. gonna need to import the best model
2. user is going to supply a file path that has the snippet of the image
3. In reality, the model needs to be trained for each book cuz it isn't a convolutional net, so you will need to retrain
'''
from the_nn import *
from functions import jpg_to_fen

try: #I don't know where the user is going to store the directory in their system, so they gotta enter some deets in the file
    model = NN.load_best_model()
except:
    "Go to the file the_nn and enter the file path of the best_model4"
    
location = input("input the file path of the jpg file")
print(jpg_to_fen(model, location))
