import configparser
import os

config = configparser.ConfigParser()
dir_path = os.path.dirname(os.path.realpath(__file__))

config.read(dir_path + '../config/auth')

consumer_key =         config['twitter']['c_key']
consumer_secret =      config['twitter']['c_secret']
access_token_key=api = config['twitter']['a_key']
access_token_secret =  config['twitter']['a_secret']
