import os

# Secret key needed to encode and decode token
SECRET_KEY = os.getenv('SECRET_KEY') or 'SECRET'
