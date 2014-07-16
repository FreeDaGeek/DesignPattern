'''
Fridelande Rosas
07/10/2014
DWP
Assignment---
'''
import webapp2  #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #the fuction that starts everything
        page = '''<!DOCTYPE HTML>
<html>
    <head><title>Simple Form</title>
    </head>
     <body>
         <form method="GET">
           <label>Name: </label><input type="text" "name"="user" />
            <label>Email: </label><input type="text" "name"="email" />
            <input type="submit" value="Submit">
         </form>
     </body>
</html> '''

        if self.request.GET:
            #Stores details we got from the forms
            user = self.request.GET['user']
            email = self.request.GET['email']

        self.response.write(page) #prints infromation.




#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
