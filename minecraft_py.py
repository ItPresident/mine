from mcpi.minecraft import Minecraft

mc = Minecraft.create(address="192.168.1.129")

mc.postToChat("Start")

def p_pos(mc):
	x, y, z = mc.player.getPos()
	return x, y, z

#
# x += 1
# # y += 1
# z += 1

# print(x, y, z)



# for i_x in range(20):
# 	for i_z in range(20):
# 		mc.setBlock(x, y, z + i_z, 168)
# 	x += 1

pos = (55.9688434543945, 12.0, 69.59631104662134)
# pos = p_pos(mc)

# mc.setBlock(pos[0], pos[1], pos[2], 45)
x = pos[0]
y = pos[1]
z = pos[2]
print(pos)
for s in range(2):
	for i in range(5):
		mc.setBlocks(x, y, z, x, y, z + 11, 45)
		y += 1
	x -= 1
	y -= 5


mc.postToChat("Stop")

