from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'kurly.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcd\xc2\xc1\xb8\xfa\x85\xdd\xca\xf2\x89@\xa4\xc20r\xf6'