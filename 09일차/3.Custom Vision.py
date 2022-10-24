from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials
import os, time, uuid
import env3



credentials_Training = ApiKeyCredentials(in_headers={"Training-key": env3.training_key})
trainer = CustomVisionTrainingClient(env3.ENDPOINT_Training, credentials_Training)

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

credentials_Prediction = ApiKeyCredentials(in_headers={'Prediction-key': env3.prediction_key})
predictor = CustomVisionPredictionClient(env3.ENDPOINT_Prediction, credentials_Prediction)

target_image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiCfYeFRBUmW6gvlU2JvsQCcsrOFcJkBdDeA&usqp=CAU'
result = predictor.classify_image_url(project.id, 'greatwall', target_image_url)

for prediction in result.predictions:
  print('\t' + prediction.tag_name + ': {0:.2f}%'.format(prediction.probability * 100))