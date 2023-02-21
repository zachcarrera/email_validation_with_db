from flask import Flask

app = Flask(__name__)

app.secret_key = "password"

DATABASE = "emails_schema"