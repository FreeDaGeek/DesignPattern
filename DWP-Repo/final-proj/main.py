'''
Free Rosas

'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


      #this class shows the data
class BeerView(object):
    def __init__(self):
        pass




class BeerModel(object):
    def __init__(self):
        pass



class BeerData(object):
    def __init__(self):
        pass




class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Weather App</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self._body = '<h1>Beer Finder</h1>'
        self._close = '''
    </body>
</html>'''






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)




