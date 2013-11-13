import PIL as pil
from PIL import Image
import numpy as np
from scipy.misc import imsave

image_filename = 'gague-test-image.jpg'
base_filename = 'gague'
my_image = pil.Image.open(image_filename).convert('L')
np_image = np.array(pil.Image.open(image_filename))
image_b = np_image[:,:,0]
image_r = np_image[:,:,1]
image_g = np_image[:,:,2]
imsave(base_filename + '-g.pdf',image_g)
imsave(base_filename + '-r.pdf',image_r)
imsave(base_filename + '-b.pdf',image_b)

