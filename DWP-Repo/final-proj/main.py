'''
Free Rosas

'''
import webapp2
import urllib2
import json
#from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zipcode'], ['submit', 'submit']]

        if self.request.GET:
            #creates our model
            sm =SchoolModel()
            sm.school = self.response.GET['school']
            sm.call_api()

            #creates out view
            sv = SchoolView()
            #takes data object from model class and give it to view
            sv.bdos = sm.dos
            p._body = sv.content

        self.response.write(p.print_out())

      #this class shows the data
class SchoolView(object):
    def __init__(self):
        self.__sdos =[]
        self.__content = '<br/>'

    def update(self):
        for do in self.__bdos:
            pass




class SchoolModel(object):
    def __init__(self):
        self.__url ='http://code.org/schools.json'
        self.__school_type = ''
        self.__school_name = ''
        self.__jsondoc = ''


    def __call_api(self):
        request = urllib2.Request(self.__url + self.__school_type + self.__school_name)
        opener = urllib2.build_opener()
        results = opener.open(request)

        #parse data w/ json
        jsondoc = json.load(results)

        name = jsondoc['name']
        condition = jsondoc['weather'][0]['description']

        self.response.write("School Found: " + name + "<br/>"+condition)



class SchoolData(object):
    def __init__(self):
        pass




class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Find My </title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self._body = '<h1>Schools near by</h1>'
        self._close = '''
    </body>
</html>'''


def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'

        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):

        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]

            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            except:
                self._form_inputs += '" />'

    def print_out(self):
        return self._head + "Local School Found"+ self._form_open + self._form_inputs + self._form_close + self._body + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
