def image_histogram(image):
    out = [0] * 256
    for row in image:
        for pixel in row:
            out[pixel] += 1
    return out
            
image1 =  [[0, 1], [1, 2]]
print(image_histogram(image1))  
image2 =  [[128, 128], [128, 128]]
print(image_histogram(image2))  
            