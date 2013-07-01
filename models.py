#!/usr/bin/python

from google.appengine.ext import db

class PhotoRecord(db.Model):
    date = db.StringProperty()
    photo = db.TextProperty()
    lon = db.StringProperty()
    lat = db.StringProperty()
    sender = db.StringProperty()    
    description = db.StringProperty()