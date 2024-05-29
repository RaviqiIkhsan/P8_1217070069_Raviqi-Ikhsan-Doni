#Raviqi Ikhsan Doni
#1217070069
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Kopi.jpg')
kopi = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(kopi)
plt.show()
kernel = np.ones((5,5),np.float32)/25
print("Kernel:\n", kernel)
kopi_filter = cv2.filter2D(img, -1, kernel)
plt.imshow(kopi_filter)
plt.show()