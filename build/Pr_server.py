from mcpi.minecraft import Minecraft
from settings import (
        address,
        stone,
        air,
        REDSTONE,
	
)
import time 

mc = Minecraft.create(address=address)
def status(func):
	print("[INFO] is running")
	func()
	print("[INFO] is closid")


@status
def start():
	mc.postToChat("Hi chat")
	print(mc.player.getPos())
	print(mc.player.getPos(id=536))
