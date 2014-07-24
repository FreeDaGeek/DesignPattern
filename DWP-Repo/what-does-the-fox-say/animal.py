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
        self._page_head = """

<!DOCTYPE HTML>
<html>
    <head>
    <title>{self.title}</title>
    <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self._page_body = "What does the FOX say?" \
                   "<a href='/'><button>Return</button></a>" \
                   # "<a href='" + self.play_sound() + "'><button>Sound</button></a>"

        self._page_close = """
    </body>
</html> """

    def print_out(self):
        total = self._page_head + self._page_body + self._page_close
        total = total.format(**locals())
        return total
        #print on page

    def play_sound(self):
        pass

#panther's info
class Panther(Animals):
    def __init__(self):
        super(Panther, self).__init__() #const. function -- super class

        #data for the empty var in the super class above
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

        self._list_close = "</ul>"

    def play_sound(self):
        pass

    def print_out(self):
        total = self._page_head + self._page_body + self._list_open + self._list_close + self._page_close
        total = total.format(**locals())
        return total


#dolphin's info
class Dolphin(Animals):
    def __init__(self):
        super(Dolphin, self).__init__() #const. function -- super class

        #data for the empty var in the super class above
        self._title = "What does the Dolphin Say?"
        self._phylum = 'Chordata'
        self._classs = 'Mammalia'
        self._order = 'Cetacea'
        self._family = 'Odontaceti'
        self._genus = 'Delphinidae'
        self._image = ''
        self._lifespan = 'Up to 20 years'
        self._habitat = 'Water'
        self._geolocation = 'Throughout the oceans'
        self._list_open = "<h1>The Dolphin:</h1>"\
                          "<ul><li>Phylum: " + self._phylum + "</li>"\
                          "<li>Class: " + self._classs + "</li>"\
                          "<li>Order: " + self._order + "</li>"\
                          "<li>Family: " + self._family + "</li>"\
                          "<li>Genus: " + self._genus + "</li>"\
                          "<li>Image: " + self._image + "</li>"\
                          "<li>Lifespan: " + self._lifespan + "</li>"\
                          "<li>Habitat: " + self._habitat + "</li>"\
                          "<li>Geolocation: " + self._geolocation + "</li>"\

        self._list_close = "</ul>"

    def play_sound(self):
        pass

    def print_out(self):
        total = self._page_head + self._page_body + self._list_open + self._list_close + self._page_close
        total = total.format(**locals())
        return total


#fox's info
class Fox(Animals):
    def __init__(self):
        super(Fox, self).__init__() #const. function -- super class
        #data for the empty var in the super class above
        self._title = "What does the Fox Say?"
        self._phylum = 'Chordata'
        self._classs = 'Mammalia'
        self._order = 'Carnivora'
        self._family = 'Canidae'
        self._genus = 'Vulpes'
        self._image = ''
        self._lifespan = '10 years in the wild'
        self._habitat = 'Forest, deserts, grassland, mountains'
        self._geolocation = 'All continent expect Antarctica'
        self._list_open = "<h1>The Dolphin:</h1>"\
                          "<ul><li>Phylum: " + self._phylum + "</li>"\
                          "<li>Class: " + self._classs + "</li>"\
                          "<li>Order: " + self._order + "</li>"\
                          "<li>Family: " + self._family + "</li>"\
                          "<li>Genus: " + self._genus + "</li>"\
                          "<li>Image: " + self._image + "</li>"\
                          "<li>Lifespan: " + self._lifespan + "</li>"\
                          "<li>Habitat: " + self._habitat + "</li>"\
                          "<li>Geolocation: " + self._geolocation + "</li>"\

        self._list_close = "</ul>"

    def play_sound(self):
        pass

    def print_out(self):
        total = self._page_head + self._page_body + self._list_open + self._list_close + self._page_close
        total = total.format(**locals())
        return total #print info on the page
