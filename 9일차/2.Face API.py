import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

subscription_key = '9db30db7ded4443daede28de93c47a40'
face_api_url = 'https://labuser36face.cognitiveservices.azure.com/face/v1.0/detect'

#Class, library, Package는 관례상 대문자
#지역변수, 파라메타는 관례상 소문자
#addr, msg 줄임말은 배제
#두 단어가 합쳐지면 두 번쨰 단어는 대문자
#상수는 전체가 대문자  const MAX_USER=100

image_url = 'https://image.ajunews.com/content/image/2018/04/19/20180419161753124159.jpg'
image = Image.open(BytesIO(requests.get(image_url).content))

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceID': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender'
}

data = {'url': image_url}

response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()

draw = ImageDraw.Draw(image)

def DrawBox(faces):

  for face in faces:
    rect = face['faceRectangle']
    left = rect['left']
    top = rect['top']
    width = rect['width']
    height = rect['height']

    draw.rectangle(((left,top),(left+width,top+height)),outline='red')

    face_attributes = face['faceAttributes']
    smile = face_attributes['smile']
    draw.text((left, top), str(smile), fill='red')

    DrawBox(faces)