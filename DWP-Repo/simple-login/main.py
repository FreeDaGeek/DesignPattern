'''
Fridelande Rosas
07/10/2014
DWP
Assignment---
'''
import webapp2  #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #the fuction that starts everything
        page = '''
        <!DOCTYPE HTML>
<html>
    <head><title>Welcome!</title>
    </head>
     <body> Hello to Everyone!
     </body>
</html>
        '''
        self.response.write('Hello world!')




#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
