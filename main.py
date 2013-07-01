#!/usr/bin/env python
#
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from django.utils import simplejson as json

from models import PhotoRecord
from KML import KML

import base64


class MainHandler(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, {}))
        
class ImageServer(webapp.RequestHandler):
    def get(self):
        
        respKML = KML()          
        
        q = PhotoRecord.all()
        results = q.fetch(25)
        for p in results:
            
            # set up description
            #
            desc = " <![CDATA[ \
                <img src='http://ogmimage.appspot.com/content/" + \
                str(p.key().id()) + \
                "' width='250' height='200' />"            
            if p.description:
                desc += "<h2>Notlar</h2><p><b>" + p.description + "</b></p>"
            desc += "]]>"   
            
            if p.date:
                name = p.date
            else:
                name = "undef"
            
            respKML.addPlacemark(p.lat,p.lon,description = desc,name=name)
            
        respKML.close()
        
        self.response.headers["Content-Type"]= "application/vnd.google-earth.kml+xml"
        self.response.out.write(respKML.content)
        
    def post(self):
        
        pack = json.loads(self.request.body)
        
        r = PhotoRecord()
        
        r.lon = pack["lon"]
        r.lat = pack["lat"]
        r.photo = pack["photo"]
        r.sender = pack["sender"]
        r.date = pack["date"]
        r.description = pack["description"]

        
        r.put()
        
        self.response.out.write(json.dumps(pack))
        
class ContentServer(webapp.RequestHandler):
    def get(self,id):

        r = PhotoRecord.get_by_id(int(id))
        imStr = r.photo
        image = base64.b64decode(imStr)
    
        self.response.headers["Content-Type"] = "image/jpeg"
        self.response.out.write(image)

        


def main():
    application = webapp.WSGIApplication([
        ('/', MainHandler),
        ('/imageServer',ImageServer),
        ('/content/(.*)',ContentServer)],
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
