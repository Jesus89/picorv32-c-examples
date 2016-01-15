import os
import png
import numpy
import itertools


images = ['clifford', 'os', 'oh', 'gnu', 'tux', 'riscv', 'rpi', 'smiley', 'bq']

numpy.set_printoptions(threshold=numpy.nan)


def generate(name):
    path = os.getcwd() + '/images/' + name + '-32x32.png'
    file = open(path, 'r')
    img = png.Reader(file)
    matrix = img.read()
    data = matrix[2]
    # Check data
    image_2d = numpy.vstack(itertools.imap(numpy.uint16, data))

    r = image_2d[:, range(0, 96, 3)]
    g = image_2d[:, range(1, 96, 3)]
    b = image_2d[:, range(2, 96, 3)]

    return r, g, b


def replace(text):
    text = text.replace('[ ', '').replace('[', '').replace(']', '')
    text = text.replace(' ', ',').replace(',,', ',').replace(',,', ',')
    return text


def print_channel(id, data, n):
    print('uint8_t ' + id + '[' + str(n) + '][32][32] = {')
    print(replace(str(data)))
    print('};\n')


def add(channel, new):
    if channel is None:
        return new
    else:
        return numpy.concatenate((channel, new))


def main():
    n = len(images)
    r, g, b = None, None, None
    for image in images:
        nr, ng, nb = generate(image)
        r = add(r, nr)
        g = add(g, ng)
        b = add(b, nb)
    print('int num = ' + str(n) + ';\n')
    print_channel('r', r, n)
    print_channel('g', g, n)
    print_channel('b', b, n)


if __name__ == '__main__':
    main()
