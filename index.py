import Capture
import Calculator
import cv2
import colour

img = Capture.getCapture("images/imagenTeste1.png")

input = cv2.imread("src/color2.jpg")

RGB = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
R, G, B = cv2.split(RGB)
r = R[0][0]
g = G[0][0]
b = B[0][0]

print("##### RGB #####")
print(str(r) + " " + str(g) + " " + str(b))

print("\n##### CIELab #####")
CIELab = Calculator.rgb2lab([r, g, b])
print(CIELab)

XYZ = Calculator.rgbtoXYZ(r, g, b)
print("\n####### XYZ -> ##########")
print(XYZ)

xyY = colour.XYZ_to_xyY(XYZ)
print("\n####### xyZ -> ##########")
print(xyY)

mussel = colour.xyY_to_munsell_colour([xyY[0], xyY[1], xyY[2]/100])
print("\n####### mussel -> ##########")
print(mussel)