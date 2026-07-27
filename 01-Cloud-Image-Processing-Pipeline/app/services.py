from app.model import predict_image
import cv2
import os


UPLOAD_FOLDER = "uploads"


def process_image(file_path, filename):

    image = cv2.imread(file_path)

    if image is None:
        return None

    height, width, channels = image.shape

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_filename = "gray_" + filename
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, gray_filename), gray_image)

    resized_image = cv2.resize(image, (512, 512))
    resized_filename = "resized_" + filename
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, resized_filename), resized_image)

    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    blurred_filename = "blurred_" + filename
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, blurred_filename), blurred_image)

    edges_image = cv2.Canny(gray_image, 100, 200)
    edges_filename = "edges_" + filename
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, edges_filename), edges_image)

    return {
        "filename": filename,
        "width": width,
        "height": height,
        "channels": channels,
        "grayscale_image": gray_filename,
        "resized_image": resized_filename,
        "blurred_image": blurred_filename,
        "edges_image": edges_filename
    }