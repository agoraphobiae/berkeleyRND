import os

DEBUG = True
ANALYTICS = False

CSRF_ENABLED = True
SECRET_KEY = 'c0a3a867444f3b764642727099c2b721'

# the md5 of someday-maybe-m

# OPENID_PROVIDERS = [
#     { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
#     { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#     { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#     { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#     { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# db config

# USERNAME = "admin"
# PASSWORD = "default"

# sqlite db sqlalchemy
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_LOC = "db/rnd.sqlite"
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE_LOC
SQLALCHEMY_ECHO = True # logs stderr

# migration setup, so upgrading the db doesn't require so much work
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')