from cv2 import cv2
for i in range(8):
    for j in range(590):
        image = cv2.imread("%d/frame%d.jpg"%(i, j))
        image = cv2.resize(image, (image.shape[1]//(j % 10 + 1), image.shape[0]//(j % 10 + 1)))
        cv2.imwrite("%d/frame%d.jpg"%(i, j), image)
