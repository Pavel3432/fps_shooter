from settings import *


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None



    def get_sprite(self, player):
        dx = math.cos(player.angle)
        dy = math.sin(player.angle)
        full_distance = math.hypot(dx,dy)
        angle_to_obj = math.atan2(dx, dy)
        delta_angle = angle_to_obj - player.angle
        delta_angle = (math.pi + delta_angle) % math.tau - math.pi

        if -HALF_FOV < delta_angle < HALF_FOV:
            distance = full_distance * math.cos(delta_angle)
            if distance <= 0:
                return None
            proj_height = PROJ_COEF / distance
            screen_x = SCREEN_WIDTH // 2 + (delta_angle * DIST)
            screen_y = SCREEN_HEIGHT // 2 - proj_height // 2
            return full_distance, screen_X, screen_y, proj_height


        return None



class Enemy:
    def __init__(self, x, y, image, health, damage, speed):
        super().__init__(x,y)
        self.image = image
        self.health = health
        self.damage = damage
        self.speed = speed
        self.path = []
        self.path_timer = 30
        self.attack_timer = 60

    def attack(self, player):
        self.attack_timer -= 1
        if self.attack_timer <= 0 and player.check_collision(self):
            self.attack_timer = 60
            player.health -= self.damage
            print(player.health)

    def move(self, player, game_map):
        self.path_timer -= 1
        if self.path_timer <= 0:
            self.path_timer = 30
            sy,sx = game_map.mapping(self.x, self.y)
            gy, gx = game_map.mapping(player.x, player.y)
            self.path = game_map.find_path((sx, sy), (gx, gy))

class Medkit(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = MEDKIT_IMG
        self.health = 50

class Ammobox(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = AMMO_IMG
        self.ammo = 10

class LevelExit(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = EXIT_IMG

class WeaponIcon(GameObject):
    def __init__(self, x, y, weapon_type):
        self.weapon_type = weapon_type
        super().__init__(x, y)
        self.image = weapon_type.icon_image