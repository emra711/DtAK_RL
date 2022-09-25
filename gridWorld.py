import numpy as np
import random

# global variables:
BOARD_ROWS = 5
BOARD_COLS = 4
START_STATE = (0,0)
GOAL_STATE = (BOARD_ROWS-1, BOARD_COLS-1)
FAIL_STATE = (1, 3)
OBSTACLES = 2
GOAL_REWARD = 100
FAIL_REWARD = -10

# define world actions according to (delta-y, delta-x)
# note: grid world defined as (x, y) with top left as (0,0)
world_actions = {
    'N': 0,
    'S': 2,
    'E': 1,
    'W': 3
}
action_arr = list(world_actions.keys())

class GridWorld():
    def __init__(self, rows=BOARD_ROWS, cols=BOARD_COLS, obstacles=OBSTACLES):
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles
        self.start_state = START_STATE
        self.goal_state = GOAL_STATE
        self.fail_state = FAIL_STATE
        self.world_actions = world_actions
        self.action_arr = action_arr

    def reset(self):
        self.grid = np.zeros((self.rows, self.cols))
        self.grid[GOAL_STATE[0], GOAL_STATE[1]] = GOAL_REWARD
        self.grid[FAIL_STATE[0], FAIL_STATE[1]] = FAIL_REWARD

        # randomly assign obstacles with random negative values
        for _ in range(self.obstacles):
            obst_val = random.uniform(-2.0, -0.5)
            obst_row = None
            obst_col = None

            # make sure obstacle isn't placed at the start state, goal state, or fail state
            while True:
                obst_row = random.randint(0, self.rows-1)
                obst_col = random.randint(0, self.cols-1)

                if (obst_row, obst_col) != START_STATE and (obst_row, obst_col) != GOAL_STATE and (obst_row, obst_col) != FAIL_STATE:
                    break

            self.grid[obst_row, obst_col] = obst_val

    def actionProbs(self, action):
        if action == 0:   # move north (up)
            return np.random.choice(action_arr, p=[0.7, 0.1, 0.1, 0.1])
        elif action == 1: # move east (right)
            return np.random.choice(action_arr, p=[0.1, 0.7, 0.1, 0.1])
        elif action == 2: # move south (down)
            return np.random.choice(action_arr, p=[0.1, 0.1, 0.7, 0.1])
        elif action == 3: # move west (left)
            return np.random.choice(action_arr, p=[0.1, 0.1, 0.1, 0.7])
    
    def drawWorld(self):
        world = []
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) == START_STATE:
                    world.append('o ')
                elif (i, j) == GOAL_STATE:
                    world.append('X ')
                elif (i, j) == FAIL_STATE:
                    world.append('_ ')
                elif self.grid[i][j] < 0.0: # is an obstacle
                    world.append('# ')
                else:
                    world.append('. ')
            world.append('\n')

        toDraw = ''.join(world)
        print(toDraw)


def main():
    grid = GridWorld()
    grid.reset()
    grid.drawWorld()

if __name__ == "__main__":
    main()



