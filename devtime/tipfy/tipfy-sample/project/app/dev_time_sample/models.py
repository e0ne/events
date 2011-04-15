from google.appengine.ext import db

class DevTime(db.Model):
    date = db.DateTimeProperty(auto_now=False)
    topics = db.StringListProperty()