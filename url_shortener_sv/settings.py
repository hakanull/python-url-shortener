import os

#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')