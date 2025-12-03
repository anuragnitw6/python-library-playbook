import cv2
import numpy as np

# Load image
img = cv2.imread("document.png")
orig = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(gray, 75, 200)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        doc_cnt = approx
        break

# Perspective transform
pts1 = np.float32([pt[0] for pt in doc_cnt])
pts2 = np.float32([[0,0],[500,0],[500,700],[0,700]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
scanned = cv2.warpPerspective(orig, matrix, (500,700))

cv2.imshow("Original", orig)
cv2.imshow("Scanned Document", scanned)
cv2.waitKey(0)
cv2.destroyAllWindows()
