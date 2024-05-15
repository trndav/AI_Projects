# Need fixing, not working
# Basic Transcription with Whisper
# pip install git+https://github.com/openai/whisper.git

import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
#result = model.transcribe("audio_example.mp3")
result = model.transcribe("test_audio.mp3")

# Output the transcription
print(result["text"])