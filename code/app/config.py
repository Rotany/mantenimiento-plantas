class Config(object):
    SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://nani:example@localhost:5555/plantas'


