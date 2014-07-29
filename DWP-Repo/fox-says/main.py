"""
Fridelande Rosas
DPW
07/25/2014
What does the fox say
"""
import webapp2
from page import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
            p = Page()

            #Array for animal classes
            animals = [Panther, Dolphin, Fox]

            #sounds : panther, dolphin, fox
            panther = Panther()
            panther.sound = "Meeeooowww"

            dolphin = Dolphin()
            dolphin.sound = "Eeeeeik"

            fox = Fox()
            fox.sound = "Aaaooh"

            self.response.write(p.header + p.links)
            if self.request.GET:
                    details = int(self.request.get["animals"])

                    title = animals[details].title
                    phylum = animals[details].phylum
                    classs = animals[details].classs
                    order = animals[details].order
                    family = animals[details].family
                    genus = animals[details].genus
                    img = animals[details].img
                    lifespan = animals[details].lifespan
                    habitat = animals[details].habitat
                    geolocation = animals[details].geolocation
                    sound = animals[details].sound

                    #info will have all the information populated into 3 sections
                    info = '''<div id="info">
                    <h3>{title}</h3>
                            <section id="properties">
                                     <p class="labels"><strong>Phylum:</strong></p>
                                     <p class="labels"><strong>Class:</strong></p>
                                     <p class="labels"><strong>Order:</strong></p>
                                     <p class="labels"><strong>Family:</strong></p>
                                     <p class="labels"><strong>Genus:</strong></p>
                                     <p class="labels"><strong>Lifespan:</strong></p>
                                     <p class="labels"><strong>Habitat:</strong></p>
                                     <p class="labels"><strong>Geolocation:</strong></p>
                                     <p class="labels"><strong>Sound:</strong></p>
                            </section>

                            <section id="details">
                                     <p class="detail-info">{phylum}</p>
                                     <p class="detail-info">{classs}</p>
                                     <p class="detail-info">{order}</p>
                                     <p class="detail-info">{family}</p>
                                     <p class="detail-info">{genus}</p>
                                     <p class="detail-info">{lifespan}</p>
                                     <p class="detail-info">{habitat}</p>
                                     <p class="detail-info">{geolocation}</p>
                                     <p class="detail-info">{sound}</p>
                            </section>

                            <div id="img">
                                <img src="{img}" title="{name}" alt=" {name}" width="290" height="340"/>
                            </div> <!--"img" div -->

                            </div>'''
                    info = info.format(**locals())

                    self.response.write(info)

            self.response.write(p.footer)


class Animals(object):
    def __init__(self):
        #empty variable space for the sub classes to fill in
        self.phylum = ''
        self.classs = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.image = ''
        self.lifespan = ''
        self.habitat = ''
        self.geolocation = ''

    @property
    def sound(self):
        return self.sound

    @sound.setter
    def sound(self, new_sound):
        pass
        #self.sound = new_sound


#panther's info
class Panther(Animals):
    def __init__(self):
            super(Panther, self).__init__()
            #const. function -- super class

            #data for the empty var in the super class above
            self.title = "What does the Panther Say?"
            self.phylum = 'Chordata'
            self.classs = 'Mammalia'
            self.order = 'Carnivora'
            self.family = 'Felidae'
            self.genus = 'Puma'
            self.image = ''
            self.lifespan = 'Twelve years in the wild'
            self.habitat = 'Wetland/Saw palmetto'
            self.geolocation = 'Florida- Everglades'


#dolphin's info
class Dolphin(Animals):
    def __init__(self):
            super(Dolphin, self).__init__()
            #const. function -- super class

            #data for the empty var in the super class above
            self._title = "What does the Dolphin Say?"
            self._phylum = 'Chordata'
            self._classs = 'Mammalia'
            self._order = 'Cetacea'
            self._family = 'Odontaceti'
            self._genus = 'Delphinidae'
            self._image = ''
            self._lifespan = 'Up to Twenty years'
            self._habitat = 'Water'
            self._geolocation = 'Throughout the oceans'


#fox's info
class Fox(Animals):
    def __init__(self):
            super(Fox, self).__init__()
            #const. function -- super class
            #data for the empty var in the super class above
            self._title = "What does the Fox Say?"
            self._phylum = 'Chordata'
            self._classs = 'Mammalia'
            self._order = 'Carnivora'
            self._family = 'Canidae'
            self._genus = 'Vulpes'
            self._image = ''
            self._lifespan = 'Ten years in the wild'
            self._habitat = 'Forest, deserts, grassland, mountains'
            self._geolocation = 'All continent expect Antarctica'

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
