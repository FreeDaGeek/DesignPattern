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
        array = ["Panther()", "Dolphin()", "Fox()"]
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
                             "<a href=?animals=" + array[0] + "><button class='first'>Panther</button>" \
                             "<a href=?animals=" + array[1] + "><button class='second'>Dolphin</button>" \
                             "<a href=?animals=" + array[2] + "><button class='third'>Fox</button>" \
                     ""
        page_close = """
        </div>
        </body>
    </html>"""


    




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
