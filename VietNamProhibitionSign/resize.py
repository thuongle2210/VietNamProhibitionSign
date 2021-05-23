from cv2 import cv2
import numpy as np
for i in range(8):
    for j in range(590):
        image = cv2.imread("/home/thuongle2210/Documents/OS/mở rộng/VietNamProhibitionSign (copy)/VietNamProhibitionSign/%d/frame%d.jpg"%(i, j))
        image = cv2.resize(image, (image.shape[1]//(j % 20 + 1), image.shape[0]//(j % 20 + 1)))

        size = j % 7 + 1
        kernel = np.ones((size,size), np.float32)/(size**2)
        image = cv2.filter2D(image, -1, kernel)
        cv2.imwrite("%d/frame%d.jpg"%(i, j), image)
