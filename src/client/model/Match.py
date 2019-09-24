
class Match():
    """Class of model that has all functions/logic needed to execute application without including view logic"""
    
    def __init__(self):
        """Builder empty"""
        pass
    
    def is_collided_with(self, player, ball):
        """Method that check if a player -specified by parameter- hit with the ball -specified by parameter-"""
        if player.has_ball:
            return True
        collided = False
        sw = ball.rect.width
        sh = ball.rect.height
        if player.team:
            if (player.x+sw*2)>=ball.x and (player.x+sw)<=ball.x:
                if player.y<=ball.y and (player.y+sh)>=(ball.y-sh-10):
                    collided = True
        else:
            if (player.x-15)>=ball.x and (player.x-sw)<=ball.x:
                if player.y<=ball.y and (player.y+sh)>=(ball.y-sh-10):
                    collided = True
        return collided