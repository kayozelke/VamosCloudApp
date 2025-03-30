import os
from app import app

import argparse

parser = argparse.ArgumentParser(description='Run the Flask application.')
parser.add_argument('-p','--port', type=int, default=80, help='Port to run the application on.')
parser.add_argument('-d','--debug', action='store_true', help='Enable debug mode.')
args = parser.parse_args()

# -------------------- Start Flask server --------------------
if __name__ == '__main__':
    if args.debug:
        app.run(debug=True, port=int(os.environ.get('PORT', args.port)))
    else:
        app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', args.port)))

