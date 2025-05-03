# RL_Final_Project

An impementation of the game of "cat and mouse" with reinforcement learning in PyTorch using OpenAI Gym and MuJoCo as training environments.

# Installation Directions
## MuJoCo
MuJoCo is available open-source, either from their website or using the following commands, making a hidden file for the code under `.mujoco`
```
wget -c https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz -O - | tar -xz
mkdir -p ~/.mujoco
mv ./mujoco210 ~/.mujoco
```
## Dependencies
We use conda to manage our dependencies. First, download Anaconda, make a conda environment (such as conda activate `mujoco_py`) and run the following commands:
```
conda install python==3.8.12
conda install -c conda-forge gym[all]
conda install -c pytorch pytorch
conda install matplotlib 
pip3 install mujoco-py>=2.1.2.14 more_itertools tqdm
```

# Running the Project