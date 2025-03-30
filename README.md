# VamosCloud App - Music Track Web App

VamosCloudApp is a web application serving as a graphical user interface (GUI) that interacts with an external API to manage and display music data. This project was developed as part of studies at the Poznan University of Technology.

# Features

* Track Overview: Display a list of all tracks available in the database.
* Track Details: View detailed information about a selected track. 
* Add Tracks: Use a form to add new tracks to the database. 
* Edit Tracks: Modify information of existing tracks.

# Requirements

* Python 3.x 
* [VamosCloudAPI](https://github.com/kayozelke/VamosCloudAPI)
* Flask: A micro web framework for Python. 
* Requests: A library for making HTTP requests in Python.

# Installation and Running

1. Clone the repository:
    ```bash 
    git clone https://github.com/kayozelke/VamosCloudApp.git 
    ```

2. Navigate to the project directory:
    ```bash
    cd VamosCloudApp
    ```

3. Configure `config.ini` file.

4. Run the application: 
    ```bash 
    python webserver.py 
    ```

The application will be available at `http://localhost:80/`.

# Project Structure

```bash
VamosCloudApp/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── routes.py
├── datasrc/
├── webserver.py
├── .gitignore
└── README.md
```
* `app/`: Main application directory containing static files, templates, and route definitions. 
* `datasrc/`: Directory intended for data sources used by the application. 
* `webserver.py`: File to run the application server. 

# Configuration

Before running the application, ensure that the config.py file contains the correct settings, such as the API URL that the application will communicate with.
