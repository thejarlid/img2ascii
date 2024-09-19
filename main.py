from PIL import Image
import subprocess
import argparse

ASCII_SCALE = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # 65 characters long
MAX_PIXEL_VAL = 255
SCALE_FACTOR = (len(ASCII_SCALE) - 1)/MAX_PIXEL_VAL

def load_image(img_path):
    try:
        im = Image.open(img_path)
        im = im.resize((im.size[0]//4, im.size[1]//4))
        print(f"Successfully loaded image!\nImage Size: {im.size}")
        return im    
    except OSError:
        print("failed to open file")
        return None
    
def pixeldata2mat(pixeldata):
    pixel_matrix = [[(0, 0, 0)] * img.size[0] for _ in range(img.size[1])]

    for i in range(len(pixeldata)):
        row = i // img.size[0]
        col = i % img.size[0]
        pixel_matrix[row][col] = pixeldata[i]

    return pixel_matrix

def rgb2brightness(rgb_mat, invert=False):
    brightness_mat = [[0] * len(rgb_mat[0]) for _ in range(len(rgb_mat))]
    for row in range(len(rgb_mat)):
        for col in range(len(rgb_mat[0])):
            rgb_val = rgb_mat[row][col]
            brightness_mat[row][col] = (rgb_val[0] + rgb_val[1] + rgb_val[2])/3
            if invert:
                brightness_mat[row][col] = 255 - brightness_mat[row][col]
    return brightness_mat

def rgb2luminosity(rgb_mat, invert=False):
    brightness_mat = [[0] * len(rgb_mat[0]) for _ in range(len(rgb_mat))]
    for row in range(len(rgb_mat)):
        for col in range(len(rgb_mat[0])):
            rgb_val = rgb_mat[row][col]
            brightness_mat[row][col] = (0.21 * rgb_val[0] + 0.72 * rgb_val[1] + 0.07 * rgb_val[2])
            if invert:
                brightness_mat[row][col] = 255 - brightness_mat[row][col]
    return brightness_mat

def brightness2ascii(brightness_mat):
    ascii_mat = [[''] * len(brightness_mat[0]) for _ in range(len(brightness_mat))]
    for row in range(len(brightness_mat)):
        for col in range(len(brightness_mat[0])):
            ascii_mat[row][col] = ASCII_SCALE[round(brightness_mat[row][col] * SCALE_FACTOR)]
    return ascii_mat

def print_ascii_mat(ascii_mat):
    for row in range(len(ascii_mat)):
        for col in range(len(ascii_mat[0])):
            print(f"{ascii_mat[row][col]}{ascii_mat[row][col]}{ascii_mat[row][col]}", end="")
        print("\n", end="")




parser = argparse.ArgumentParser(prog='img2ascii', description='Converts images to ascii text on the terminal')
parser.add_argument('-c', '--camera', action='store_true', help='Use the camera feed as input')
parser.add_argument('-f', '--filename', type=str, nargs='?', help='The filename of the image to be used')
args = parser.parse_args()

if args.camera:
    subprocess.run("imagesnap")
    filename = "snapshot.jpg"
elif args.filename:
    filename = args.filename      
else:
    parser.error('No input source provided, add --camera or --filename')

img = load_image(filename)
if not img:
    exit()

pixeldata = list(img.getdata())
pixel_mat = pixeldata2mat(pixeldata)
print("Successfully constructed pixel matrix!")
print(f"Brightness matrix size: {len(pixel_mat[0])} x {len(pixel_mat)}")
print("Dumping Last 2 rows of pixel data")
print(f"{pixel_mat[-2]}\n{pixel_mat[-1]}")

brightness_mat = rgb2luminosity(pixel_mat)
print("Successfully constructed brightness matrix!")
print(f"Brightness matrix size: {len(brightness_mat[0])} x {len(brightness_mat)}")
print("Dimping last 2 rows of pixel data")
print(f"{brightness_mat[-2]}\n{brightness_mat[-1]}")

ascii_mat = brightness2ascii(brightness_mat)
print("Successfully constructed ASCII matrix!")
print(f"ASCII matrix size: {len(ascii_mat[0])} x {len(ascii_mat)}")
print("Dumping last two rows of ascii pixel data")
print(f"{ascii_mat[-2]}\n{ascii_mat[-1]}")

print_ascii_mat(ascii_mat)
