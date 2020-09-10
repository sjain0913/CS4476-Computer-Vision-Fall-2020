import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = np.asarray(Image.open('q4-input.png'))

# Question 4 (a)
def swap_rg_channels(image):
    red = image[:,:,:1]
    green = img[:,:,1:2]
    blue = img[:,:,2:3]
    swapped = np.zeros(image.shape)
    swapped[:,:,:1] = green
    swapped[:,:,1:2] = red
    swapped[:,:,2:3] = blue
    return swapped.astype(np.uint8)

# Commented out after image produced
# img_to_save = Image.fromarray(swap_rg_channels(img), 'RGB')
# img_to_save.save('q4-output-swapped.png')
swapped = np.asarray(Image.open('q4-output-swapped.png')) # Saving channel swapped image for future reference


# Question 4 (b)
def grayscale(image):
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
# Commented out after image produced
# img_to_save = Image.fromarray(grayscale(img))
# img_to_save.save('q4-output-grayscale.png')
gray = np.asarray(Image.open('q4-output-grayscale.png')) # Saving grayscale image for future reference

# Question 4 (c)
def gray_to_negative(gray_image):
    init_matrix = np.full(gray_image.shape, 255)
    negative = np.subtract(init_matrix, gray_image)
    return negative.astype(np.uint8)

negative = np.asarray(Image.open('q4-output-negative.png')) # Saving negative image for future reference

# Commented out after image produced
# img_to_save = Image.fromarray(gray_to_negative(gray))
# img_to_save.save('q4-output-negative.png')

# Question 4 (d)
def gray_to_mirror(gray_image):
    return gray_image[:,::-1].astype(np.uint8)

# Commented out after image produced
# img_to_save = Image.fromarray(gray_to_mirror(gray))
# img_to_save.save('q4-output-mirror.png')
mirror = np.asarray(Image.open('q4-output-mirror.png')) # Saving mirror image for future reference

# Question 4 (e)
def avg_orig_mirror(gray_image, mirror_image):
    gray = gray_image.astype(np.uint8)
    mirror = mirror_image.astype(np.uint8)
    average = np.divide(np.add(gray, mirror), 2)
    return average.astype(np.uint8)

# Commented out after image produced
# img_to_save = Image.fromarray(avg_orig_mirror(gray, mirror))
# img_to_save.save('q4-output-average.png')
average = np.asarray(Image.open('q4-output-average.png')) # Saving average image for future reference

# Question 4 (f)
def noise(gray_image):
    N = np.random.randint(0, 256, size = gray.shape)
    np.save('q4-noise.npy', N)
    result = np.add(N, gray_image)
    clipped = np.clip(result, 0, 255)
    return clipped.astype(np.uint8)

# Commented out after image produced
# img_to_save = Image.fromarray(noise(gray))
# img_to_save.save('q4-output-noise.png')
noise = np.asarray(Image.open('q4-output-noise.png')) # Saving noise image for future reference



# MAKING SUBPLOTS
fig, ax = plt.subplots(3, 2)

ax[0,0].imshow(swapped)
ax[0,0].set_title('Channels Swapped')

ax[0,1].imshow(gray, cmap="gray")
ax[0,1].set_title('Grayscale')

ax[1,0].imshow(negative, cmap="gray")
ax[1,0].set_title('Negative')

ax[1,1].imshow(mirror, cmap="gray")
ax[1,1].set_title('Mirror')

ax[2,0].imshow(average, cmap="gray")
ax[2,0].set_title('Average')

ax[2,1].imshow(noise, cmap="gray")
ax[2,1].set_title('Noise')

fig.tight_layout()
plt.savefig('q4-subplot')
plt.show()