import gym
from numpy import inf
from gym import error, spaces, utils
from gym.utils import seeding


class DayTradingEnv(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self, action_space=spaces.Box(-1, 1, (1,)), history=5):
		self.action_space = action_space
		self.history = history
		self.observation_space = spaces.Tuple(spaces={
			spaces.Box(low=-1, high=1, shape=(history,))
		})

	def step(self, action):
		...

	def reset(self):
		...

	def render(self, mode='human', close=False):
		...

