import camera
import movement
import os
import pygame
os.environ['SDL_VIDEODRIVER']='dummy'
pygame.init()
pygame.display.set_mode((1,1))
condition = True
st = 0.5
camera.init()
#movement.car.init()
print('HAJIMAE')
while condition:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_UP:
                print('UP')
                movement.forward(st)
                os.chdir('/home/pi/Desktop/New_beginning/w')
                camera.take_picture()
                
            elif event.key == pygame.K_DOWN:
                movement.reverse(st)
                print('DOWN')
            elif event.key == pygame.K_LEFT:
                os.chdir('/home/pi/Desktop/New_beginning/a')
                camera.take_picture()
                movement.left(st)
                print('LEFT')
            elif event.key == pygame.K_RIGHT:
                os.chdir('/home/pi/Desktop/New_beginning/d')
                camera.take_picture()
                movement.right(st)
                print('RIGHT')
            elif event.key == pygame.K_SPACE:
                movement.car.end()
                
                print('STOP')
                
            elif event.key == 113:
                print("done")
                camera.end()
                condition=False
                break
    

