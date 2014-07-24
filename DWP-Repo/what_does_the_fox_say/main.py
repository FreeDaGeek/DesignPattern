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
        animals = ["Panther()", "Dolphin()", "Fox()"]
        # self.response.write('Hello world!')

        #html
        title = "What does the Fox Say?"
        css = "css/main.css"
        page_head = """
<!DOCTYPE HTML>
    <html>
        <head><title>What Does the Fox Say?</title>
        <link href= rel="stylesheet type="text/css />
        </head>
        <body>
            """
        page_body = "" \
                    "<header><h1>Animal:</h1><header>" \
                        "<div class='info'>" \
                            "<button class='first'>Panther</button>" \
                            "<button class='second'>Dolphin</button>" \
                            "<button class='third'>Fox</button>" \
                    ""
        page_close = """
        </div>
        </body>
    </html>"""

        def print_out(self):
            return page_head + page_body + page_close



        #statment that get the the GET info on the page


        #gets the value of the animal and store it

        #request which class to connect to






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
