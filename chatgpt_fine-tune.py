import os
import openai
import json
import shutil
from openai import cli
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_summary(title):
    response = requests.get(f"https://en.wikipedia.org/wiki/{title}")
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find('div', {'class': 'noarticletext'}):
        return None
    else:
        return soup.select_one('div.mw-parser-output p').text.split('.')[0] + '.'

sample_data = []
for i in range(50):
	while True: 
         title = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnlimit=1&rnnamespace=0").json()["query"]["random"][0]["title"]
         summary = get_summary(title)
         if summary:
             break
	sample_data.append({"prompt": title, "completion": " " + summary})
        
training_file_name = 'training.jsonl'
validation_file_name = 'validation.jsonl'

# print(sample_data)

# Generate the training dataset file.
print(f'Generating the training file: {training_file_name}')
with open(training_file_name, 'w') as training_file:
    for entry in sample_data:
        json.dump(entry, training_file)
        training_file.write('\n')

# Copy the validation dataset file from the training dataset file.
# Typically, your training data and validation data should be mutually exclusive.
# For the purposes of this example, we're using the same data.
print(f'Copying the training file to the validation file')
shutil.copy(training_file_name, validation_file_name)

def check_status(training_id, validation_id):
    train_status = openai.File.retrieve(training_id)["status"]
    valid_status = openai.File.retrieve(validation_id)["status"]
    print(f'Status (training_file | validation_file): {train_status} | {valid_status}')
    return (train_status, valid_status)

# Upload the training and validation dataset files to Azure OpenAI.
training_id = cli.FineTune._get_or_upload(training_file_name, True)
validation_id = cli.FineTune._get_or_upload(validation_file_name, True)