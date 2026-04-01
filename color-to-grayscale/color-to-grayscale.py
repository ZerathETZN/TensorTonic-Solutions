def color_to_grayscale(image):
    out = []
    for row in image:
        out_row = []
        for pixel in row:
            R, G, B = pixel
            g = 0.299 * R + 0.587 * G + 0.114 * B
            out_row.append(g)
        out.append(out_row)
    return out

image1 = [[[255,0,0]]]  # 1x1
print(color_to_grayscale(image1))  # [[76.245]]
image2 = [[[255,0,0],[0,255,0]], [[0,0,255],[255,255,255]]]
print(color_to_grayscale(image2))