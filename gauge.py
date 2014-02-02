import PIL as pil
from PIL import Image
import numpy as np
from scipy.misc import imsave

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

