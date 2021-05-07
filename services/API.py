import requests
import json

def login(url, jsonData):
    res = requests.post(url = url, json = jsonData)
    return json.loads(res.content)['$user']['ke']

def getMonitors(url):
    res = requests.get(url = url)
    return json.loads(res.content)

def getMonitor(url):
    res = requests.get(url = url)
    return json.loads(res.content)

def setDetectTypes(url, detecttypes):
    # res = requests.post(url = url, json = detecttypes)
    # return res.content
    return 'ok'