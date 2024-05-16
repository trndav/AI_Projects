import requests
url = "https://www.page.com/someaudiofile.mp3"
response = requests.get(url)
audio_file_path = "downloaded_audio.mp3"
with open(audio_file_path, "wb") as file:
    file.write(response.content)