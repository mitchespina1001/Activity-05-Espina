import cv2 as cv
import numpy as np


def sijak():
    read()


def read():

    image = cv.imread('CHITTAPHON.jpg')

    s = image.shape

    if len(s) == 3:
        mod(image)

    else:
        print("IMAGE CAN'T RELOAD")


def mod(image):
    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("COLOR FEATURES: "))

    cv.imshow("BEFORE ", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    pixel = image.item(x, y, z)
    print("IMAGE VALUE: ", x, y, z)
    print("PIXEL VALUE: ", pixel)

    image.itemset((x, y, z), 200)
    pixel = image.item(x, y, z)
    print("MODIFIED PIXEL VALUE: ", pixel)

    dm(image)


def dm(image):

    sz = image.shape

    x = 1000
    y = 1000

    if sz[0] > x and sz [1] > y:
        print("INVALID IMAGE DIMENTION!!!!!")

    else:
        imgTyp(image)


def imgTyp(image):
    dtype = image.dtype
    print("IMAGE DATA TYPE: ", dtype)

    imgSz(image)


def imgSz(image):

    reqSz = 2000000
    size = image.size

    if size <= reqSz:
        print("IMAGE SIZE VALIDATED!!!!!")
        cv.imshow("AFTER", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("IMAGE SIZE INVALID!!!!")


sijak()
