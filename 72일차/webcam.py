import cv2
from torchvision import models
from torchvision import transforms
from torch import nn
import torch


device = 'cuda' if torch.cuda.is_available() else 'cpu'

webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

# model
net = torch.hub.load('pytorch/vision:v0.10.0', 'vgg16', pretrained=True)
num_ftrs = net.classifier[6].in_features
net.classifier[6] = nn.Linear(num_ftrs, 6)


# 학습한 모델 불러오기
# models_loader_path = './weight/resnet.pt'
net.load_state_dict(torch.load('./models/vgg16_22.pt', map_location=device))
net.to(device)

val_transforms = transforms.Compose([
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    transforms.ToTensor()
])


def preprocess(image, device):
    from PIL import Image
    image = Image.fromarray(image)
    image = val_transforms(image)
    image = image.float()
    image = image.to(device)
    image = image.unsqueeze(0)

    return image


if not webcam.isOpened():
    print('카메라 열기 실패!!')
    exit()

while webcam.isOpened():
    status, frame = webcam.read()

    frame = cv2.flip(frame, 1)  # 화면 좌우 반전
    with torch.no_grad():
        if status:
            image = preprocess(frame, device=device)
            output = net(image)
            _, argmax = torch.max(output, 1)
            print('output', output)
            cv2.imshow('test', frame)

        if cv2.waitKey(1) & 0xFf == ord('q'):
            break

webcam.release()
cv2.destroyAllwindows()