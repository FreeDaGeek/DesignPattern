#data objects
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        luke = character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "Tattooine"

        leia = character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = 26
        leia.home_planet = "Alderan"

        yoda =character()
        yoda.name = "Master Yoda"
        yoda.profession = "Jedi Knight"
        yoda.age = 762
        yoda.home_planet = "Dagobah"

        chars = [luke,leia,yoda]
        print chars[0].profession


class character(object):
    def __init__(self): #construtor function
        self.name = ""
        self.age = 0
        self.profession = ""
        self.home_planet = ""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
