
import webapp2#use the webapp2 library

class MainHandler(webapp2.RequestHandler): #delcaring a class
    def get(self): #function that starts everything. Catalyst
        page = '''<!DOCTYPE HTML>
<html>
    <head><title>Simple Login2</title></head>
    <body>
        <form method="GET">
           <a href=""?email=mickey@disney.com&user="Micky">Mickey Mouse</a><br/>
            <a href=""?email=Donald@disney.com>Donald Duck</a><br/>
            <a href=""?email=Petee@disney.com&userPete</a><br/>
           <a></a><br/>
           <a></a><br/>
           <a></a><br/>
            </form></body>
</html>'''
        self.response.out.write(page)
        #code goes here

#never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
