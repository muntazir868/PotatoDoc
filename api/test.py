import cv2
import os

# Path to the directory containing the image
image_dir = 'C:\Project\PlantVillage\Potato___healthy/'

# List all files in the directory
files = os.listdir(image_dir)

# Select the first image file (you may need to modify this logic based on your requirements)
image_path = os.path.join(image_dir, files[0])

# Read the image
image = cv2.imread(image_path)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
