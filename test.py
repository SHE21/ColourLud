import imageio
import colour.io
import cv2

# RGB = images.read_image('src/foto1.jpg')
# img = imageio.imread('src/foto1.jpg')
# RGB = colour.read_image('src/foto1.jpg', 'float32', 'Imageio')
# colour.read_LUT('src/foto1.jpg')
# print(RGB.shape)

input = cv2.imread('src/color1.jpg') # faz leitura do raster
cv2.imshow('Hello World', input)
cv2.waitKey(0)
cv2.destroyAllWindows()

lab = cv2.cvtColor(input, cv2.COLOR_BGR2LAB)
cv2.imshow("l*a*b",lab)

L,A,B = cv2.split(lab)
cv2.imshow("L_Channel",L) # For L Channel
cv2.imshow("A_Channel",A) # For A Channel (Here's what You need)
cv2.imshow("B_Channel",B) # For B Channel

cv2.waitKey(0)
cv2.destroyAllWindows()

print(L)

#array([ 0.45595571,  0.03039702,  0.04087245])