import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xda\x0cx\xcf\xd1Qsf\x05,\xddI\xa7\x84}B\xca\x97\xe0Qo\xe7T\xdd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import thermos.models
import thermos.views
