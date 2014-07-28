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
        animals = [panther, dolphin, fox]

        #sounds : panther, dolphin, fox
        panther = Panther()
        panther.sound = "Meeeooowww"

        dolphin = Dolphin()
        dolphin.sound = "Eeeeeik"

        fox = Fox()
        fox.sound = "Aaaooh"

        self.response.write(page.header + page.links)
        if self.request.GET: #button is selected show data
            animals = int(self.request.GET['animal'])

name = animals[animal].name
phylum = animals[animal].phylum
classs = animals[animal].classs
order = animals[animal].order
family = animals[animal].family
genus = animals[animal].genus
img = animals[animal].img
lifespan = animals[animal].lifespan
habitat = animals[animal].habitat
geolocation = animals[animal].geolocation
sound = animals[animal].sound

#info will have all the information populated into 3 sections
info='''<div id="info">
<h3>{name}</h3>
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
<img src="{img}" title="Picture of {name}" alt="Picture of {name}" width="290" height="340" />
</div> <!-- Closes "img" div -->
</div>'''
info = info.format(**locals())

self.response.write(info)
self.response.write(page.footer)

#abstract class-- used as a template
class Animals(object):
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
@property
def sound(self):
return self.__sound
@sound.setter
def sound(self, new_sound):
self.__sound = new_sound



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
