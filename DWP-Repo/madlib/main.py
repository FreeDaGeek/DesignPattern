'''
Free Rosas
07/10/2014
MadLib (Hey There Delilah-Remix)
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        print "Sorry Im not Sorry"
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)



