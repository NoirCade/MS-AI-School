from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

ENDPOINT_Training = 'https://labuser36custom.cognitiveservices.azure.com/'
ENDPOINT_Prediction = 'https://labuser36custom-prediction.cognitiveservices.azure.com/'

training_key = 'eb5358531509457298c63a4754fd65aa'
prediction_key = 'e942cbdb498c4bfdb7f0bff8541b4113'
prediction_resource_id = '/subscriptions/7ae06d59-97e1-4a36-bbfe-efb081b9b03b/resourceGroups/RG36/providers/Microsoft.CognitiveServices/accounts/labuser36custom'

credentials_Training = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT_Training, credentials_Training)

print("Creating project...")
project = trainer.create_project("labuser36 project")

Jajangmyeon_tag = trainer.create_tag(project.id, "Jajangmyeon")
Champon_tag = trainer.create_tag(project.id, "Champon")
Tangsuyook_tag = trainer.create_tag(project.id, "Tangsuyook")

print('Training...')
iteration = trainer.train_project(project.id)
while (iteration.status != 'Completed'):
  iteration = trainer.get_iteration(project.id, iteration.id)
  print('Training status' + iteration.status)

  time.sleep(10)

print('Done!')

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

credentials_Prediction = ApiKeyCredentials(in_headers={'Prediction-key': prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT_Prediction, credentials_Prediction)

target_image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiCfYeFRBUmW6gvlU2JvsQCcsrOFcJkBdDeA&usqp=CAU'
result = predictor.classify_image_url(project.id, 'greatwall', target_image_url)

for prediction in result.predictions:
  print('\t' + prediction.tag_name + ': {0:.2f}%'.format(prediction.probability * 100))