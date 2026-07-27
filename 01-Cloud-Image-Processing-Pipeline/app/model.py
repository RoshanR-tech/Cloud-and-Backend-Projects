import tensorflow as tf
import numpy as np
from PIL import Image

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights="imagenet")


def preprocess_image(image):
    """
    Preprocess the uploaded image before sending it to the model.
    """

    image = image.convert("RGB")
    image = image.resize((224, 224))

    img_array = np.array(image)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def predict_image(image):
    """
    Predict the Top 5 classes for the uploaded image.
    """

    # Preprocess image
    processed = preprocess_image(image)

    # Make prediction
    predictions = model.predict(processed)

    # Decode Top 5 predictions
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(
        predictions,
        top=5
    )[0]

    # Store predictions in a list
    results = []

    for prediction in decoded:
        results.append({
            "class_id": prediction[0],
            "label": prediction[1].replace("_", " ").title(),
            "confidence": round(float(prediction[2]) * 100, 2)
        })

    return results