
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #the fuction that starts everything
        page_head = '''

<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
     <body>
     '''
        page_body ='''
            <form method="GET" action="">
                <label>Name: </label><input type="text" "name"="user" />
                <label>Email: </label><input type="text" "name"="email" />
                <input type="submit" value="Submit" />
            </form>
            '''

        page_close = '''
     </body>
</html>
'''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #prints infromation.

#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
