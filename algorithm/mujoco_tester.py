import mujoco 
import mediapy as media

with open("../environments/main_scene.xml", "r") as file:
  xml = file.read()

arm = mujoco.MjModel.from_xml_string(xml)

# with open("../environments/cat/go1.xml", "r") as file:
#   xml = file.read()

# cat = mujoco.MjModel.from_xml_string(xml)

# data stores the state and quantities that depend of it
# The state is made up of time, generalized positions and generalized velocities. 
# These are respectively <data>.time, <data>.qpos and <data>.qvel
arm_data = mujoco.MjData(arm)
# cat_data = mujoco.MjData(cat)

# render and show 
with mujoco.Renderer(arm) as renderer:
  media.write_image('graphics/agent.png', renderer.render())

print(arm_data.time)