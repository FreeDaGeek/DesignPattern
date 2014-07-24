class Animals(object): #abstract class-- used as a template
    def __init__(self):
        #empty variable space for the sub classes to fill in
        self._phylum = ''
        self._classs = ''
        self._order = ''
        self._family = ''
        self._genus = ''
        self._image = ''
        self._lifespan = ''
        self._habitat = ''
        self._geolocation = ''

#template - html
        self._title = ''
        self._css = "css/style.css"
        self.head = """

<!DOCTYPE HTML>
<html>
    <head>
    <title>{self.title}</title>
    <link href ="{self.css}" rel="stylesheet" text/css=text/css/>
    </head>
    <body>
        """
        self.body = "What does the FOX say?" \
                   "<a href='/'><button>Return</button></a>" \
                   # "<a href='" + self.play_sound() + "'><button>Sound</button></a>"

        self.close = """
    </body>
</html> """

    def print_out(self):
        total = self._page_head + self._page_body + self._page_close
        total = total.format(**locals())
        return total  #print on page

    def play_sound(self):
        pass


class Panther(Animals):
    def __init__(self):
        super(Panther, self).__init__() #const. function -- super class

        self._title = "What does the Panther Say?"
        self._phylum = 'Chordata'
        self._classs = 'Mammalia'
        self._order = 'Carnivora'
        self._family = 'Felidae'
        self._genus = 'Puma'
        self._image = ''
        self._lifespan = '12 years in the wild'
        self._habitat = 'Wetland/Saw palmetto'
        self._geolocation = 'Florida- Everglades'
        self._list_open = "<h1>The Panther:</h1>"\
                          "<ul><li>Phylum: " + self._phylum + "</li>"\
                          "<li>Class: " + self._classs + "</li>"\
                          "<li>Order: " + self._order + "</li>"\
                          "<li>Family: " + self._family + "</li>"\
                          "<li>Genus: " + self._genus + "</li>"\
                          "<li>Image: " + self._image + "</li>"\
                          "<li>Lifespan: " + self._lifespan + "</li>"\
                          "<li>Habitat: " + self._habitat + "</li>"\
                          "<li>Geolocation: " + self._geolocation + "</li>"\

        self.list_close = "</ul>"












