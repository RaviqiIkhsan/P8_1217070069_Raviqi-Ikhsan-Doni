import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('Kopi.jpg')
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(cat)
plt.show()
kernel = np.ones((5,5),np.float32)/25
print("Kernel:\n", kernel)
kopi_filter = cv2.filter2D(img, -1, kernel)
plt.imshow(kopi_filter)
plt.show()
plt.rcParams["figure.figsize"] = (15,15)

plt.subplot(121),plt.imshow(cat),plt.title('Ori')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(kopi_filter)
plt.title('Avg')
plt.xticks([]), plt.yticks([])

plt.show()