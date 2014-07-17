
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
                <select name="activity">
                    <option value="daily">Daily</option>
                    <option value="weekly">Weekly</option>
                    <option value="bi-weekly">Bi-Weekly</option>
                    <option value="monthly">Monthly</option>
                </select><br/>
                 <label>Newsletter Topics</label><br/>
                 <input type="checkbox" value="New in tech" name="tech">Tech New Update<br/>
                  <input type="checkbox" value="Design Inspiration" name="design">Design Inspiration<br/>
                 <input type="checkbox" value='Cool Codes "Cracked" name="code">Cool Codes: "Cracked!"
                   <label></br>
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
            activity = self.request.GET['activity']
            tech = self.request.GET['tech']
            design = self.request.GET['design']
            code = self.request.GET['code']
            self.response.write(page_head + user + ' ' + activity +' '+ email + ' '+ tech + design + code + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #prints infromation.

#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
