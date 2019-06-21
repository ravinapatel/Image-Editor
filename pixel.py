"""
PIXELATOR

Pixelates image

NAME: Ravina Patel
DATE: 6-6-19
"""


from PIL import Image

#create an Image object
im = Image.open('clock_tower.jpg')
og = im.copy()

#copy
def copy(image, box):
    """
    RETURNS: a copy of the region of the image determined by the coordinates of box

    PARAMETER: image - an Image object
    PARAMETER: box - the region rectangle, as a (left, upper, right, lower)-tuple
    """

    region = image.crop(box)
    return region

#process
def process(region):
    """
    RETURNS: the region after making all the pixels the average color of the whole region

    PARAMETER: region - an image object
    """
    r = []
    g = []
    b = []
    for pixel in list(region.getdata()):
        r.append(pixel[0])
        g.append(pixel[1])
        b.append(pixel[2])
    average_color = (average(r), average(g), average(b), 255)

    pixels = region.load() # creates pixel map
    for i in range(region.size[0]):
        for j in range(region.size[1]):
            pixels[i,j] = average_color # makes each pixel = ave color
    return region


def average(list):
    """
    RETURNS: the average float value of the items in a list

    PARAMETER: list - a nonempty list of numbers (integers or floats)
    """
    sum = 0
    for num in list:
        sum += num
    return sum//len(list)

#paste back
def replace(image,processed_region,box):
    """
    RETURNS: the image with the box region replaced with the processed_region image

    PARAMETER: image - an Image object
    PARAMETER: processed_region - an Image object that has been processed
    PARAMETER: box - the region rectangle, as a (left, upper, right, lower)-tuple
    """
    image.paste(processed_region,box)
    return image

def pixelate(image, rank):
    """
    RETURNS: the image modified so it is pixelated with RANK square pixels along the length

    PARAMETER: image - an Image object
    PARAMETER: rank - a number > 0
    """
    pixel_size = image.size[0]//rank
    vert_pix = image.size[1]//pixel_size
    if image.size[0]%rank != 0:
        rank +=1
    if image.size[1]%rank != 0:
        vert_pix +=1
    for i in range(rank):
        for j in range(vert_pix):
            box = (i*pixel_size,j*pixel_size,min((i+1)*pixel_size,image.size[0]),min((j+1)*pixel_size,image.size[1]))
            replace(image,process(copy(image,box)),box)
    return image
