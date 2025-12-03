import cv2

# Load image
img = cv2.imread("sample_image.jpg")

# Apply different blurring techniques
blur = cv2.GaussianBlur(img, (7,7), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
