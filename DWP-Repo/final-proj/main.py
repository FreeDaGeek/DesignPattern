'''
Free Rosas

'''
import webapp2
import urllib2
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zipcode'], ['submit', 'submit']]
        self.response.write(p.print_out())

        if self.request.GET:
            #get info from API
            zip = self.request.GET['zip']
            url = "http://code.org/schools.json" + zip
            #request being assembled
            request = urllib2.Request(url)
            #urllib2 creates an object to get the url
            opener = urllib2.build_opener()
            #the url to open the result
            result = opener.open(request)

            #parse w/JSON
            jsondoc = json.load(result)
            self.response.write(jsondoc)
'''
#sm.call_api()
#creates out view
#sv = SchoolView()
#takes data object from model class and give it to view


            sv.sdos = sm.dos
            p._body = sv.content

        self.response.write(p.print_out())

      #this class shows the data
class SchoolView(object):
    def __init__(self):
        self._sdos = []
        self.__content = '<br/ >'

    def update(self):
        for do in self.__sdos:
            self.__content += " Name: "+do.name

    @property
    def content(self):
        return self.__content

    @property
    def sdos(self):
        pass

    @sdos.setter
    def sdos(self, arr):
        self.__sdos = arr
        self.update()


class SchoolModel(object):
    def __init__(self):
        self.__url = 'http://code.org/schools.json' + zip
        self.__school_contact_name = ''
        self.__school_website = ''
        self.__school_levels = ''
        self.__school_contact_number = ''
        self.__school_website = ''
        self.__jsondoc = ''

    def call_api(self):

#request = urllib2.Request(self.__url + self.__school_levels + self.__school_contact_number + self.__school_website + self.__school_contact_name)

#opener = urllib2.build_opener()

#result = opener.open(request)

        #parse data w/ json
        self.__jsondoc = json.load(result)

        name = jsondoc['schools'][0]['name']
        sitelink = jsondoc['schools'][0]['website']

        #self.response.write("School Found: " + name + "<br/>"+sitelink)



class SchoolData(object):
    def __init__(self):
        self.title = ''
        self.href = ''
        self.school

'''

class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Schools</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self._body = '<p>Schools near by</p>'
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
        #changes privates into var
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            except:
                self._form_inputs += '" />'

    def print_out(self):
        return self._head + "<h1>Local School Found: </h1>"+ self._form_open + self._form_inputs + self._form_close + self._body + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
