import streamlit as st
import cv2
import numpy as np
import io
from PIL import Image
import tempfile
import base64
from utils import convert_to_drawing, generate_download_link

# Set page configuration
st.set_page_config(
    page_title="Image to Drawing Converter",
    page_icon="✏️",
    layout="wide"
)

# Main title
st.title("📷 Image to Drawing Converter 🖌️")

# Description
st.markdown("""
This app transforms your photos into artistic drawings using AI. 
Upload an image and see it converted into a beautiful sketch!
""")

# Sidebar with options
st.sidebar.title("Drawing Style Options")
drawing_style = st.sidebar.selectbox(
    "Select Drawing Style", 
    ["Pencil Sketch", "Pen Sketch"]
)

# Image uploader
uploaded_file = st.file_uploader("Choose an image file...", type=['jpg', 'jpeg', 'png'])

# Processing state tracking
processing = False

if uploaded_file is not None:
    try:
        # Read image
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        
        # Create columns for displaying images
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)
        
        # Processing button
        if st.button("Convert to Drawing"):
            processing = True
            
            with st.spinner(f"Converting to {drawing_style}..."):
                # Convert image based on selected style
                result_image = convert_to_drawing(img_array, style=drawing_style)
                
                # Display the result
                with col2:
                    st.subheader(f"{drawing_style} Result")
                    st.image(result_image, use_container_width=True)
                    
                    # Create download link
                    download_link = generate_download_link(
                        result_image, 
                        f"drawing_{drawing_style.lower().replace(' ', '_')}.jpg", 
                        "Download Drawing"
                    )
                    st.markdown(download_link, unsafe_allow_html=True)
                
                processing = False
    
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        processing = False

# Information section
st.markdown("---")
st.markdown("""
### How it works
This application uses computer vision techniques and pre-trained models to transform your photos into different drawing styles.

### Tips for best results:
- Use clear images with good lighting
- Images with distinct features work best
- For detailed sketches, choose higher resolution images
""")
