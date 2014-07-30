
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text',  'Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out())

class Page(object): #borrowing stuff from the object class
    def __init__(self): #constuctor
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
    <title>Weather App</title>
    </head>
    <body>'''
        self._body = 'Weather-App'
        self._close = '''
    </body>
<html>'''

    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        #constructor function
        #Page.__init__()
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self._inputs = []
        self._form_inputs = ''
        #<label>First Name:</label><input type="text value="" name="first_name"/>
        # ['first_name, 'text','First Name']
        #<input type="text value="" name="last_name" placeholder="last Name>
        #<input type="submit" value="Submit />

    @property
    def inputs(self)


    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through mega array and create HTML input based on the info there.
        print arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item.. add it in..
           # if len(item) > 2:
            try:
                self._form_inputs +='" placeholder="' +item[2]+'" />'
            #otherwise.. end the tag
            except:
                self._form_inputs += ' " />'
        print self._form_inputs

    #Polymorphism Alert!  method overriding
    def _print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
