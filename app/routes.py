from datetime import datetime
import os
import json
import requests
from flask import render_template, request, redirect, url_for
from app import app
from app import config_module as conf

@app.route('/')
def index():    
    config = conf.loadConfig()
    
    return render_template('index.html', 
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
        )
    
@app.route('/init')
def init():
    try:
        config = conf.loadConfig()
        
        # current dir
        directory = os.path.dirname((os.path.abspath(__file__)))
        # get to the parent of current dir
        directory = os.path.dirname(directory)
        
        # get to child dir
        directory = os.path.join(directory, 'datasrc')
        
        filepath = os.path.join(directory, 'music_dataset.csv')
        
        print("Source filepath: ", filepath)
        
        return "Not implemented yet"
        
        return """
            <h2>Operation successfull!</h2>
            <p><a href="/">Return to main page</a></p>
        """
    
    
    except Exception as e:
        print(f"ERROR. '{type(e)}' : '{str(e)}'")
        return "<h2>Operation failed!</h2><p>Check console logs</p>"
        
    
    
    
@app.route('/tracks')
def tracks():    
    config = conf.loadConfig()
    
    url = f"{config['API']['url']}/objects"
    
    response = requests.get(
        url=url,
        headers={
            'Content-Type': 'application/json'
        },
        timeout=5
    )

    # print(response.json())
    # return "Not implemented yet"
    
    return render_template('objects.html', 
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
            tracks = response.json()
        )


@app.route('/add_track', methods=['POST'])
def add():
    config = conf.loadConfig()
    return "Not implemented yet"
    return render_template('index.html', 
        now=datetime.now(),
        app_name = config['GENERAL']['app_name'],
    )

