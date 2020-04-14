import datetime
class Building: 
    def __init__(self, address, stories):
        self.address = address
        self.stories = stories
        self.designer = "Sofia"
        self.owner = ""
        self.date_constructed = ""
    def construct(self): 
        self.date_constructed = datetime.datetime.now()
    def purchase(self, owner): 
        self.owner = owner
