#Raviqi Ikhsan Doni
#1217070069
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"Kopi.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fourier = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
fourier_shift = np.fft.fftshift(fourier)
magnitude = 20 * np.log(cv2.magnitude(fourier_shift[:, :, 0], fourier_shift[:, :, 1]))
magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
plt.imshow(magnitude_normalized, cmap='gray')
plt.title('Magnitude Spectrum')
plt.axis('off')
plt.show()