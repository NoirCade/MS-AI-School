import gym
import torch
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.evaluation import evaluate_policy
import cv2

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# create environment
env = make_atari_env('ALE/Skiing-v5', n_envs=16, seed=0)

# create DQN agent
model = DQN('CnnPolicy', env, learning_rate=1e-4, buffer_size=100000, batch_size=32, learning_starts=10000,
            exploration_fraction=0.1, exploration_initial_eps=1.0, exploration_final_eps=0.01, train_freq=4,
            target_update_interval=10000, gamma=0.99, verbose=1, device=device)

# train the agent
model.learn(total_timesteps=10000000)

# save the model
model.save("./dqn_test.pt")

# evaluate the trained agent
mean_reward, _ = evaluate_policy(model, env, n_eval_episodes=10)
print(f"Mean reward: {mean_reward:.2f}")

obs = env.reset()
obs = torch.from_numpy(obs).float().to(device)
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    obs = torch.from_numpy(obs).float().to(device)
    env.render()
