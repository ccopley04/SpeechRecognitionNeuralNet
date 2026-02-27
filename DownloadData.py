import urllib.request
import os

url = "http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz"
filename = "speech_commands.tar.gz"

print("Starting download... this might take a minute.")
urllib.request.urlretrieve(url, filename)
print(f"Downloaded to {os.getcwd()}")

def download():
    print("Starting download... this might take a minute.")
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded to {os.getcwd()}")