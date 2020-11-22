# -*- coding: utf-8 -*-
"""DeepLearning_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PnE4NLVBnl5TuavkKgF2egANbNnegRDh
"""

import torch
import matplotlib.pyplot as plt
import numpy as np
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import seaborn as sns



class LeNet(nn.Module):
    def __init__(self): 
        super(LeNet, self).__init__()
        self.cnn_model = nn.Sequential(
            nn.Conv2d(1, 6, 5),         
            nn.Tanh(),
            nn.AvgPool2d(2, stride=2),  
            nn.Conv2d(6, 16, 5),       
            nn.Tanh(),
            nn.AvgPool2d(2, stride=2)   
        )
        self.fc_model = nn.Sequential(
            nn.Linear(256,120),        
            nn.Tanh(),
            nn.Linear(120,84),         
            nn.Tanh(),
            nn.Linear(84,10)     ,
            nn.Softmax()
        )
        
    def forward(self, x):
        x = self.cnn_model(x)
    
        x = x.view(x.size(0), -1)
       
        x = self.fc_model(x)
        return x

batch_size = 128
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transforms.ToTensor())
trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transforms.ToTensor())
testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False)

def evaluation(dataloader):
    total, correct = 0, 0
    for data in dataloader:
        inputs, labels = data
        outputs = net(inputs)
        _, pred = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (pred == labels).sum().item()
    return 100 * correct / total



net =LeNet()

gradient_norms=[]

def grad(parameters):
  grad_tensor = torch.zeros(0)
  grad_tensor=grad_tensor.to(device)
  for w, b in parameters:
    print(n)
    if b.requires_grad and "bias" not in w:
      curr_tensor = torch.flatten(b.grad.data)
      print(curr_tensor.size())
      grad_tensor = torch.cat((grad_tensor,curr_tensor),0)
  gradiant_norms.append(grad_tensor.norm().item())



import torch.optim as optim

loss_fn = nn.CrossEntropyLoss()
opt = optim.Adam(net.parameters())

loss_arr = []
loss_epoch_arr = []
max_epochs = 6

for epoch in range(max_epochs):

    for i, data in enumerate(trainloader, 0):

        inputs, labels = data

        opt.zero_grad()

        outputs = net(inputs)
        loss = loss_fn(outputs, labels)
        loss.backward()
        opt.step()
        
        loss_arr.append(loss.item())
        
    loss_epoch_arr.append(loss.item())
  
    print('Epoch: %d/%d, Test acc: %0.2f, Train acc: %0.2f' % (epoch, max_epochs, evaluation(testloader), evaluation(trainloader)))
    
    
plt.plot(loss_epoch_arr)
plt.show()

max_epochs = 1000

for epoch in range(max_epochs):

    for i, data in enumerate(trainloader, 0):

        inputs, labels = data

        opt.zero_grad()

        outputs = net(inputs)
        loss = loss_fn(outputs, labels)
        loss.backward()
        opt.step()

    grad(net.parameters)



x = np.arange(len(gradiant_norms))
plt.scatter(x,grad_norms)
plt.plot(x,gradiant_norms)