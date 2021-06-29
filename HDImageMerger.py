import PIL.Image
import random

#Made by Deeakron L

#number needs to be in quotation marks (a string) so that numbers like 0001 can be input
def combineImagesHD(number):

    #Path for unit to add background to
    pathUnit = "files/unit/Unit" + number + ".png"

    #Paths of the parts of the background
    path000 = "files/circle/bgi_circle_000.png"
    path001 = "files/circle/bgi_circle_001.png"
    path002 = "files/circle/bgi_circle_002.png"
    path003 = "files/circle/bgi_circle_003.png"
    path004 = "files/circle/bgi_circle_004.png"
    path005 = "files/circle/bgi_circle_005.png"
    path006 = "files/circle/bgi_circle_006.png"
    path007 = "files/circle/bgi_circle_007.png"
    path008 = "files/circle/bgi_circle_008.png"
    path009 = "files/circle/bgi_circle_009.png"
    path010 = "files/circle/bgi_circle_010.png"

    #Opening up the images
    unit = PIL.Image.open(pathUnit)
    circle000 = PIL.Image.open(path000)
    circle001 = PIL.Image.open(path001)
    circle002 = PIL.Image.open(path002)
    circle003 = PIL.Image.open(path003)
    circle004 = PIL.Image.open(path004)
    circle005 = PIL.Image.open(path005)
    circle006 = PIL.Image.open(path006)
    circle007 = PIL.Image.open(path007)
    circle008 = PIL.Image.open(path008)
    circle009 = PIL.Image.open(path009)
    circle010 = PIL.Image.open(path010)

    #Generating random spins
    num1 = random.randrange(360)
    num2 = random.randrange(360)
    num3 = random.randrange(360)
    num4 = random.randrange(360)
    num5 = random.randrange(360)
    num6 = random.randrange(360)
    num8 = random.randrange(360)

    #Applying random spins
    circle001 = circle001.rotate(num1)
    circle002 = circle002.rotate(num2)
    circle003 = circle003.rotate(num3)
    circle004 = circle004.rotate(num4)
    circle005 = circle005.rotate(num5)
    circle006 = circle006.rotate(num6)
    circle008 = circle008.rotate(num8)

    #Creating the layer with the unit centered in the correct spot and the bounding box for cropping
    unit.convert('RGBA')
    unitSize = unit.size
    unitSize2 = unitSize[0] / 2, unitSize[1] / 2
    unitBox = (1991 - unitSize2[0] - 10, 745 - unitSize2[1] - 10, 1991 + unitSize2[0] + 10, 745 + unitSize2[1] + 10)
    unitSpace = PIL.Image.new("RGBA", circle000.size)
    unitSpace.paste(unit, (1991 - unitSize2[0], 745 - unitSize2[1]))

    #Putting it all together
    circle = PIL.Image.new("RGBA", circle000.size)
    circle = PIL.Image.alpha_composite(circle, circle000)
    circle = PIL.Image.alpha_composite(circle, circle010)
    circle = PIL.Image.alpha_composite(circle, circle009)
    circle = PIL.Image.alpha_composite(circle, circle008)
    circle = PIL.Image.alpha_composite(circle, circle007)
    circle = PIL.Image.alpha_composite(circle, circle006)
    circle = PIL.Image.alpha_composite(circle, circle005)
    circle = PIL.Image.alpha_composite(circle, circle004)
    circle = PIL.Image.alpha_composite(circle, circle003)
    circle = PIL.Image.alpha_composite(circle, circle002)
    circle = PIL.Image.alpha_composite(circle, circle001)
    circle = PIL.Image.alpha_composite(circle, unitSpace)

    #Cropping and saving
    circle = circle.crop(unitBox)
    circle.save("Done.png")


combineImagesHD("2447")