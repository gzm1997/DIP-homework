from PIL import Image
import numpy
import math

def scale(image_url, new_size, new_url):
    try:
        img = Image.open(image_url)
    except Exception as e:
        return False
    img = img.convert("L")
    src = numpy.array(img)
    src_heigh = src.shape[0]
    src_width = src.shape[1]   
    dst = numpy.zeros(shape = new_size)
    dst_heigh = new_size[0]
    dst_width = new_size[1]

    for dst_x in range(dst_heigh):
        for dst_y in range(dst_width):
            src_h = dst_x * (src_heigh / dst_heigh)
            src_w = dst_y * (src_width / dst_width)
            u, i = math.modf(src_h)
            v, j = math.modf(src_w)
            i = int(i)
            j = int(j)
            if i + 1 > src_heigh - 1:
                iadd1 = src_heigh - 1
            else:
            	iadd1 = i + 1
            if j + 1 > src_width - 1:
            	jadd1 = src_width - 1
            else:
            	jadd1 = j + 1
            q1 = src[i, j]
            q2 = src[iadd1, j]
            q3 = src[i, jadd1]
            q4 = src[iadd1, jadd1]
            dst[dst_x, dst_y] = (1 - u) * (1 - v) * q1 + (1 - u) * v * q3 + u * (1 - v) * q2 + u * v * q4
    dst = Image.fromarray(dst)
    if dst.mode != 'RGB':
        dst = dst.convert('RGB')
    dst.save(new_url)
    return True

if __name__ == "__main__":
    print(scale("94.png", (192, 128), "192_128.png"))
    print(scale("94.png", (96, 64), "96_64.png"))
    print(scale("94.png", (48, 32), "48_32.png"))
    print(scale("94.png", (24, 16), "24_16.png"))
    print(scale("94.png", (12, 8), "12_8.png"))
    print(scale("94.png", (300, 200), "300_200.png"))
    print(scale("94.png", (450, 300), "450_300.png"))
    print(scale("94.png", (500, 200), "500_200.png"))