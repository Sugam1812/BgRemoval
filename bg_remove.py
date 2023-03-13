import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set page configuration
st.set_page_config(page_title='Background Remover', page_icon=':camera:', layout='wide')

# Set page title and description
st.write('# Background Remover')
st.write('Remove the background from your images!')

# Create a file uploader widget
uploaded_file = st.file_uploader('Choose an image file', type=['jpg', 'jpeg', 'png'])

# Define a function to remove background from the image
def remove_background(image):
    # Load the image
    img = Image.open(io.BytesIO(image))

    # Remove the background
    result = remove(img)

    # Return the result as bytes
    buffered = io.BytesIO()
    result.save(buffered, format='PNG')
    return buffered.getvalue()

# Display the uploaded image and the result
if uploaded_file is not None:
    # Remove the background from the uploaded image
    image_bytes = uploaded_file.read()
    result_bytes = remove_background(image_bytes)

    # Display the images side by side
    st.image([Image.open(io.BytesIO(image_bytes)), Image.open(io.BytesIO(result_bytes))], 
             caption=['Original Image', 'Background Removed'], width=300)
else:
    st.write('Upload an image to get started!')
