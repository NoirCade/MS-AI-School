# Computer Vision Object Dectection
# Computer Vision API를 사용해서 이미지속에 있는 사물을 인식하는 데모 입니다.

# 네트워크 통신을 위해서 requests 패키지를 import 합니다.

from re import sub
import requests

# 이미지처리를 위해서 matplotlib.pyplot, Image, BytesIO 세 개의 패키지를 import 합니다.
# matplotlib.pyplot는 import 할 때 시간이 조금 걸릴 수 있습니다.

import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import json
import env1

# Subscription Key와 접속에 필요한 URL을 설정합니다.

analyze_url = env1.vision_base_url + 'analyze'

# 분석에 사용되는 이미지를 확인 합니다.

image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdW25Qs-ASGq9Le4mHAWrdm41uaRMpnNy2gg&usqp=CAU'
con = requests.get(image_url).content
byte = BytesIO(con)
image = Image.open(byte)

# 한줄로 작성시 image = Image.open(BytesIO(requests.get(image_url).content))

headers = {'Ocp-Apim-Subscription-key': env1.subscription_key}
params  = {'visualFeatures': 'Categories,Description,Color'} # 띄어쓰기 하면 안됨;
data = {'url': image_url}

response = requests.post(analyze_url, headers = headers, params = params, json = data) #get or post

result = response.json()

# print(result) #result 내용을 json 형태로 표시함

image_caption = result['description']['captions'][0]['text']

# print(image_caption)
# 이미지에 대한 간단한 설명만 출력!

# Object Detection

objectDetection_url = env1.vision_base_url + 'detect'

image_url2 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyDNKi6WBrnQ4GIK0VUm648Rpbqp063CMSlw&usqp=CAU'
image2 = Image.open(BytesIO(requests.get(image_url2).content))

headers2 = {'Ocp-Apim-Subscription-key': env1.subscription_key}
params2  = {'visualFeatures': 'Categories,Description,Color'} # 띄어쓰기 하면 안됨;
data2 = {'url': image_url2}

response2 = requests.post(objectDetection_url, headers = headers2, params = params2, json = data2)

result2 = response2.json()

print(result2)

from PIL import Image, ImageDraw, ImageFont

draw = ImageDraw.Draw(image2)

#범위 지정이나 설명 등은 자주 쓰는 기능이 될 것이므로 별도의 함수로 지정
def DrawBox(detectData):
    objects = detectData['objects']
    
    for obj in objects:
        # print(obj)

        rect = obj['rectangle']
        print(rect)

        x = rect['x']
        y = rect['y']
        w = rect['w']
        h = rect['h']

        draw.rectangle(((x,y),(x+w,y+h)),outline='red')

        objectName = obj['object']
        draw.text((x,y),objectName,fill='red')

DrawBox(result2)