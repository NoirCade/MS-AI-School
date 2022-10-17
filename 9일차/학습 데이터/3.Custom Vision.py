from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

ENDPOINT = 'https://labuser36custom.cognitiveservices.azure.com/'

training_key = 'eb5358531509457298c63a4754fd65aa'
prediction_key = 'e942cbdb498c4bfdb7f0bff8541b4113'
prediction_resource_id = '/subscriptions/7ae06d59-97e1-4a36-bbfe-efb081b9b03b/resourceGroups/RG36/providers/Microsoft.CognitiveServices/accounts/labuser36custom'

publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

print("Creating project...")
project = trainer.create_project("labuser36 project")

Jajangmyeon_tag = trainer.create_tag(project.id, "Jajangmyeon")
Champon_tag = trainer.create_tag(project.id, "Champon")
Tangsuyook_tag = trainer.create_tag(project.id, "Tangsuyook")

import time

print('Training...')
iteration = trainer.train_project(project.id)
while (iteration.status != 'Completed'):
  iteration = trainer.get_iteration(project.id, iteration.id)
  print('Training status' + iteration.status)

  time.sleep(10)

print('Done!')