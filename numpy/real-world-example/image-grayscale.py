import numpy as np
from PIL import Image

# Load image
img = Image.open("sample.jpg")
img_arr = np.array(img)

# Convert to grayscale using mean
gray = np.mean(img_arr, axis=2)

# Save output
gray_img = Image.fromarray(gray.astype("uint8"))
gray_img.save("gray_output.jpg")

print("Grayscale conversion done!")
