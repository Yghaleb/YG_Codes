import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image

# Explicitly set the device to CPU (adjust if you have GPU available)
device = torch.device('cpu')

# Define the CoralClassifier class
class CoralClassifier(nn.Module):
    def __init__(self):
        super(CoralClassifier, self).__init__()
        self.model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
        self.model.fc = nn.Linear(self.model.fc.in_features, 2)  # Assuming 2 classes: healthy and bleached

    def forward(self, x):
        return self.model(x)

# Initialize the model
model = CoralClassifier().to(device)

# Load the saved model parameters
model.load_state_dict(torch.load('coral_classifier.pth', map_location=device))
model.eval()  # Set the model to evaluation mode
print("Model loaded from coral_classifier.pth")

# Define the same transformations used during training, with an additional conversion to RGB
transform = transforms.Compose([
    transforms.Lambda(lambda img: img.convert('RGB')),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to make a prediction on a new image
def predict_image(image_path, model):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0).to(device)
    model.eval()
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    return 'Healthy' if predicted.item() == 0 else 'Bleached'


image_path = "/Users/youssefghaleb/Desktop/BleachedCorals_and_HealthyCoralsClassification/Validation/healthy_corals/3410650980_f13539931c_o_0_9671_0_551.jpg"
prediction = predict_image(image_path, model)
print(f"The coral in the image is: {prediction}")




