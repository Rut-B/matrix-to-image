#view image from txt file
import numpy as np
from pylab import imshow, figure
import matplotlib.pyplot as plt
import cv2
import scipy.misc

f = open('____.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
A=np.array(triplets, dtype=np.uint8)
B = np.array(A).reshape(1024, 1024)
plt.figure("output image: ")
plt.imshow(B , cmap='gray')
plt.show()