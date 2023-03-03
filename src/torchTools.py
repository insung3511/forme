from tqdm import tqdm

import torch

class torchTools:
    def __init__(self, model, critention, device):
        super(torchTools, self).__init__()
        self.model = model 
        self.critention = critention
        self.device = device

    def ValidationLoss(self, dataloader):
        n = len(dataloader)
        running_loss = 0.0
        with torch.no_grad():
            self.model.eval()
            with tqdm(total=dataloader.__len__, position=0, leave=True) as pbar:
                for data in tqdm(dataloader, position=0, leave=True, desc=f"Validation loss: {running_loss}"):
                    images, labels = data[0].to(self.device), data[1].to(self.device)
                    outputs = self.model(images)
                    loss = self.critention(outputs, labels)
                    running_loss += loss.item()

            self.model.train()
            return running_loss / n
        
class torchToolsSupervisiedLearning:
    def __init__(self, model, optimizer, critention, device):
        self.model = model
        self.optimizer = optimizer
        self.critention = critention
        self.device = device

    def TrainingModel(self, EPOCH, train_dataloader, test_dataloader=None):
        running_loss = 0.0
        for epoch in range(EPOCH + 1):
            with tqdm(total=train_dataloader.__len__, position=0, leave=True) as pbar:
                for data in tqdm(train_dataloader, position=0, leave=True, desc=f"{epoch}th Training. Train loss: {running_loss}"):
                    inputs = data[0].to(self.device)
                    labels = data[1].to(self.device)
                    self.optimizer.zero_grad()

                    outputs = self.model(inputs)
                    
                    loss = self.critention(labels, outputs)
                    loss.backward()
                    self.optimizer.step()

                    running_loss += loss.item()

                if test_dataloader != None:
                    validationObj = torchTools(self.model, self.critention, self.device)
                    validationObj.ValidationLoss(self.test_dataloader)
