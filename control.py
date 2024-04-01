

import imageio
import numpy as np
import torch
from skimage import img_as_ubyte

from test import homography


class Control:
    def __init__(self, outputPath):
        self.outputPath = outputPath
        pass

    def normalize(self, x):
        """
        Normalize a list of sample image data in the range of 0 to 1
        : x: List of image data.  The image shape is (32, 32, 3)
        : return: Numpy array of normalized data
        """
        return np.array((x - np.min(x)) / (np.max(x) - np.min(x)))

    def trainLoop(self, dataloader, model, loss_fn, optimizer):
        size = len(dataloader.dataset)
        model.train()
        i = 0
        for batch, (x, y) in enumerate(dataloader):
            pred = model(x)
            loss = loss_fn(pred, y)

            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            if batch % 10 == 0:
                loss, current = loss.item(), (batch+1)*len(x)
                with open(self.outputPath + "/"+"results.txt", "a", encoding="utf-8") as f:
                    f.write(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]\n")
                self.saveImg(i, x, y, pred)
                i += 1

    def testLoop(self, dataloader, model, loss_fn):
        model.eval()
        size = len(dataloader.dataset)
        num_batches = len(dataloader)
        test_loss, correct = 0, 0
        i = 0
        with torch.no_grad():
            for x, y in dataloader:
                pred = model(x)
                test_loss += loss_fn(pred, y).item()
                if i % 10 == 0:
                    # saveImg(i, x, y, pred)
                    i += 1

        test_loss /= num_batches
        with open(self.outputPath + "/"+"results.txt", "a", encoding="utf-8") as f:
            f.write(f"Test error: \n Avg loss:{test_loss:>8f}\n")

    def saveImg(self, i, x, y, pred):
        y = y[0].cpu().detach().numpy()
        pred = pred[0].cpu().detach().numpy()
        x = self.normalize(x[0].permute(
            1, 2, 0).contiguous().cpu().detach().numpy())
        x = np.repeat(x[:, :, :], 3, axis=2)
        y_pred = homography(x, pred)
        y_gt = homography(x, y)
        border = np.ones([3, 994, 3])
        img = img_as_ubyte(np.concatenate(
            (y_pred, border, y_gt, border, x), 0))
        imageio.imwrite(self.outputPath + "/"+str(i) +
                        "_result.png", img)

    def runTraining(self, epochs, trainDataloader, testDataloader, model, loss, optimizer):
        for t in range(epochs):
            with open(self.outputPath + "/"+"results.txt", "a", encoding="utf-8") as f:
                f.write(f"Epoch {t+1}\n------------------\n")
            self.trainLoop(trainDataloader, model, loss, optimizer)
            if t % 10 == 0:
                self.testLoop(testDataloader, model, loss)
