import os
import ssl
import certifi
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import torchvision.models as models
import numpy as np

# Set SSL certificate environment variable
os.environ['SSL_CERT_FILE'] = certifi.where()

# Define paths
train_dir = '/Users/youssefghaleb/Desktop/BleachedCorals_and_HealthyCoralsClassification/Training'
test_dir = '/Users/youssefghaleb/Desktop/BleachedCorals_and_HealthyCoralsClassification/Testing'

# Transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load datasets
train_dataset = ImageFolder(root=train_dir, transform=transform)
test_dataset = ImageFolder(root=test_dir, transform=transform)

# Data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=4)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, num_workers=4)

# Define the model
class CoralClassifier(nn.Module):
    def __init__(self):
        super(CoralClassifier, self).__init__()
        self.model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
        self.model.fc = nn.Linear(self.model.fc.in_features, 2)  # Assuming 2 classes: healthy and bleached

    def forward(self, x):
        return self.model(x)

# Initialize model, loss function and optimizer
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = CoralClassifier().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Early stopping parameters
early_stopping_patience = 5
best_loss = np.inf
epochs_no_improve = 0

# Training the model
def train_model(model, train_loader, criterion, optimizer, num_epochs=10):
    global best_loss, epochs_no_improve
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        print(f'Starting epoch {epoch+1}')
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        avg_train_loss = running_loss / len(train_loader)
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_train_loss:.4f}")

        # Early stopping
        if avg_train_loss < best_loss:
            best_loss = avg_train_loss
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if epochs_no_improve >= early_stopping_patience:
            print("Early stopping triggered")
            break

# Evaluating the model
def evaluate_model(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print(f'Accuracy of the model on the test images: {accuracy:.2f}%')

if __name__ == '__main__':
    print("Starting training process...")
    train_model(model, train_loader, criterion, optimizer, num_epochs=50)

    torch.save(model.state_dict(), 'coral_classifier.pth')   # Saves the model
    print("Model saved to coral_classifier.pth")

    print("Starting evaluation process...")
    evaluate_model(model, test_loader)
    print("Script finished.")

