from flask import Flask, render_template, redirect, url_for, request
import requests
import json
from services.API import *

app = Flask(__name__)

API_KEY = 'yQeg5Zes1SFKfd41x8dx1GEcOy8JrA'
GROUP_KEY = ''
HOST = 'http://44.192.111.58:8080'

@app.route('/')
def index():
    return redirect('/connect')

@app.route('/connect', methods = ['GET', 'POST'])

def connect():
    if(request.method == 'GET'):
        return render_template('login.html')
    if(request.method == 'POST'):
        jsonData = {'mail': request.form['mail'], 'pass': request.form['pass']}
        global GROUP_KEY
        GROUP_KEY = login('{}/?json=true'.format(HOST), jsonData)
        return render_template('detecttypes.html')

@app.route('/detecttypes', methods = ['GET', 'POST'])

def detectTypes():
    if(request.method == 'GET'):
        return render_template('detect-types.html')
    if(request.method == 'POST'):
        detecttypes = request.json
        setDetectTypes(HOST, detecttypes = detecttypes)
        return 'ok'

@app.route('/cameras')

def cameras():
    monitors = getMonitors('{}/{}/monitor/{}'.format(HOST, API_KEY, GROUP_KEY))
    return render_template('cameras.html', monitors = monitors, host = HOST)

@app.route('/camera/<mid>')

def securityCameras(mid):
    if(GROUP_KEY == ''):
        return redirect('/connect')
    else:
        mornitor = getMonitor('{}/{}/monitor/{}/{}'.format(HOST, API_KEY, GROUP_KEY, mid))
        src = HOST+mornitor[0]["streams"][0]
        return render_template('camera.html', monitor = mornitor, host = HOST, src = src)

if __name__ == '__main__':
    app.run(debug = True)