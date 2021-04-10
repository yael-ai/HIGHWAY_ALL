# -*- coding: utf-8 -*-
"""SocialAttentionDQN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/eleurent/highway-env/blob/master/scripts/intersection_social_dqn.ipynb

# Training a DQN with social attention on `intersection-v0`

## Import requirements
"""

# Commented out IPython magic to ensure Python compatibility.
# Environment
#!pip install git+https://github.com/eleurent/highway-env#egg=highway-env
import gym
import highway_env

# Agent
#!pip install git+https://github.com/eleurent/rl-agents#egg=rl-agentsA

# Visualisation utils
import sys
# %load_ext tensorboard
#!pip install tensorboardx gym pyvirtualdisplay
#!apt-get install -y xvfb python-opengl ffmpeg
#!git clone https://github.com/eleurent/highway-env.git
sys.path.insert(0,'/data/home/yael123/HIGHWAY_ALL/highway-env/scripts/')
rl_agents_dir = '/data/home/yael123/HIGHWAY_ALL/rl-agents/'
sys.path.append(rl_agents_dir)

from utils import show_videos


"""## Training

Prepare environment, agent, and evaluation process.

We use a policy architecture based on social attention, see [[Leurent and Mercat, 2019]](https://arxiv.org/abs/1911.12250).

"""

# Commented out IPython magic to ensure Python compatibility.
from rl_agents.trainer.evaluation import Evaluation
from rl_agents.agents.common.factory import load_agent, load_environment

# Get the environment and agent configurations from the rl-agents repository
#!git clone https://github.com/eleurent/rl-agents.git
# %cd /content/rl-agents/scripts/

import os
os.chdir(rl_agents_dir + "/scripts/")
env_config = 'configs/HighwayEnv/env.json'
agent_config = 'configs/HighwayEnv/agents/DQNAgent/ddqn.json'

env = load_environment(env_config)
env.config["lanes_count"] = 4
#env.config["vehicles_count"]=30
#env.config["vehicles_density"] = 2

env.reset()
agent = load_agent(agent_config, env)
evaluation = Evaluation(env, agent, num_episodes=3000, display_env=False)
print("10/04/2021")
print("From git")
print(f"Ready to train {agent} on {env}")

"""Run tensorboard locally to visualize training."""

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir "{evaluation.directory}"

"""Start training. This should take about an hour."""

evaluation.train()

"""Progress can be visualised in the tensorboard cell above, which should update every 30s (or manually). You may need to click the *Fit domain to data* buttons below each graph.

## Testing

Run the learned policy for a few episodes.
"""

env = load_environment(env_config)
env.configure({"offscreen_rendering": True})
env.config["lanes_count"] = 4
#env.config["vehicles_count"]=30
#env.config["vehicles_density"] = 2
env.reset()
agent = load_agent(agent_config, env)
evaluation = Evaluation(env, agent, num_episodes=3000, recover=True)
evaluation.test()
show_videos(evaluation.run_directory)
