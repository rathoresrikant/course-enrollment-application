import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xfc\x9e\x04\xde\xc5om0\xfa\xd6H\xad\x89f\x13z'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }


    