
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #the fuction that starts everything
        #between the doctype is html and css/style
        page_head = '''

<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href='http://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Poiret+One' rel='stylesheet' type='text/css'>
        <style>

        html{
            background-color:#2D232C;
            width:100%;
            height:100%;
            font-family:helvetica;

            }

            body {
                width:600px;
                margin: 0 auto;
                background-color:#2D232C;

            }

            h1 {
                font-family:lobster;
            }

            h2, h3{
            font-family: Poiret One;
            }

            .box{
                background-color:#D1AA4F;
                margin: 0 auto;
                padding:15px;
                margin-top:25%;
                -webkit-border-radius: 40px;
                -moz-border-radius: 40px;
                border-radius: 40px;
                }

            form {
                margin: 0 auto;

                width:75%;
                background-color:#F0E0D1;
                font-family:'Poiret One', cursive;
                font-size:14px;
                padding:10px;
                -webkit-border-radius: 20px;
                -moz-border-radius: 20px;
                border-radius: 20px;
            }

            option{
            font-family: 'Poiret One', cursive;
            }

            form h2{
            font-family:lobster;
            }

            input{
            font-family: 'Poiret One', cursive;

            }
            button{
            width:100px;
            height:20px;
            margin-left: 15px;
            padding-bottom:10px;
            font-family: 'Poiret One', cursive;
            text-align:center;

            }



        </style>

    </head>
     <body>

     '''
        page_body ='''
        <div class="box">
        <h1>Fabulous Female Coders</h1>
        <h2>Welcome to the place for the overlooked.</h2>
        <h3>Stay updated on accomplishments of females in the coding world!</h3>

            <form method="GET" action="">
            <h2><b>Sign up for our newsletters</b></h2>
    <label>Name:</label>
    <input type="text" name="user" />
    <br/>
    <label>Email:</label>
    <input type="text" name="email" />
    <br/>
    <label>Send emails: </label>
    <select name="activity">
        <option value="daily">Daily</option>
        <option value="weekly">Weekly</option>
        <option value="bi-weekly">Bi-Weekly</option>
        <option value="monthly">Monthly</option>
    </select>
    <br/>
           <label class="pure-checkbox">
              <input type="checkbox" value="ready" name="ready" required><small><i>Terms and Conditions</i></small>
            </label>

    <br/>
    <button type="submit" value="Submit" />Submit</button>


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
