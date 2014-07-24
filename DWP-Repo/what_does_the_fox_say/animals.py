class Animal(object): #abstract class-- used as a template
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
        
