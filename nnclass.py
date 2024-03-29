import torch.nn as nn
from torchvision.io import read_image
import swin_transformer as sw
import math as m

class swinT2(nn.Module):
    def __init__(self):
        super().__init__()
        self.swinT = sw.SwinTransformer(img_size=(
            128, 128), patch_size=4, window_size=4, in_chans=1, depths=[12], embed_dim=12, drop_rate=0.3)
        self.swinT2 = sw.SwinTransformer(img_size=(
            32, 32), patch_size=4, window_size=4, in_chans=12, depths=[12], embed_dim=24, drop_rate=0.3)

        self.convStack = nn.Sequential(
            
          
            nn.ConvTranspose2d(24, 16, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 8, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ConvTranspose2d(8, 4, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
              nn.ConvTranspose2d(4, 1, 3, padding=1,
                               output_padding=1, stride=2),

        )

    def forward(self, x):
        x = self.swinT(x)
        H = 128
        W = 128
        B, HW, C = x.shape
        newH = int((H/(m.pow((H*W)/HW, 0.5))))
        newW = int((W/(m.pow((H*W)/HW, 0.5))))
        x = x.view(B, C, newH, newW)
        x = self.swinT2(x)
        H = 32
        W = 32
        B, HW, C = x.shape
        newH = int((H/(m.pow((H*W)/HW, 0.5))))
        newW = int((W/(m.pow((H*W)/HW, 0.5))))
        x = x.view(B, C, newH, newW)
        x = self.convStack(x)
        return x

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.convStack = nn.Sequential(
            nn.Conv2d(1, 6, 3, 2, 1),
            nn.ReLU(),
            nn.Conv2d(6, 12, 3, 2, 1),
            nn.ReLU(),
            nn.Conv2d(12, 24, 3, 2, 1),
            nn.ReLU(),
            nn.Conv2d(24, 48, 3, 2, 1),
            nn.ReLU(),
            nn.Conv2d(48, 48, 3, 2, 1),
            nn.ReLU(),
           
            nn.ConvTranspose2d(48, 48, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(48, 24, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(24, 12, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(12, 6, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(6, 1, 3, padding=1, output_padding=1, stride=2),
        )

    def forward(self, x):
        input = self.convStack(x)
        return input
    
class swinT(nn.Module):
    def __init__(self):
        super().__init__()
        self.swinT = sw.SwinTransformer(img_size=(
            128, 128), patch_size=4, window_size=4, in_chans=1, depths=[12], embed_dim=48, drop_rate=0.3)
        self.convStack = nn.Sequential(
            nn.ConvTranspose2d(48, 24, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(24, 12, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.Conv2d(12, 6, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(6, 3, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(3, 1, 3, padding=1),
        )

    def forward(self, x):
        x = self.swinT(x)
        H = 128
        W = 128
        B, HW, C = x.shape
        newH = int((H/(m.pow((H*W)/HW, 0.5))))
        newW = int((W/(m.pow((H*W)/HW, 0.5))))
        x = x.view(B, C, newH, newW)
        x = self.convStack(x)
        return x
    
class swinT3(nn.Module):
    def __init__(self):
        super().__init__()
        self.swinT = sw.SwinTransformer(img_size=(
            128, 128), patch_size=4, window_size=4, in_chans=3, depths=[12], embed_dim=12, drop_rate=0.3)
        self.swinT2 = sw.SwinTransformer(img_size=(
            32, 32), patch_size=4, window_size=4, in_chans=12, depths=[12], embed_dim=24, drop_rate=0.3)
        self.swinT3 = sw.SwinTransformer(img_size=(
            8, 8), patch_size=4, window_size=4, in_chans=24, depths=[6], embed_dim=48, drop_rate=0.1)

        self.convStack = nn.Sequential(
            nn.ConvTranspose2d(48, 36, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            
            nn.ConvTranspose2d(36, 24, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(24, 16, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 8, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ConvTranspose2d(8, 4, 3, padding=1,
                               output_padding=1, stride=2),
            nn.ReLU(),
              nn.ConvTranspose2d(4, 3, 3, padding=1,
                               output_padding=1, stride=2),

        )

    def forward(self, x):
        x = self.swinT(x)
        H = 128
        W = 128
        B, HW, C = x.shape
        newH = int((H/(m.pow((H*W)/HW, 0.5))))
        newW = int((W/(m.pow((H*W)/HW, 0.5))))
        x = x.view(B, C, newH, newW)
        x = self.swinT2(x)
        H = 32
        W = 32
        B, HW, C = x.shape
        newH = int((H/(m.pow((H*W)/HW, 0.5))))
        newW = int((W/(m.pow((H*W)/HW, 0.5))))
        x = x.view(B, C, newH, newW)
        x = self.swinT3(x)
        H = 8
        W = 8
        B, HW, C = x.shape
        newH = int((H/(m.pow((H*W)/HW, 0.5))))
        newW = int((W/(m.pow((H*W)/HW, 0.5))))
        x = x.view(B, C, newH, newW)
        x = self.convStack(x)
        return x
    
class FCNN(nn.Module):
    def __init__(self):
        super().__init__()
        inSize=32*32
        self.fc1 = nn.Linear(inSize,int(inSize/2))
        self.fc2 = nn.Linear(int(inSize/2),int(inSize/4))
        self.fc3 = nn.Linear(int(inSize/4),int(inSize/8))
        self.fc4 = nn.Linear(int(inSize/8),8)
        
        

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.fc4(x)
        return x
