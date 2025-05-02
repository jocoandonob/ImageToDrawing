import cv2
import numpy as np
import base64
from PIL import Image
import io
import requests

def pencil_sketch(img):
    """Convert image to pencil sketch"""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted = 255 - gray
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred = 255 - blurred
    
    # Create the pencil sketch image
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    
    return sketch

def pen_sketch(img):
    """Convert image to pen sketch with more defined edges"""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 8
    )
    
    return edges

# Oil painting and watercolor effects removed due to compatibility issues

def convert_to_drawing(img, style="Pencil Sketch"):
    """Convert image to drawing based on selected style"""
    # Ensure image is in BGR format for OpenCV processing
    if len(img.shape) == 2:  # Grayscale
        img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:  # RGBA
        img_rgb = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    elif img.shape[2] == 3:  # RGB
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Apply selected style
    if style == "Pencil Sketch":
        result = pencil_sketch(img_bgr)
        # Convert back to RGB for display
        if len(result.shape) == 2:  # Grayscale result
            result_rgb = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
        else:
            result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    
    elif style == "Pen Sketch":
        result = pen_sketch(img_bgr)
        # Convert back to RGB for display
        result_rgb = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
    
    else:
        # Default to pencil sketch if style not recognized
        result = pencil_sketch(img_bgr)
        # Convert back to RGB for display
        result_rgb = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
    
    return result_rgb

def generate_download_link(img_array, filename, link_text):
    """Generate HTML link to download the image"""
    # Convert the image array to PIL Image
    if isinstance(img_array, np.ndarray):
        img = Image.fromarray(img_array)
    else:
        img = img_array
    
    # Save image to bytes buffer
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG", quality=90)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    # Create download link
    href = f'<a href="data:file/jpg;base64,{img_str}" download="{filename}">{link_text}</a>'
    
    return href
