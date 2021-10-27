import os
class Config ():
    REGISTERED_USERS = {
    'patel.pari.97@gmail.com':{"name":"Pari","password":"abc123"},
    }
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
