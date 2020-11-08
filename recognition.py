from ximilar.client import DetectionClient
import json

def get_recognition_client():
    client = DetectionClient("e8d6294050a77bf31f56ad9e3e3e321706e64949")
    return client

def detect(detection_task, status, object_name, to_detect, i):
    result = detection_task.detect(to_detect)
    objects = result['records'][0]['_objects']
    if (len(objects) == 0):
        print("Imagen " + str(i) + ": " + object_name + " no se encontró.")
    else:
        print("Imagen " + str(i) + ": " + object_name + " se encontró.")

def recognition_facade(to_detect, i):
    client = get_recognition_client()
    detection_task, status = client.get_task("47df802e-7d28-4743-af70-767a9e4bc582")
    detect(detection_task, status, "la fachada", to_detect, i)

def recognition_band(to_detect, i):
    client = get_recognition_client()
    detection_task, status = client.get_task("47df802e-7d28-4743-af70-767a9e4bc582")
    detect(detection_task, status, "el cintillo", to_detect, i)