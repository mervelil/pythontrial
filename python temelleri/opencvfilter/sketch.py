import cv2 as cv

def convert(image):
    grayImage= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    blur_image=cv.GaussianBlur(grayImage,(3,3),0)
    edgeImage=cv.adaptiveThreshold(blur_image,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,5)
    output=cv.bitwise_and(image,image,mask=edgeImage)
    cv.imshow("Cartoon Effect",output)
    cv.waitKey(0)
text = 'MerveCelik'
image_original = cv.imread("C:\\resim.jpg")
font = cv.FONT_HERSHEY_SIMPLEX
org = (00, 185)
color = (0, 0, 255)
fontScale=1
thickness = 2
image = cv.putText(image_original, text, org, font, fontScale,
                    color, thickness, cv.LINE_AA, True)
convert(image_original)