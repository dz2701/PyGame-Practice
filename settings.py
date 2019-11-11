class Settings():
    def __init__(self):
        #screen Settings
        self.screen_w = 2000
        self.screen_h = 1200
        self.color = (51,153,255)

        #ship Settings
        self.ship_speed = 10

        #bullet Settings
        self.bullet_speed_factor = 10
        self.bullet_width = 25
        self.bullet_height = 25
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3

        #enemy Settings
        self.enemy_speed = 1
        self.drop_speed = 10
        #set direction 1 for right and -1 left
        self.fleet_direction =  1
