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
        self.geolocation = ''

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





