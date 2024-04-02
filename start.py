from control import Control
from model import CustomImageDataset
import torch
import torch.nn as nn
from torchvision.io import read_image
from torch.utils.data import DataLoader
import nnclass as n
from torchvision import datasets, transforms


from skimage import img_as_ubyte
import torch.nn.functional as F
transform = transforms.Compose([
    transforms.Resize((512, 1024)),  # Resize images to 1024x512
    transforms.ToTensor(),            # Convert images to tensors
])

trainDataset = CustomImageDataset("train/", "labels.txt",)
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
model = n.swinT2()


if device == "cuda":
    model = model.cuda()

learningRate = 1e-5
batchSize = 10
epochs = 300
loss = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
control.runTraining(epochs, trainDataloader,
                    testDataloader, model, loss, optimizer)
torch.save(model.state_dict(), "model.pth")
