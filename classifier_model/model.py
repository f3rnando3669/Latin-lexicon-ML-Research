import torch
import torch.nn as nn

class ProteinClassificationModel(nn.Model):
    def __init__(self, input_dim, num_classes):
        super(ProteinClassificationModel, self).__init__()
        self.fc = nn.Linear(input_dim, num_classes)

    def forward(self,x):
        x = self.fc(x)
        return x