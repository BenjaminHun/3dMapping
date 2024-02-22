import numpy as np
import nnclass as n
import time
import torch

x = np.random.rand(32*32)
x= torch.tensor(x, dtype=torch.float32).cuda()
model = n.FCNN()
model = model.cuda()
start = time.time()
output = model(x) 
end = time.time()
print(end - start)