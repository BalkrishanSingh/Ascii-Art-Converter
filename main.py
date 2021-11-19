from PIL import Image

# ASCII_TEMPLATE = ['$', '@','B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 
# 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j',
#  'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', 'i', '!', 'l', 'I',
#  ';', ':', ',', '"', '^', '`']

ASCII_TEMPLATE  = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def get_image():
    """Returns a image at the user inputted path"""
    while True:
        try:
            image = Image.open(input('Input the Absolute Path To JPG Image: '))
        except KeyboardInterrupt:
            print('bye')
            break
        except:
            print('Input The Absolute Path.')
        else:
            return image

def resize_image(image,new_width = 250):#Use Can Resize your image from here
    """Resizes a given image to the specfied width and height and returns it"""
    width,height = image.size
    ratio = height/width
    new_height = int(new_width*ratio)
    new_image = image.resize((new_width,new_height))
    return new_image

def gray_scaling_image(image):
    """Converts a given image to a grayscaled image"""
    grayscaled_image = image.convert('L')
    return grayscaled_image

def pixel_to_ascii(image):
    """Converts a image's Pixel data to ascii data. """
    pixels  = image.getdata()
    image_ascii_data  = ''.join([ASCII_TEMPLATE[pixel//25] for pixel in pixels])
    return image_ascii_data

def add_newlines(string,width):
    """This will add newlines at specifed intervals in the given string."""
    rows = []
    for i in range(0,len(string),width):
        rows.append(string[i:i+width])
    return '\n'.join(rows)

#Main Logic
def main():
    image = get_image() #Getting The Image
    new_image = gray_scaling_image(resize_image(image)) # GrayScaling and Resizing the image
    width,_ = new_image.size #Getting the new image width
    image_ascii_data = pixel_to_ascii(new_image)
    ascii_image = add_newlines(image_ascii_data,width)
    try:
        save_as = input('Save Ascii Art as : ' )
        with open(f'{save_as.strip()}.txt','w+') as f:
            f.write(ascii_image)
    except:
        print('There was a Error Making your Ascii Art.')
if __name__ == '__main__':
    main()