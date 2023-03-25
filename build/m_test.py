import time

from mcpi.minecraft import Minecraft
from settings import (
	address,
	stone,
	air,
	REDSTONE
)

mc = Minecraft.create(address=address)

mc.postToChat("[INFO] Start")

data = mc.player.getPos()

print(data)
mc.postToChat("[INFO] End")
