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


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_mysql_uri(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # 注册 Blueprint
    from view.accounts import accounts_bp
    app.register_blueprint(accounts_bp)

    return app


config = load_config()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8898)
