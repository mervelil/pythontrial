# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np

image_original = cv2.imread("C:\\resim.jpg")
text = 'MerveCelik'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (00, 185)
color = (0, 0, 255)
fontScale=1
thickness = 2
image = cv2.putText(image_original, text, org, font, fontScale,
                    color, thickness, cv2.LINE_AA, True)

gaus_blur=cv2.GaussianBlur(image_original,(7,7),0)
cv2.imshow('Gaussian Blur',gaus_blur)
cv2.waitKey(0)
avg_blur= cv2.blur(image_original,(3,3))
cv2.imshow('Averaging blur',avg_blur)
cv2.waitKey(0)
median_blur=cv2.medianBlur(image_original,5)
cv2.imshow('Median blur',median_blur)

cv2.waitKey(0)
bilateral_blur=cv2.bilateralFilter(image_original,9,75,75)
cv2.imshow('Bilateral blur',avg_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
