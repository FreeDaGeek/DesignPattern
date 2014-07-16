
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
                <label>Name: </label><input type="text" name="user" /><br/>
                <label>Email: </label><input type="text" name="email" /><br/>

                <label>Send me emails..</label>
                <select name="email_options" name="send">
                    <option value="daily">Daily</option>
                    <option value="weekly">Weekly</option>
                    <option value="bi-weekly">Bi-Weekly</option>
                    <option value="monthly">Monthly</option>
                </select><br/>

                 <label>Newsletter Topics</label><br/><input type="checkbox" names= "topics" value="New in tech">Tech New Update<br/>
                  <input type="checkbox" names= "topics" value="Design Inspiration">Design Inspiration<br/>
                 <input type="checkbox" names= "topics" value='Cool Codes "Cracked'>Cool Codes: "Cracked!"
                   <label>
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
            send = self.request.GET['send']
            self.response.write(page_head + user + ' ' + email + ' ' + send + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #prints infromation.

#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
