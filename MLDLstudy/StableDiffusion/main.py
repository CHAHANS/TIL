# Stable diffusion 코드구현 해보기

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
