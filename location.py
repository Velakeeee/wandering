class location:
    def __init__(self):
        self.location_wandering = {}
        
    def add_wandering(self, wandering, location):
        self.location_wandering[wandering] = location
        
    def move_wandering(self,wandering):
        delt_x, delt_y = wandering.walk()
        location_now = self.location_wandering[wandering]
        new_location = location_now.move(delt_x, delt_y)
        
        self.location_wandering[wandering] = new_location
    
    def get_location(self, wandering):
        return self.location_wandering[wandering]
        