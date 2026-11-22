from settings import *
from collections import deque
from game_objects import LevelExit, Ammobox, Medkit, Enemy

class GameMap:
    def __init__(self, level):
        self.grid = []
        filename = f"levels/level{level}.txt"
        with open(filename, 'r') as file:
            for line in file.readlines():
                self.grid.append(line.replace('\n', ''))

    def draw_map(self, screen,player, objects):
        scale = 0.1
        map_title = TILE_SIZE * scale

        for j, line in enumerate(self.grid):
            for i, symbol in enumerate(line):
                if symbol == '.':
                    tile_color = (100, 100, 100)
                if symbol == '#':
                    tile_color = (30,30,30)
                pygame.draw.rect(screen, tile_color, (i * map_title, j * map_title, map_title, map_title))


        map_player_x = int(player.x * scale)
        map_player_y = int(player.y * scale)
        pygame.draw.circle = (screen, (0, 200, 0), (map_player_x, map_player_y), 5)
        target_x = int(math.cos(player.angle) * 20)
        target_y = int(math.sin(player.angle) * 20)
        pygame.draw.line(screen, (20, 200, 20),
                         (map_player_x, map_player_y),
                         (map_player_x + target_x, map_player_y + target_y)
                         )

        for o in objects:
            map_o_x = int(o.x * scale)
            map_o_y = int(o.y * scale)
            color = (30,30,30)
            if isinstance(o, Enemy):
                color = (200,0,0)
            elif isinstance(o, Medkit):
                color = (200,100,100)
            elif isinstance(o, LevelExit):
                color = (0,0,200)
            elif isinstance(o, Ammobox):
                color = (0,100,100)
            pygame.draw.circle(screen,color,(map_o_x,map_o_y), 5)

    def mapping(self, x, y):
        return int(y) // TILE_SIZE, int(x) // TILE_SIZE