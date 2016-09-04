from flask import Flask
from config import secret_key, download_folder


#create application object
app = Flask(__name__)

app.config['DOWNLOAD_FOLDER'] = download_folder
app.secret_key = secret_key


from youtube import routes
