'''
Fridelande Rosas
7/31/2014
Final Project: Api
'''
import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        #makes the page load correctly w/ GET
        if self.request.GET:
            pass

#the View
class MovieView(object):
    '''This class deals with how the data will be seen by the user '''
    def __init__(self):
        pass


#the Model
class MovieModel(object):
    '''this model works with the info by fetching and parsing and sorting'''
    def __init__(self):
        pass



#The Data - stores info
class MovieData(object):
    def __init__(self):
        pass


#Page template
class Page(object):
    def __init__(self):
        pass


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
