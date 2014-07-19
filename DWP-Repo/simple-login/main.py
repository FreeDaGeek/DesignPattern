
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #the fuction that starts everything
        #between the doctype is html and css/style
        page_head = '''

<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <style>

            body {
                width:600px;
                background-color:teal;
            }

            h1 {
                font-family:helvetica;
            }

            form {
                margin: 0 auto;
                width:450px;
                background-color:gold;
                font-family: helvetica;
                margin-top:25px;
                padding:10px;

            }

            option {

                margin: 15px;

            }

            input {

                height: 20px;
                width: 150px;
                margin:3%;
                border-radius: 8px;
                -moz-border-radius: 8px;
                -khtml-border-radius: 8px;
                -webkit-border-radius: 8px;

            }

            .tc {
                width: 200px;
                height: 30px;
                margin-left:10px;
                padding-bottom:10px;
            }

            .tc label {

            }
        </style>

    </head>
     <body>
     '''
        page_body ='''
            <form method="GET" action="">
    <label>Name:</label>
    <input type="text" name="user" />
    <br/>
    <label>Email:</label>
    <input type="text" name="email" />
    <br/>
    <label>Send me emails..</label>
    <select name="activity">
        <option value="daily">Daily</option>
        <option value="weekly">Weekly</option>
        <option value="bi-weekly">Bi-Weekly</option>
        <option value="monthly">Monthly</option>
    </select>
    <br/>
    <input type="submit" value="Submit" />
    <br/>
        <div class="tc">
            <label>
                <input type="checkbox" value="ready" name="ready" required/>Terms and Conditions
            </label>
         </div>
                '''

        page_close = '''
     </body>
</html>
'''
        if self.request.GET:# IF statement that gets the detail from the form
            user = self.request.GET['user']
            email = self.request.GET['email']
            activity = self.request.GET['activity']
            #the information printed on the details have been submitted
            self.response.write(page_head + page_close)
            self.response.write("FreeDaGeek <i><small>says...</small></i><br>")
            self.response.write("Thank you for signing up for"+ '  ' + activity + ' ' + "newsletters" + ' ' + user + "!<br>")
            self.response.write("Your subscription will be sent to" + ' ' + email + ".")
        else:
            self.response.write(page_head + page_body + page_close) #prints information.

#never touch this..Its magic
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
