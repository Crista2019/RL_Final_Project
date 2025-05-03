import mujoco 

with open("../environments/arm/gen3.xml", "r") as file:
  xml = file.read()

model = mujoco.MjModel.from_xml_string(xml)

# create data and render
data = mujoco.MjData(model)
renderer = mujoco.Renderer(model)

print(data)