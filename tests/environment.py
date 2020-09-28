import configparser
import os

config = configparser.ConfigParser()
config.read(os.environ.get('api_env'))
api_host = config['api']['api_host']
api_port = config['api']['api_port']
