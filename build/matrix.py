import time

from mcpi.minecraft import Minecraft, BlockEvent
from settings import (
	address,
	stone,
	air,
	REDSTONE
)

mc = Minecraft.create(address=address)

mc.postToChat("[INFO] Start")
mc.getPlayerEntityId()
b = Block
x, y, z = mc.player.getPos()

matrix = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
	[1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
	[1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
	[1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
	[1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
	[1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

matrix_revers = []

for i in range(1, len(matrix)+1):
	matrix_revers.append(matrix[-i])



# for y_r in range(10):
# 	matrix.append([])
# 	for x_c in range(10):
# 		matrix[y_r].append(1)
#
# for i in matrix:
# 	print(i)

# x -= 10
# y -= 10
z += 10
for z_m in range(10):
	for y_row, block_row in enumerate(matrix_revers):
		for x_item, block_item in enumerate(block_row):
			if not block_item:
				mc.setBlock(x+x_item, y+y_row, z, REDSTONE)
			else:
				mc.setBlock(x+x_item, y+y_row, z, air)
			time.sleep(0.01)
	z += 1
print(x, y, z)
mc.postToChat("[INFO] End")
