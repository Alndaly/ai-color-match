def getRgbChannels(image):
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]
    return r, g, b