import os
import sys
import png
import numpy
import itertools

path = os.getcwd() + '/' + sys.argv[1]
file = open(path, 'r')
img = png.Reader(file)
matrix = img.read()
data = matrix[2]
# Check data
image_2d = numpy.vstack(itertools.imap(numpy.uint16, data))

r = image_2d[:, range(0, 96, 3)]
g = image_2d[:, range(1, 96, 3)]
b = image_2d[:, range(2, 96, 3)]

numpy.set_printoptions(threshold=numpy.nan)


def replace(text):
    return text.replace(' ', ',').replace(',,', ',').replace(',,', ',').replace('[', '').replace(']', '')

print("uint8_t r[32][32] = {")
print(replace(str(r)))
print("};\n")

print("uint8_t g[32][32] = {")
print(replace(str(g)))
print("};\n")

print("uint8_t b[32][32] = {")
print(replace(str(b)))
print("};\n")
