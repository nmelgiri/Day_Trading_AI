import gym
from gym.spaces import Discrete, Box
import gym_day_trading

import json

SETTING = "Setting 1: Raw Numerical Inputs"


def get_action_space_history():
	settings = json.load(open("setup.json", "r"))
	inputs, history = settings["inputs"], settings["history"]
	if SETTING == "Setting 1: Raw Numerical Inputs":
		high, low = settings[SETTING]["Action Space"]["upper limit"], settings[SETTING]["Action Space"]["lower limit"]
		action_space = Box(low, high, shape=(history, inputs))
		return action_space, history


def main():
	history, action_space = get_action_space_history()
	env = gym.make("day_trading-v0", action_space=action_space, history=history)


if __name__ == '__main__':
	main()
