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
    import csv
    
    try:
        config = conf.loadConfig()
        
        # current dir
        directory = os.path.dirname((os.path.abspath(__file__)))
        # get to the parent of current dir
        directory = os.path.dirname(directory)
        
        # get to child dir
        directory = os.path.join(directory, 'datasrc')
        
        csv_file_path = os.path.join(directory, 'music_dataset.csv')
        
        print("Source CSV filepath: ", csv_file_path)
        
        data = []
        
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row
            for i, row in enumerate(csv_reader):
                print(f"{i}. Collecting data ...")
                # get data
                data.append({
                    "song" : row[0],
                    "artist" : row[1],
                    "streams" : row[2],
                    "daily_streams" : row[3],
                    "genre" : row[4],
                    "release_year" : row[5],
                    "peak_position" : row[6],
                    "weeks_on_chart" : row[7],
                    "lyrics_sentiment" : row[8],
                    "tiktok_virality" : row[9],
                    "danceability" : row[10],
                    "acousticness" : row[11],
                    "energy" : row[12],
                })
                
        print(f"{i}. Inserting rows ...")
        
        url = f"{config['API']['url']}/object"
        
        response = requests.post(
            url=url,
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps(data),
        )
        
        response.raise_for_status()
                
        message = response.json()['message']
        
        
        return render_template('message.html',
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
            text = f"""
                <h2>Operation successfull!</h2>
                <p>Message: {message}</p>
                <p><a href="/">Return to main page</a></p>
            """
        )
        
        
    
    
    except Exception as e:
        print(f"ERROR. '{type(e)}' : '{str(e)}'")
        
        return render_template('message.html',
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
            text = "<h2>Operation failed!</h2><p>Check console logs</p>"
        )
        
@app.route('/delete_all')
def delete_all():
    config = conf.loadConfig()
    
    url = f"{config['API']['url']}/objects"
    
    response = requests.delete(
        url=url,
        headers={
            'Content-Type': 'application/json'
        }
    )
    
    try:
        if response.status_code == 200:
            message = response.json()['message']
        
            return render_template('message.html',
                now=datetime.now(),
                app_name = config['GENERAL']['app_name'],
                text = f"""
                    <h2>Operation successfull!</h2>
                    <p>Message: {message}</p>
                    <p><a href="/">Return to main page</a></p>
                """
            )
    
        response.raise_for_status()    
    except Exception as e:
        print(f"ERROR. '{type(e)}' : '{str(e)}'")
        
        return render_template('message.html',
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
            text = "<h2>Operation failed!</h2><p>Check console logs</p>"
        )
    
    
    
@app.route('/tracks')
def tracks():   
    print(f"{datetime.now().strftime('%H:%M:%S.%f')} - Tracks route called") 
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

@app.route('/add_track', methods=['GET'])
def add_track_form():
    config = conf.loadConfig()
    
    if request.args.get('id'):
        
        url = f"{config['API']['url']}/object"
        
        response = requests.get(
            url=url,
            headers={
                'Content-Type': 'application/json'
            },
            params={'id' : request.args.get('id')}
        )
        
        if response.status_code == 200:
            data = response.json()
            return render_template('add_track.html', 
                now=datetime.now(),
                app_name = config['GENERAL']['app_name'],
                update=True,
                data = data,
            )
        else:
            return render_template('message.html',
                now=datetime.now(),
                app_name = config['GENERAL']['app_name'],
                text = f"<h2>Operation failed!</h2><p>Track not found</p><p><a href='/'>Return to main page</a></p>"
            )

    
    return render_template('add_track.html', 
        now=datetime.now(),
        app_name = config['GENERAL']['app_name'],
    )

@app.route('/add_track', methods=['POST'])

def add_track():
    config = conf.loadConfig()
    
    try:
        # Extract data from the form
        track_data = {
            "song": request.form.get('song'),
            "artist": request.form.get('artist'),
            "streams": request.form.get('streams'),
            "daily_streams": request.form.get('daily_streams'),
            "genre": request.form.get('genre'),
            "release_year": request.form.get('release_year'),
            "peak_position": request.form.get('peak_position'),
            "weeks_on_chart": request.form.get('weeks_on_chart'),
            "lyrics_sentiment": request.form.get('lyrics_sentiment'),
            "tiktok_virality": request.form.get('tiktok_virality'),
            "danceability": request.form.get('danceability'),
            "acousticness": request.form.get('acousticness'),
            "energy": request.form.get('energy')
        }
        
        url = f"{config['API']['url']}/object"
        
        if request.form.get('_id', "") != "":
            # update field
            track_data['id'] = request.form.get('_id', "")
            
            response = requests.put(
                url=url,
                headers={
                    'Content-Type': 'application/json'
                },
                data=json.dumps(track_data),
            )
            
        else:
            # insert field
            response = requests.post(
                url=url,
                headers={
                    'Content-Type': 'application/json'
                },
                data=json.dumps([track_data]),
            )
        
        response.raise_for_status()
        
        message = response.json()['message']
        
        return render_template('message.html',
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
            text = f"""
                <h2>Operation successfull!</h2>
                <p>Message: {message}</p>
                <p><a href="/">Return to main page</a></p>
            """
        )
    
    except Exception as e:
        print(f"ERROR. '{type(e)}' : '{str(e)}'")
        
        return render_template('message.html',
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
            text = "<h2>Operation failed!</h2><p>Check console logs</p>"
        )


@app.route('/find_track', methods=['POST'])
def find_track():
    config = conf.loadConfig()

    try:
        # ...
        track_name = request.form.get('track_name')
        
        url = f"{config['API']['url']}/object"
        
        response = requests.get(
            url=url,
            headers={
                'Content-Type': 'application/json'
            },
            params={'name' : track_name, 'exact_match' : 'false'},
            timeout=5
        )
        
        if response.status_code == 200:
            return render_template('objects.html', 
                now=datetime.now(),
                app_name = config['GENERAL']['app_name'],
                tracks = [response.json()]
            )
        else:
            return render_template('message.html',
                now=datetime.now(),
                app_name = config['GENERAL']['app_name'],
                text = f"<h2>Operation failed!</h2><p>Track not found</p><p><a href='/'>Return to main page</a></p>"
            )

    
    except Exception as e:
        print(f"ERROR. '{type(e)}' : '{str(e)}'")
        return render_template('message.html',
            now=datetime.now(),
            app_name = config['GENERAL']['app_name'],
            text = "<h2>Operation failed!</h2><p>Check console logs</p>"
        )

