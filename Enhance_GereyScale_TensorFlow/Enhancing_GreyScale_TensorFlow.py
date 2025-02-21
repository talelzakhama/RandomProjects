import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
from datetime import datetime

def load_model(model_path):
    # Load a pre-trained super-resolution model from a local .pb file
    model = tf.saved_model.load(model_path)
    return model

def ensure_three_channels(img):
    """Ensure the image has three channels."""
    if len(img.shape) == 2:  # It's grayscale
        return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    return img

def preprocess_image(image_path):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = np.array(img, dtype=np.float32)
    img = np.stack((img,) * 3, axis=-1)  # Convert grayscale to 3 channel
    img /= 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def enhance_image(image_path, model_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model = load_model(model_path)
    img = preprocess_image(image_path)
    infer = model.signatures['serving_default']  # Use the appropriate signature key
    super_res_img = infer(tf.constant(img))['rrdb_net']  # Use the correct output tensor name

    # Ensure the output image has three channels
    super_res_img = super_res_img.numpy()[0]
    super_res_img = np.clip(super_res_img, 0, 1)
    super_res_img = (super_res_img * 255).astype(np.uint8)
    super_res_img = ensure_three_channels(super_res_img)  # Ensure image is RGB if needed

    # Check if the image is not already grayscale
    if super_res_img.shape[2] == 3:  # Image has three channels
        super_res_img = cv2.cvtColor(super_res_img, cv2.COLOR_RGB2GRAY)

    # Save and show the enhanced image
    enhanced_image = Image.fromarray(super_res_img)
    enhanced_image.save(f'enhanced_image_{timestamp}.jpg')
    enhanced_image.show()


# Set the path to your model directory and image file
model_path = '/Users/talelzakhama/Downloads/esrgan-tf2-tensorflow2-esrgan-tf2-v1'
# image_path = '/Users/talelzakhama/Desktop/Screenshot 2025-02-20 at 1.52.50 PM.png'
image_path = '/Users/talelzakhama/Downloads/DALL·E 2025-02-20 16.10.45 - A low quality, blurry image of a cityscape at night with indistinct lights and vague outlines of buildings, simulating a poor surveillance camera imag.webp'
enhance_image(image_path, model_path)

