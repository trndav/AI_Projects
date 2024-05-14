# Optional
'''
pip3 install virtualenv 
virtualenv my_env # create a virtual environment my_env
source my_env/bin/activate # activate my_env
python3 -m pip install transformers==4.30.2 torch
'''

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model (download on first run and reference local installation for consequent runs)
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []
history_string = "\n".join(conversation_history)

input_text ="How are you doing?"

inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
print(inputs)

# explore the pretrained_vocab_files_map attribute. Provides a mapping of pretrained models to their corresponding vocabulary files.
# tokenizer.pretrained_vocab_files_map

# Raw, undecoded output
outputs = model.generate(**inputs)
print(outputs)

# Decoded output
response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
print("Response:", response)

# Update conversation history
conversation_history.append(input_text)
conversation_history.append(response)
print(conversation_history)

# Repeat
while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)
    # Get the input data from the user
    input_text = input("> ")
    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    # Generate the response from the model
    outputs = model.generate(**inputs)
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    print(response)
    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)