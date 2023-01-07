'''
INPUT: location of image of cropped chess board
OUTPUT: fen code

1. gonna need to import the best model
2. user is going to supply a file path that has the snippet of the image
3. In reality, the model needs to be trained for each book cuz it isn't a convolutional net, so you will need to retrain
'''
from the_nn import *
from functions import jpg_to_fen

model = NN.load_best_model()
location = input("input the file path of the jpg file")
print(jpg_to_fen(model, location))
