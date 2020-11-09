from ximilar.client import DetectionClient
import json
import os

def get_recognition_client():
    client = DetectionClient("e8d6294050a77bf31f56ad9e3e3e321706e64949")
    return client

def detect(detection_task, status, object_name, to_detect, filename):
    result = detection_task.detect(to_detect)
    objects = result['records'][0]['_objects']
    if (len(objects) == 0):
        print(filename + ": " + object_name + " no se encontró.")
    else:
        print(filename + ": " + object_name + " se encontró.")

def recognition_facade(to_detect, filename):
    client = get_recognition_client()
    detection_task, status = client.get_task("47df802e-7d28-4743-af70-767a9e4bc582")
    detect(detection_task, status, "la fachada", to_detect, filename)

def recognition_band(to_detect, filename):
    client = get_recognition_client()
    detection_task, status = client.get_task("47df802e-7d28-4743-af70-767a9e4bc582")
    detect(detection_task, status, "el cintillo", to_detect, filename)

def analyze_facade(url):
    to_detect = []
    for file in os.listdir(url):
        to_detect = [{"_file": url + "/"+str(file), "noresize": True}]
        recognition_facade(to_detect, str(file))

def analyze_band(url):
    to_detect = []
    for file in os.listdir(url):
        to_detect = [{"_file": url + "/"+str(file), "noresize": True}]
        recognition_band(to_detect, str(file))

def image_comformity():
    analyze_facade("img/fachada")
    analyze_band("img/cintillo")