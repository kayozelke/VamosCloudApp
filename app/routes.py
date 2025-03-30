from datetime import datetime
import json
from flask import render_template, request, redirect, url_for
from app import app
from requests import HTTPError


@app.route('/')
def index():
    return render_template('index.html', 
            now=datetime.now()
        )
    
@app.route('/test')
def test():
    return render_template('test.html', 
            now=datetime.now()
        )


@app.route('/add', methods=['POST'])
def add():
    input_text = request.form.get('input_field')
    return render_template('index.html', 
        now=datetime.now()
    )

