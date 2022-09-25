import gridWorld

class GridAgent():
    def __init__(self):
        self.reward = 0

    def reset(self):
        self.reward = 0
    
    def act(self, action):
        y, x = self.pos

        # if hitting a wall, don't move.
        if action == 0:   # move north (up)
            if y - 1 >= 0:
                y -= 1   
        elif action == 1: # move east (right)
            if x + 1 <= gridWorld.BOARD_COLS - 1:
                x += 1 
        elif action == 2: # move south (down)
            if y + 1 <= gridWorld.BOARD_ROWS - 1:
                y += 1
        elif action == 3: # move west (left)
            if x - 1 >= 0:
                x -= 1

        self.pos = (y, x)
