from ursina import *


app = Ursina()

Entity(model='sphere', color=color.pink, texture='white_cube', scale=10)

EditorCamera()

app.run()