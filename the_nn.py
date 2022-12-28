from PIL import Image
import os
from Chess_Pieces_Dataset import ChessPiecesDataset
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torchvision.datasets as datasets # Has standard datasets we can import in a nice and easy way
import torchvision.transforms as transforms # Transformations we can perform on our dataset

class NN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_size, 25)
        self.fc2 = nn.Linear(25, 25)
        self.fc3 = nn.Linear(25, num_classes)
        self.dropout = nn.Dropout(p=.2)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        return x

    @classmethod
    def load_best_model(cls):
        path = r'C:\Users\YoungShkreli\PycharmProjects\deep_learning\best_model4'
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        input_size = 30000
        num_classes = 13
    
        best_model = NN(input_size=input_size, num_classes=num_classes).to(device)
        best_model.load_state_dict(torch.load(path))
        best_model.eval()
        return best_model
