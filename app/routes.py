from datetime import datetime
import os
# import json
# from requests import HTTPError
from flask import render_template, request, redirect, url_for
from app import app
from app import config_module as conf
from app import database_module as db

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
    
        db_engine = db.get_engine(
            username = config['DATABASE']['username'],
            password = config['DATABASE']['password'],
            host     = config['DATABASE']['host'],
            port     = config['DATABASE']['port'],
            database = config['DATABASE']['database']
        )
        db.check_and_create_tables(db_engine)
        
        # current dir
        directory = os.path.dirname((os.path.abspath(__file__)))
        # get to the parent of current dir
        directory = os.path.dirname(directory)
        
        # get to child dir
        directory = os.path.join(directory, 'datasrc')
        
        filepath = os.path.join(directory, 'music_dataset.csv')
        
        print(filepath)
        
        
        db.importTracksFromKaggle(db_engine,filepath)
        
        # return render_template('test.html', 
        #         now=datetime.now(),
        #         app_name = config['GENERAL']['app_name'],
        #     )
        return "<h2>Operation successfull!</h2>"
    
    
    except Exception as e:
        print(f"ERROR. '{type(e)}' : '{str(e)}'")
        return "<h2>Operation failed!</h2><p>Check console logs</p>"
        
    
    
    
@app.route('/objects')
def objects():    
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

