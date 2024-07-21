from PIL import Image

def get_img_path():
    return input('image path >>> ')

def preprocess_img(img):
    grays = img.convert('L')
    grays.thumbnail((100, 100))
    return grays

def generate_ascii(img):
    out = ''
    width, height = img.size
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            char = map_to_ascii(pixel)
            out += char
        out += '\n'
    return out


def map_to_ascii(pixel):
    lum_mapping = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    out_idx = pixel // 4
    return lum_mapping[out_idx]


def main():
    path = get_img_path()
    img = Image.open(path)
    img = preprocess_img(img)
    output = generate_ascii(img)
    print('here is the ascii version')
    print(output)
    with open('output.txt', 'w') as out:
        out.write(output)
    print('done')


if __name__ == '__main__':
    main()
