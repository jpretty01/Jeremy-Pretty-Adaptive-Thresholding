# Jeremy Pretty
# CSC 515 Adaptive Thresholding
import cv2
import os


# East function
def adaptive_thresholding(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    thresholded_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Display the original and thresholded images
    cv2.imshow(f"Original Image: {image_path}", image)
    cv2.imshow(f"Adaptive Thresholded Image: {image_path}", thresholded_image)

if __name__ == "__main__":

    # Created paths to all the photos
    indoor_image_path= os.path.join(os.path.dirname(__file__), 'indoor.jpg')
    outdoor_image_path = os.path.join(os.path.dirname(__file__), 'outdoor.jpg')
    close_up_image_path = os.path.join(os.path.dirname(__file__), 'closeup.jpg')

    adaptive_thresholding(indoor_image_path)
    adaptive_thresholding(outdoor_image_path)
    adaptive_thresholding(close_up_image_path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
