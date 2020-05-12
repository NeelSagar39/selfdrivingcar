import movement as movement_test
import camera
import os
from inception import inception_v3 as inception
import h5py
import numpy as np
from keras.models import load_model
from keras.models import Model
from PIL import Image


print("Wait please")
p = 0
tf = 0.5
camera.init()
#movement_test.init()
model = inception(128,128)
model.load('inception_model_final2.model')
print("Camera initialized, go ahead!")
try:
    while p != 3:
        camera.take_picture_test()
        image = Image.open('test.jpg')
        Image._show(image)
        image = np.array(image)
        p = model.predict(np.expand_dims(image, axis=0))
        print(p)
        p = np.argmax(p, axis = 1)
        p=p[0]

        if p == 0:
            movement_test.left(tf)
            print("left")

        elif p == 1:
            movement_test.forward(tf)
            print("forward")

        elif p == 2:
            movement_test.right(tf)
            print("right")
    
except  KeyboardInterrupt:
    movement_test.end()
    camera.end()
    print ("Cleaned up pins")
   

