import pygame

class Level:
    def __init__(self):

        self.current_level = 1
        self.total_levels = 5

        #tiles
        self.tile_size = 64

        #colors
        self.wall_color = (35, 15, 45)
        self.floor_color = (100, 45, 40)
        self.door_color = (160, 105, 45)
        self.counter_color = (80, 80, 80)
        self.background_color = (15, 5, 5)

        #level layouts

        self.level_maps = {
            1:[
                "####################",
                "#..................#",
                "#..######..######..#",
                "#..#....#..#....#..#",
                "#..D....#..#....D..#",
                "#..#....#..#....#..#",
                "#..######..######..#",
                "#..................#",
                "#.......CCCC.......#",
                "#..................#",
                "####################"                
            ],
            
            2:[
                "####################",
                "#..................#",
                "#..####......####..#",
                "#..#..#......#..#..#",
                "#..D..#......#..D..#",
                "#..#..#......#..#..#",
                "#..####......####..#",
                "#..................#",
                "#.....CCCCCCCC.....#",
                "#..................#",
                "####################"                
            ],

            3:[
                "####################",
                "#..................#",
                "#..####..##..####..#",
                "#..#..#..##..#..#..#",
                "#..D..#......#..D..#",
                "#..#..####..##..#..#",
                "#..####......####..#",
                "#..................#",
                "#......CCCC........#",
                "#..................#",
                "####################"
            ],

            4:[
                "####################",
                "#..................#",
                "#.####..####..####.#",
                "#.#..#..#..#..#..#.#",
                "#.D..#..D..#..D..#.#",
                "#.#..####..####..#.#",
                "#.####........####.#",
                "#..................#",
                "#....CCCCCCCC......#",
                "#..................#",
                "####################"
            ],

            5:[
                "####################",
                "#..................#",
                "#.####.######.####.#",
                "#.#..#.#....#.#..#.#",
                "#.D..#.#....#.#..D.#",
                "#.#..#.#....#.#..#.#",
                "#.####.######.####.#",
                "#..................#",
                "#......CCCC........#",
                "#..................#",
                "####################"
            ]
        }

        self.load_level(1)

    def load_level(self, level_number):

        if level_number < 1 or level_number > self.total_levels:
            return False

        self.current_level = level_number
        self.map_data = self.level_maps[level_number]

        self.rows = len(self.map_data)
        self.columns = len(self.map_data[0])

        self.width = self.columns * self.tile_size
        self.height = self.rows * self.tile_size

        self.offset_x = (1280 - self.width) // 2
        self.offset_y = (720 - self.height) // 2

        return True

#advance to th next level
    def advance_level(self):

        if self.current_level < self.total_levels:

            self.load_level(self,current_level + 1)
            return True
    
        return False

    def draw(self, screen):

        screen.fill(self.background_color)

        for row_index, row in enumerate(self.map_data):

            for column_index, tile in enumerate(row):

                x = self.offset_x + column_index* self.tile_size
                y = self.offset_y + row_index * self.tile_size

                tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_sze)

                if tile_size == "#":
                    color = self.wall_color

                elif tile == ".":
                    color = self.floor_color

                elif tile == "D":
                    color = self.door_color

                elif tile == "C":
                    color = self.counter_color

                else:
                    continue

                pygame.draw.rect(screen, color, tile_rect)

                pygame.draw.rect(screen,(20, 15, 15), tile_rect, 1)

    def is_walkable(self, pixel_x, pixel_y):

        colummn = int(
            (pixel_x - self.offset_x) // self.tile_size
        )

        row - int(
            (pixel_y - self.self.offset_y) // self.tile_size
            )

        if row < 0 or row >= self.rows:
            return False

        if column < 0 or column >= self.columns:
            return False

        tile = self.map_data[row][column]

        return tile not in ("#", "C")

    def is_final_level(self):

        return self.current level == self.total_levels
