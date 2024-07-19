
import cv2

# Read the image file
img = cv2.imread("solar-system.jpg")

# Add text below each planet
# Syntax: cv2.putText(image, text, org, fontFace, fontScale, color, thickness, lineType)

# Adding text for each planet
cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(img, "Mercury", (120, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Venus", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Earth", (300, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Mars", (400, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (500, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Saturn", (700, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Uranus", (900, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1100, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_system_with_names.jpg", img)

# Destroy all the windows
cv2.destroyAllWindows()