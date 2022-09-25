import numpy as np

class GridLearner():
    def __init__(self, env):
        self.env = env
        self.finished = False
        self.last_action = None
        self.last_reward = 0
        self.last_state = self.env.world.start_state

        self.learn_rate = 0.2
        self.discount = 0.75
        self.exp_rate = 0.0001 # exploration vs epxloitation
        self.Q = np.zeros((4, self.env.world.rows, self.env.world.cols))

    def reset(self):
        self.last_action = None
        self.last_reward = 0
        self.last_state = self.env.world.start_state

    def q_learning(self, curr_state):
        new_action = ""

        if np.random.rand() <= self.exp_rate or self.last_action == None:
            new_action = np.random.choice(self.env.world.action_arr)

            self.Q[self.env.world.world_actions[new_action]][curr_state[0]][curr_state[1]] = self.last_reward
            self.last_state = curr_state
            self.last_action = new_action

            return new_action
        else:
            new_action = np.argmax([self.Q[self.env.world.world_actions[a]][curr_state[0]][curr_state[1]] for a in self.env.world.action_arr])
            
        prev_stateQ = self.Q[self.env.world.world_actions[self.last_action]][self.last_state[0]][self.last_state[1]]
        new_stateQ = self.Q[new_action][curr_state[0]][curr_state[1]]

        self.Q[self.env.world.world_actions[self.last_action]][self.last_state[0]][self.last_state[1]] = prev_stateQ + self.learn_rate*(self.last_reward + self.discount*(new_stateQ - prev_stateQ))

        self.last_state = curr_state
        self.last_action = self.env.world.action_arr[new_action]
        return self.env.world.action_arr[new_action]


