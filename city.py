class City: 
    def __init__(self, name, mayor, year_established):
        self.name = name
        self.mayor = mayor
        self.year_established = year_established
        # Buildings are not essential, so they aren't a parameter 
        # However, for users to be able to add buildings nonetheless we establish an array that can hold the collection
        self.buildings = []
    def add_building(self, building): 
        self.buildings.append(building)