'''
INPUT: location of image of cropped chess board
OUTPUT: fen code

1. gonna need to import the best model
2. user is going to supply a file path that has the snippet of the image
'''
from the_nn import *

def jpg_to_fen(model, location):
    '''this takes in a model which can then go square by square and identify
    what piece is on it.'''
    tensor = transforms.ToTensor() #turns the image into a tensor
    piece_dict = {0: 'b', 1: 'k', 2: 'n', 3: 'p', 4: 'q', 5: 'r',6: 'B', 7: 'K', 8: 'N', 9: 'P', 10: 'Q',  11: 'R', 12: ' '} #net outputs numbers, need to convert to FEN code for pieces, need this to do that.
    im = Image.open(location) #opens location
    width = im.size[0] #width of image
    height = im.size[1] #height of image


    lst = [] #what is in the list after the loop is just letters or the empty string, FEN has rules which will require there to be numbers for counting empty squares, so this isn't FEN yet
    for i in range(0,8):
        top = i * height/8
        bottom = (i+1) * height/8
        for i in range(0,8):
            left = i * width/8
            right = (i+1) * width/8
            img = Image.open(location).crop((left, top, right, bottom)).resize((100,100)) #selects a square
            x = tensor(img) # turns image into a tensor
            x = x.reshape(-1)# reshapes tensor I'm not sure why but it's required
            scores = model(x) #model transforms tensor of image into a vector
            max = scores.max() #chooses which number it most likely is within the vector
            lst.append(piece_dict[int((scores == max).nonzero(as_tuple=True)[0])]) # translates this number into a piece and adds to the list
        lst.append('/')

    pre_fen = ''.join(lst).split('/') #joins the list of characters into one string and then splits this by backslash - THIS IS A LIST of strings for each row which needs to then be put into FEN


    def get_row_fen(lst):
        '''translates the prefen '''
        counter = 0
        fen = []
        flag = 0  #is changed to one if the last element was not empty string
        for element in lst:
            if element == ' ':
                if len(fen) != 0:
                    if flag == 0:
                        fen.pop()

                counter += 1
                fen.append(str(counter))
                flag = 0
            else:
                counter = 0
                flag = 1
                fen.append(element)

        return ''.join(fen)

    new = []
    for item in pre_fen:
        new.append(get_row_fen(item))

    return '/'.join(new)