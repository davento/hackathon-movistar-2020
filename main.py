import recognition
import os

to_detect = []
i = 1

for file in os.listdir('img/fachada'):
    to_detect = [{"_file": "img/fachada/"+str(file), "noresize": True}]
    recognition.recognition_facade(to_detect, i)
    i += 1
# to_detect = [{"_file": "img/CINTILLO_030.jpg", "noresize": True}]
# print(to_detect)