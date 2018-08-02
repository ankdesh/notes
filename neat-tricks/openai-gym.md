# Codes for handling openAI Gym

* Capturing the env frames and playing it separately in Jupyter notebook
1. Run the notebook with following command 
```sh
xvfb-run -s "-screen 0 1400x900x24" jupyter notebook
```

2. Capture the frames from environment
```py
observation = env.reset()
cum_reward = 0
frames = []
for t in range(1000):
    frames.append(env.render(mode = 'rgb_array'))
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        break
env.render(close=True)
```

3. Run the animation from captured frames 
```py
def display_frames_as_gif(frames):
    """
    Displays a list of frames as a gif, with controls
    """
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0), dpi = 72)
    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    display(display_animation(anim, default_mode='loop'))

display_frames_as_gif(frames)
```py
