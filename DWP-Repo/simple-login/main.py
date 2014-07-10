'''
Fridelande Rosas
07/10/2014
DWP
Assignment---
'''
import webapp2  #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #the fuction that starts everything
        self.response.write('Hello world!')
        #code goes here

    def additional_functions(self):
        pass
        #code goes here


#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
