#data objects
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class character(object):
    def __init__(self): #construtor function
        self.name = ""
        self.age = 0
        self.profession = ""
        self.home_planet = ""
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
