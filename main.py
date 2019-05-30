from matplotlib import image
from matplotlib import pyplot


def dataimg():

    data = image.imread('House.jpg')

    print(data.dtype)
    print(data.shape)

    return data 

