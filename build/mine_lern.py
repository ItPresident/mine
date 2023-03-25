import random
from mcpi.minecraft import Minecraft
from settings import (
    address,
    air,
    stone,
    torch,
)
import time

mc = Minecraft.create(address=address)

#mc.postToChat("Hello")
x, y, z = mc.player.getPos()

# for y_m in range(10):
#     for x_m in range(100):
#         for z_m in range(100):
#             mc.setBlock(x + x_m, y-y_m, z + z_m, air)


def light_post(mc, x, y, z, id, id2):
    mc.setBlocks(x, y, z, x, y+10, z, id)
    mc.setBlocks(x+1, y, z, y+10, z, id2)
    mc.setBlocks(x-1, y, z, y+10, z, id2)
    mc.setBlocks(x, y, z+1, y+10, z, id2)
    mc.setBlocks(x, y, z-1, y+10, z, id2)

# light_post(mc, x, y, z, stone, torch)

x_r = random.randint(-30, 30)
y_r = random.randint(-30, 30)
z_r = random.randint(-30, 30)

mc.setBlock(x+x_r, y+y_r, z+z_r, torch)