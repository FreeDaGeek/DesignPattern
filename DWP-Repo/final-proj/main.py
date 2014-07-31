'''
Free Rosas

'''
import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['beer', 'text', 'beer type'], ['submit', 'submit']]

        if self.request.GET:
            #creates our model
            bm =BeerModel()
            bm.beer = self.response.GET['beer']
            bm.call_api()

            #creates out view
            bv = BeerView()
            #takes data object from model class and give it to view
            bv.bdos = bm.dos
            p._body = bv.content

        self.response.write(p.print_out())

      #this class shows the data
class BeerView(object):
    def __init__(self):
        self.__bdos =[]
        self.__content = '<br/>'

    def update(self):
        for do in self.__bdos:
            pass




class BeerModel(object):
    def __init__(self):
        self.__url ='https://www.thebeerspot.com/api/'
        self.__beer_type = ''
        self.__beer_name = ''
        self.__xmldoc = ''


    def __call_api(self):
        request = urllib2.Request(self.__url + self.__beer_type + self.__beer_name)
        opener = urllib2.build_opener()
        results = opener.open(request)
        #parse data
        self.xmldoc = minidom.parse(results)
        list = self.__xmldoc = minidom.parse(results)
        self.dos = []






class BeerData(object):
    def __init__(self):
        pass




class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Find My Beer</title>
        <link href="css/main.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''

        self._body = '<h1>Beer Finder</h1>'
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
        return self._head + "Find My Beer!"+ self._form_open + self._form_inputs + self._form_close + self._body + self._close


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
