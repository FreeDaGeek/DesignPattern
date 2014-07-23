"""
Free Rosas
7/22/2014
DPW-01
What Does the Fox Say?
"""
import webapp2
#from animals import Panther, Dolphin, Fox

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #method array
        # self.response.write('Hello world!')

        #default html
        title = "What does the Fox Say?"
        css = "css/main.css"


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
