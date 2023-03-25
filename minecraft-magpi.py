import mcpi.minecraft as minecraft

import time

mc = minecraft.Minecraft.create(address="127.0.0.1", port=25565)
#mc = minecraft.Minecraft.create()

if __name__ == "__main__":
    mc.postToChat("Hellow min")
#    mc.getBlock(-2, 63, 7, 22)
