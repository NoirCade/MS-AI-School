import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

subscription_key = 'a6523245b14a49a5988ab0de93c70f0a'
vision_base_url = 'https://labuser36coumputervision.cognitiveservices.azure.com/vision/v2.0/'
ocr_url = vision_base_url + 'ocr'

image_url = 'https://popperfont.files.wordpress.com/2011/12/nothing-exists.jpg'

image = Image.open(BytesIO(requests.get(image_url).content))

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'ukn', 'detectOrientation': 'true'}
data = {'url': image_url}