
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #the fuction that starts everything
        page_head = '''

<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <style>
            body{width:800px; margin: 0 auto; background-color:teal;}
            h1{font-family:cooper black;}
            form{width:400px;
                 font-family: helvetica;
                 margin-top:50px;
                 padding-left:10px;}

            input{margin-top:20px;
                  height: 22px;
                  weight: 30px;
                  outline:none;
                  border-radius:5px;
                  padding-left:10px;
                  }
        </style>

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
                 <input type="checkbox" value="ready" name="ready" required><small><i>Terms and Conditions</i></small><br/>
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

            self.response.write(page_head + page_close)
            self.response.write("FreeDaGeek <i><small>says...</small></i><br>")
            self.response.write("Thank you for signing up for"+ '  ' + activity + ' ' + "newsletters" + ' ' + user + "!<br>")
            self.response.write("Your subscription will be sent to" + ' ' + email + ".")

            #self.response.write("Welcome to TEAM AWESOME-SAUCE")
            #self.response.write("You signed up for" + '  ' + activity + "newsletters" + "to be sent to" + ' ' + email + "!")
        else:
            self.response.write(page_head + page_body + page_close) #prints information.

#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
