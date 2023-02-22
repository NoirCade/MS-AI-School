from torchvision import models
import torch
import torch.nn as nn
from PIL import ImageGrab
import cv2
import torch.nn.functional as F


def ingame_predic():

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    net = models.resnet50(pretrained=True)
    net.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=7, padding=3, bias=False)
    net.fc = nn.Linear(in_features=2048,out_features=5)

    net.load_state_dict(torch.load('./lastmodel580.pt'))
    net.to(device)
    net.eval()

    with torch.no_grad():
        # screen = np.array(ImageGrab.grab(bbox=(0, 40, 1024, 768))) # 1024, 768 화면을 받아서 Numpy Array로 전환
        screen = cv2.imread('./test_image.png') # test image
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (224, 224))

        output = net(screen)
        softmax_result = F.softmax(output)
        top_prob, top_label = torch.topk(softmax_result, 1)
        print(top_prob, top_label)

        if top_label == 'a':
            pass
        elif top_label == 'w':
            pass
        elif top_label == 'd':
            pass
        elif top_label == 's':
            pass
        elif top_label == 'n':
            pass

        return top_prob, top_label


if __name__ == '__main__':
    predic_prob, predic_label = ingame_predic()
    print(predic_prob, predic_label)
