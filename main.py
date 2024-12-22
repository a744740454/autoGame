import yaml
import pymysql
from flask import Flask
from models import db
# Install pymysql as MySQLdb
pymysql.install_as_MySQLdb()

# Initialize the Flask app and the database

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

    # 在这里初始化 SQLAlchemy，确保它与 Flask 应用实例关联
    db.init_app(app)

    # 延迟导入 Blueprint，避免循环导入
    from view.accounts import accounts_bp
    app.register_blueprint(accounts_bp)

    return app


# 加载配置文件
config = load_config()

if __name__ == '__main__':
    app = create_app(config)
    app.run(debug=True, host='0.0.0.0', port=8898)
