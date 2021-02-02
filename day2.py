from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+4,y+4,z+4,46)
mc.setBlocks(x+1,y+1,z+1,x+3,y+3,z+3)


import time

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.01)
    
    
    
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(5)
    
    
while True:
    x,y,z = mc.player.getTilePos()
    a = mc.getBlock(x+1,y-1,z)
    b = mc.getBlock(x-1,y-1,z)
    c = mc.getBlock(x,y-1,z+1)
    d = mc.getBlock(x,y-1,z-1)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,20)
        
x,y,z = mc.player.getTilePos()   
    
a = 0
while a < 5:
    mc.setBlocks(x+10,y-1,z,x-5,y-5,z,19)
    z = z+5
    a = a+1
  
x,y,z = mc.player.getTilePos()  
a = int(input('what block do you want to put?'))
mc.setBlock(x,y,z,a)
  
name = input('enter your name.')
message = input('enter your message.')
mc.postToChat('<' + name + '>' + message)

x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'hello','world','yeh','yeh')

while True:
    x,y,z = mc.player.getTilePos()  
    
    a = mc.getBlockWithData(x,y-1,z)
    if a.data == 15:
        mc.postToChat('turn right')  
    if a.data == 11:
        mc.postToChat('turn right')
        
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        
        if block == 1:
            mc.setBlock(x,y,z,41)
            

            
            
            
        