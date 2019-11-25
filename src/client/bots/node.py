
class node():
    
    def __init__(self, coord, username, team = None):
        self.coord = coord
        self.team = team
        self.username = username
        self.n_around = 0
    
    def set_dist_to_ball(self, dist):
        self.dist_to_ball = dist
    
    def increase_n_around(self):
        self.n_around += 1
        
    def calculate_weight(self):
        self.w = self.dist_to_ball*self.n_around