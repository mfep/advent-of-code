from itertools import product

WIDTH = 25
HEIGHT = 6
SIZE = WIDTH * HEIGHT
BLACK = 0
WHITE = 1
TRANSPARENT = 2

def get_layers(line):
    data = [int(char) for char in line]
    numlayers = int(len(data) / SIZE)
    layers = []
    for layer_idx in range(numlayers):
        layers.append(data[layer_idx * SIZE : (layer_idx + 1) * SIZE])
    return layers

def get_pixel(col, row, layer):
    return layer[row * WIDTH + col]

def render_pixel(col, row, layers):
    for layer in layers:
        layer_pixel = get_pixel(col, row, layer)
        if layer_pixel is not TRANSPARENT:
            return layer_pixel
    return TRANSPARENT

def render_image(layers):
    image = []
    for row, col in product(range(HEIGHT), range(WIDTH)):
        image.append(render_pixel(col, row, layers))
    return image

def display_image(image):
    for row in range(HEIGHT):
        line = ''
        for col in range(WIDTH):
            pixel = get_pixel(col, row, image)
            if pixel is BLACK:
                line += '▓'
            elif pixel is WHITE:
                line += '░'
            elif pixel is TRANSPARENT:
                line += ' '
            else: raise Exception()
        print(line)

with open('day8.txt') as f:
    line = f.readline().strip()
layers = get_layers(line)
min_layer = min(layers, key=lambda layer: layer.count(0))
print('part one', min_layer.count(1) * min_layer.count(2))
image = render_image(layers)
display_image(image)
