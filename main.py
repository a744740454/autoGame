import yaml
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Initialize the Flask app and the database
def load_config(config_path='config/prod.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def get_mysql_uri(config):
    mysql_config = config['mysql']
    return f"mysql://{mysql_config['username']}:{mysql_config['password']}@{mysql_config['host']}/{mysql_config['database']}"


app = Flask(__name__)

config = load_config()

app.config['SQLALCHEMY_DATABASE_URI'] = get_mysql_uri(config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Route to get all game accounts


if __name__ == '__main__':
    app.run(debug=True,port=8898)
