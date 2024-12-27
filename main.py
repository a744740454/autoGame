import pymysql
import yaml
from flask import Flask
from flask_migrate import Migrate

from models import db

# Install pymysql as MySQLdb
pymysql.install_as_MySQLdb()


def load_config(config_path='config/prod.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def get_mysql_uri(config):
    mysql_config = config['mysql']
    url = f"mysql://{mysql_config['username']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}"
    print(url)
    return url


def create_app(config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_mysql_uri(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化 SQLAlchemy 和 Migrate
    db.init_app(app)
    migrate = Migrate(app, db)  # 添加这一行来初始化 Migrate

    # 注册 Blueprint 等
    from view.accounts import accounts_bp
    from view.idCard import id_card_bp
    app.register_blueprint(accounts_bp)
    app.register_blueprint(id_card_bp)

    return app


# 加载配置文件
config = load_config()

app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8898)
