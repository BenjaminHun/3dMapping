from control import Control
from model import CustomImageDataset
import torch
import torch.nn as nn
from torchvision.io import read_image
from torch.utils.data import DataLoader
import nnclass as n

from skimage import img_as_ubyte
import torch.nn.functional as F

trainDataset = CustomImageDataset("train/", "labels.txt")
testDataset = CustomImageDataset("test/", "testLabel.txt")

trainDataloader = DataLoader(trainDataset, batch_size=10, shuffle=True)
testDataloader = DataLoader(testDataset, batch_size=10, shuffle=True)
outputPath = "swinT2"
control = Control(outputPath)


trainFeatures, trainLabels = next(iter(trainDataloader))
device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

print(f"Feature batch shape: {trainFeatures.size()}")
print(f"Labels batch shape: {trainLabels.size()}")

print(f"Using {device} device")
model = n.CnnToFCNN()


if device == "cuda":
    model = model.cuda()

learningRate = 1e-4
batchSize = 10
epochs = 300
loss = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
control.runTraining(epochs, trainDataloader,
                    testDataloader, model, loss, optimizer)
