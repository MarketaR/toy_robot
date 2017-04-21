class Robot():
    direction = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    rotation_map = {'NORTH': {'LEFT': 'WEST', 'RIGHT': 'EAST'},
                    'SOUTH': {'LEFT': 'EAST', 'RIGHT': 'WEST'},
                    'EAST': {'LEFT': 'NORTH', 'RIGHT': 'SOUTH'},
                    'WEST': {'LEFT': 'SOUTH', 'RIGHT': 'NORTH'}}

    coord_x = [0, 1, 2, 3, 4]
    coord_y = [0, 1, 2, 3, 4]

    def __init__(self, placed, x, y, facing):
        self.placed = placed
        self.x = x
        self.y = y
        self.facing = facing

    def place(self, x, y, f):
        """
        Place the robot on the table.
        """
        try:
            self.coord_x[int(x)]
            self.coord_y[int(y)]

            if f in self.direction:

                self.x = x
                self.y = y
                self.facing = f
                self.placed = True

            else:
                pass

        except IndexError:
            pass

    def move(self):
        """
        Move robot one field according to the direction of facing.
        """
        if self.placed:
            try:
                if self.facing == 'NORTH':
                    self.y = self.coord_y[int(self.y) + 1]
                elif self.facing == 'SOUTH':
                    self.y = self.coord_y[int(self.y) - 1]
                elif self.facing == 'WEST':
                    self.x = self.coord_x[int(self.x) - 1]
                elif self.facing == 'EAST':
                    self.x = self.coord_x[int(self.x) + 1]
            except IndexError:
                pass

        else:
            pass

    def left(self):
        """
        Turn robot 90 degrees to the left.
        """
        if self.placed:
            self.facing = self.rotation_map[self.facing]["LEFT"]
        else:
            pass

    def right(self):
        """
        Turn robot 90 degress to the right.
        """
        if self.placed:
            self.facing = self.rotation_map[self.facing]["RIGHT"]
        else:
            pass

    def report(self):
        """
        Return position and facing of the robot.
        """
        if self.placed:
            print("{},{},{}". format(self.x, self.y, self.facing))
        else:
            return None
