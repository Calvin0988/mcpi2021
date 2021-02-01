from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat('X:' + str(x) +'Y:' + str(y) + 'Z:' + str(z))


x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,22)
mc.setBlock(x,y+1,z,22)
mc.setBlock(x,y+2,z,22)
mc.setBlock(x,y+3,z,22)
mc.setBlock(x,y+4,z,22)
mc.setBlock(x,y+5,z,22)
mc.setBlock(x,y+6,z,22)
mc.setBlock(x,y+7,z,22)


x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,22)
mc.setBlock(x-1,y,z,22)
mc.setBlock(x,y,z+1,22)
mc.setBlock(x,y,z-1,22)
mc.setBlock(x+1,y,z-1,22)
mc.setBlock(x+1,y,z+1,22)
mc.setBlock(x-1,y,z+1,22)
mc.setBlock(x-1,y,z-1,22)




x,y,z = mc.player.getTilePos()
mc.setBlocks(x+22,y,z+22,x-22,y,z-22,20)


import random
import time
x,y,z = mc.player.getTilePos()

while True:
    r=random.randrange(0,16)
    mc.setBlocks(x+7,y,z+7,x-7,y,z-7,35,r)
    time.sleep(0.01)





