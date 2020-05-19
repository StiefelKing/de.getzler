import configparser
import os

config = configparser.ConfigParser()
config.sections()
config.read(os.environ['Appdata'] + "\\Arnotop\\Arnotop.ini")
print(config.sections())
