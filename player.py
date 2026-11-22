from settings import *

class Player:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
        self.speed = 10
        self.sensitivity = 0.005
        self.angle = 0
        self.health = 70
        self.max_health = 100
        self.size = 57
        self.ammo = 50
        self.weapons = SHOTGUN
        self.chosen = 0
    def check_collision(self, object_touching):
        distance = (self.x - object_touching.x) ** 2 + (self.y - object_touching.y) ** 2
        return distance <= self.size ** 2
    def move(self, gave_map):
        self.angle += pygame.mouse.get_rel()[0] * self.sensitivity
        self.angle %= math.tau
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        if keys[pygame.K_1]:
            if len(self.weapons) > 0:
                self.chosen = 0
        if keys[pygame.K_2]:
            if len(self.weapons) > 1:
                self.chosen = 1

        if keys[pygame.K_w]:
            dx += cos_a * self.speed
            dy += sin_a * self.speed
        if keys[pygame.K_s]:
            dx -= cos_a * self.speed
            dy -= sin_a * self.speed

        if keys[pygame.K_a]:
            dx += sin_a * self.speed
            dy -= cos_a * self.speed
        if keys[pygame.K_d]:
            dx -= sin_a * self.speed
            dy += cos_a * self.speed


        if not game_map.is_wall(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy
        else:
            self.x -= dx
            self.y -= dy

