import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

subscription_key = 'a6523245b14a49a5988ab0de93c70f0a'
vision_base_url = 'https://labuser36coumputervision.cognitiveservices.azure.com/vision/v2.0/'
ocr_url = vision_base_url + 'ocr'

image_url = 'https://i.stack.imgur.com/WiDpa.jpg'

image = Image.open(BytesIO(requests.get(image_url).content))

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'unk', 'detectOrientation': 'true'}
data = {'url': image_url}

response = requests.post(ocr_url, headers=headers, params=params, json=data)

result = response.json()

for region in result['regions']:
  lines = region['lines']

  for line in lines:
    words = line['words']

    for word in words:
      print(word['text'])

image_url = "https://www.unikorea.go.kr/unikorea/common/images/content/peace.png"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'unk', 'detectOrientation': 'true'}
data = {'url': image_url}

#지원하는 언어목록
# unk (AutoDetect) zh-Hans (ChineseSimplified) zh-Hant (ChineseTraditional) cs (Czech)
# da (Danish) nl (Dutch) en (English) fi (Finnish) fr (French) de (German) el (Greek)
# hu (Hungarian) it (Italian) ja (Japanese) ko (Korean) nb (Norwegian) pl (Polish)
# pt (Portuguese, ru (Russian) es (Spanish) sv (Swedish) tr (Turkish) ar (Arabic)
# ro (Romanian) sr-Cyrl (SerbianCyrillic) sr-Latn (SerbianLatin) sk (Slovak)

response = requests.post(ocr_url, headers=headers, params=params, json=data)
result = response.json()

for region in result['regions']:
  lines = region['lines']

  for line in lines:
    words = line['words']

    for word in words:
      print(word['text'])