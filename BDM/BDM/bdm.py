import numpy as np

'''
image1--d--image2
'''

image1 = [0,0,0,0,0,
          0,0,0,0,0,
          0,0,0,1,0,
          0,0,0,0,0,
          0,0,0,0,0]

image2 = [0,0,0,0,0,
          0,0,0,0,0,
          0,1,0,0,0,
          0,0,0,0,0,
          0,0,0,0,0]

cameraFocalLength = 24 #in [mm]
distanceBOC = 5 # [cm]
Ul = 15 # [cm] this is an estimate distance by pixel representation
Ur = 5 # [cm] this is an estimate distance by pixel representation

def distFromPtoCam(Cfl, Dboc, Ul, Ur):
    return Cfl*(Dboc/(Ul-Ur))

print(distFromPtoCam(cameraFocalLength,distanceBOC,Ul,Ur))
