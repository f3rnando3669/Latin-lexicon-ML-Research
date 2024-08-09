import torch
import torch.nn as nn

class ProteinClassificationModel(nn.Module):
    def __init__(self, input_dim):
        super(ProteinClassificationModel, self).__init__()
        # 2-5 Hidden Layers
        # Linear
        # ReLu
        # Linear
        # ReLu
        # Linear(1 Neuron)
        self.fc = nn.Linear(input_dim, 1)

    def forward(self,x):
        x = self.fc(x)
        return x