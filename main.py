from matplotlib import image
from matplotlib import pyplot
import pandas as pd

print("HI")
def dataimg():

    data = image.imread('C:\\Users\\Vaikavi\\Desktop\\Kayaemo\\gigi.jpg')
    imagedata = pd.DataFrame({"image": data})

    print(imagedata)

    return imagedata 

a = dataimg()
print(a)
