from PIL import Image
import numpy
import math

def nearest_point(gray_list, gray_value):
	_min = (abs(gray_value - gray_list[0]), 0)
	index = 1
	for i in gray_list[1:]:
		dis = abs(gray_value - i)
		if dis < _min[0]:
			_min = (dis, index)
		index = index + 1
	return gray_list[_min[1]]
	

def quantize(image_url, new_level):
    try:
        img = Image.open(image_url)
    except Exception as e:
        return False
    img = img.convert("L")
    src = numpy.array(img)
    src_heigh = src.shape[0]
    src_width = src.shape[1]
    interval = int(256 / new_level)
    gray_list = [0]
    for i in range(1, new_level + 1):
    	gray_list.append(interval * i - 1)
    dst = numpy.zeros(shape = src.shape)
    for dst_x in range(src_heigh):
    	for dst_y in range(src_width):
    		result_gray = nearest_point(gray_list, src[dst_x, dst_y])
    		#print("result_gray", result_gray)
    		dst[dst_x, dst_y] = result_gray

    dst = Image.fromarray(dst)
    if dst.mode != 'RGB':
        dst = dst.convert('RGB')
    dst.save("newImage.png")
    return True

if __name__ == "__main__":
	print(quantize("94.png", 8))