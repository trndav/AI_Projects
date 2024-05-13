# Creates caption for given image

# Optional create virtual environment
# pip3 install virtualenv 
# virtualenv my_env # create a virtual environment my_env
# source my_env/bin/activate # activate my_env
# # installing required libraries in my_env
# pip install langchain==0.1.11 gradio==4.21.0 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1

import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image, DONT FORGET TO WRITE YOUR IMAGE NAME
img_path = "reading_book.jpg"
# convert it into an RGB format 
image = Image.open(img_path).convert('RGB')

# You do not need a question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate a caption for the image. (unpack inputs, token length)
outputs = model.generate(**inputs, max_length=50)

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)