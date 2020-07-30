from horus_app import create_app
from flask_cors import *

app = create_app('config')
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(PORT=5000, HOST="0.0.0.0")
