import torch
import torchvision

def get_model():
    return torchvision.models.resnet(pretrained=True)

def get_pred(model):
    return model(torch.rand([1, 3, 224, 224]))

model = get_model()

for i in range(1, 10000):
    get_pred(model)


# py-spy record -o output/profile.svg -- python output/flametest.py