import torch
import torch.nn as nn
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
from torchvision.io import ImageReadMode
import matplotlib.pyplot as plt
import pandas as pd
import os
from torchvision.io import read_image
from torch.utils.data import DataLoader
import numpy as np
import swin_transformer as sw
import math as m
import nnclass as n
import skimage.measure
import imageio
from skimage import img_as_ubyte
import torch.nn.functional as F
device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)


class CustomImageDataset(Dataset):

    def __init__(self, img_dir, annotations_file):
        super().__init__()
        self.img_dir = img_dir
        self.img_labels = pd.read_csv(annotations_file)

    def __len__(self):
        return len(self.img_labels)

    def parse_numbers_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                numbers = []
                lines = text.strip().split('\n')
                for line in lines:
                    nums = line.split(';')
                    numbers.extend([float(num) for num in nums])
                numbers = self.average_coordinates_with_removed(numbers)
                return numbers
        except FileNotFoundError:
            print("File not found.")
            return []

    def average_coordinates_with_removed(self, original_list):
        # Split the original list into x and y coordinates
        # Every even index is an x coordinate
        x_coordinates = original_list[::2]
        # Every odd index is a y coordinate
        y_coordinates = original_list[1::2]

        # Calculate the average of the removed items
        removed_x_avg = sum(x_coordinates[:4]) / 4
        removed_y_avg = sum(y_coordinates[:4]) / 4

        # Remove the last four coordinate pairs
        original_list = original_list[8:]

        # Calculate the average x and y coordinates
        avg_x = sum(x_coordinates[:4]) / len(x_coordinates[:4])
        avg_y = sum(y_coordinates[:4]) / len(y_coordinates[:4])

        # Append the averaged x and y coordinates along with the averaged removed items to the original list
        original_list.extend([removed_x_avg, removed_y_avg])

        return original_list

    def __getitem__(self, idx):
        noisedImgPath = os.path.join(
            self.img_dir, self.img_labels.iloc[idx, 0])

        image = read_image(noisedImgPath, ImageReadMode.GRAY)
        groundTruthImgPath = os.path.join(
            self.img_dir, self.img_labels.iloc[idx, 1])

        # Remove alpha layer
        label = self.parse_numbers_from_file(groundTruthImgPath)

        global device
        if device == "cuda":
            return torch.tensor(image, dtype=torch.float32).cuda(), torch.tensor(label, dtype=torch.float32).cuda()
        else:
            return torch.tensor(image, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)
