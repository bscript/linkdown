from flask import Flask 

app = Flask(__name__)

#Avoid Circular importing
from app import views