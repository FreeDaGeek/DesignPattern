'''
Free Rosas
07/10/2014
MadLib (Hey There Delilah-Remix)
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!M')
        print "Sorry Im not Sorry"
        music = dict()
        music = {"Band": "Plain White T's",
         "Song": "Hey There Delilah",
         "Album": "All That We Needed"}

        print "Help me learn the lyrics to " + music["Band"] + "Lyrics to " + music["Song"]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)



