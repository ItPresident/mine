from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create(address="127.0.0.1", port=25565)

if __name__ == "__main__":
    mc.postToChat("Hellow min")
    time.sleep(5)


