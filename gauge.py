import PIL as pil
from PIL import Image
import numpy as np
from scipy.misc import imsave
from scipy.ndimage import filters


def sobel_filter(image):
    dx = filters.sobel(image, 0)
    dy = filters.sobel(image, 1)
    return np.hypot(dx, dy)


def harris_filter(image, sigma=7):
    # image derivatives
    imx = np.zeros(image.shape)
    imy = np.zeros(image.shape)
    filters.gaussian_filter(image, (sigma, sigma), (0,1), imx)
    filters.gaussian_filter(image, (sigma, sigma), (1,0), imy)

    window_xx = filters.gaussian_filter(imx ** 2, sigma)
    window_xy = filters.gaussian_filter(imx * imy, sigma)
    window_yy = filters.gaussian_filter(imy * imy, sigma)

    determinant = window_xx * window_yy - window_xy ** 2
    trace = window_xx + window_yy
    return determinant / trace


image_filename = 'oil_gauge.jpg'
base_filename = image_filename.split('.')[0]
my_image = pil.Image.open(image_filename).convert('L')
np_image = np.array(pil.Image.open(image_filename))
image_r = np_image[:,:,0]
image_g = np_image[:,:,1]
image_b = np_image[:,:,2]
imsave(base_filename + '-g.jpg',image_g)
imsave(base_filename + '-r.jpg',image_r)
imsave(base_filename + '-b.jpg',image_b)
for color, image in zip(['r', 'g', 'b'], [image_r, image_g, image_b]):
    imsave('corner' + color + '.jpg', harris_filter(image))
