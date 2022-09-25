import matplotlib.pyplot as plt
import matplotlib.animation
from IPython.display import HTML
from IPython.display import display
import numpy as np
import gridWorld
import gridAgent
import gridLearner

class GridEnvironmemt():
    def __init__(self):
        self.world = gridWorld.GridWorld()
        self.agent = gridAgent.GridAgent()
        self.learn = gridLearner.GridLearner(self)

    def reset(self):
        self.world.reset()
        self.agent.reset()
        self.learn.reset()

        self.agent.pos = self.world.start_state

        self.history = []
    
    def record(self):
        grid = np.array(self.world.grid)
        self.history.append(grid)

    def getState(self):
        return self.agent.pos

    def step(self, action):
        # var to keep track of whether game is finished or not
        finished = False

        action_taken = self.world.actionProbs(self.world.world_actions[action])
        self.agent.act(self.world.world_actions[action_taken])

        self.learn.last_reward = self.world.grid[self.agent.pos]

        # give grid value to agent reward after doing an action
        self.agent.reward += self.world.grid[self.agent.pos]

        if self.agent.pos == self.world.goal_state or self.agent.pos == self.world.fail_state:
            finished = True
        
        self.record()
        
        return self.agent.pos, self.world.grid[self.agent.pos], finished

    def run(self, rounds=10, step_limit=10000):
        for _ in range(rounds):
            reward = 0
            self.reset()
            num_steps = 0
            finished = False
            curr_state = self.agent.pos

            while not finished and num_steps <= step_limit:
                action_to_take = self.learn.q_learning(curr_state)
                curr_state, action_reward, finished = self.step(action_to_take)
                reward += action_reward
                num_steps += 1
            print("Reward is here:", reward)

def animate(history):
    frames = len(history)
    fig = plt.figure(figsize=(gridWorld.BOARD_ROWS, gridWorld.BOARD_COLS))
    fig_grid = fig.add_subplot(121)

    def render_frame(i):
        grid = history[i]
        fig_grid.matshow(grid, vmin=-1, vmax=1, cmap='jet')

    anim = matplotlib.animation.FuncAnimation(
        fig, render_frame, frames = frames, interval=100
    )

    plt.close()
    display(HTML(anim.to_html5_video()))


def main():
    env = GridEnvironmemt()
    env.reset()
    env.world.drawWorld()
    env.run()

    # animate(env.history)

if __name__ == "__main__":
    main()
