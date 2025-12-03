import cv2

# Load an image
img = cv2.imread("sample.jpg")  # Place a sample image in the folder

# Display the image
cv2.imshow("Image", img)

# Wait for key press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()
