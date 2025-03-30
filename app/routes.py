from datetime import datetime
import json
from flask import render_template, request, redirect, url_for
from app import app
from requests import HTTPError
from app import config_module as conf


@app.route('/')
def index():    
    config = conf.loadConfig()
    
    return render_template('index.html', 
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
        )
    
@app.route('/init')
def test():
    config = conf.loadConfig()    
    
    return render_template('test.html', 
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
        )
    
@app.route('/objects')
def index():    
    config = conf.loadConfig()
    
    return render_template('index.html', 
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
        )


@app.route('/add', methods=['POST'])
def add():
    config = conf.loadConfig()
    input_text = request.form.get('input_field')
    return render_template('index.html', 
        now=datetime.now(),
        app_name = config['GENERAL']['app_name'],
    )

