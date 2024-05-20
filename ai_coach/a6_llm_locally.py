# Simple chatbot

'''
You need to have watsonx_API and project_id for authentication when using the watsonx API.
Get the watsonx_API key https://eu-de.dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all%3Futm_source%3Dskills_network&utm_source_platform=medium&preselect_region=true
IBM API: https://cloud.ibm.com/iam/apikeys

'''

# pip install ibm-watson-machine-learning 
# you can also specifiy the package version such as 1.0.348

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods

# Set up the API key and project ID for IBM Watson 
watsonx_API = "" # below is the instruction how to get them
project_id= "" # like "0blahblah-000-9999-blah-99bla0hblah0"

generate_params = {
    GenParams.MAX_NEW_TOKENS: 250
}

model = Model(
    model_id = 'meta-llama/llama-2-70b-chat', # you can also specify like: ModelTypes.LLAMA_2_70B_CHAT
    params = generate_params,
    credentials={
        "apikey": watsonx_API,
        "url": "https://us-south.ml.cloud.ibm.com"
    },
    project_id= project_id
    )

q = "How to be happy?"
generated_response = model.generate(prompt=q)
print(generated_response['results'][0]['generated_text'])