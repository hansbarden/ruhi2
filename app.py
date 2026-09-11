import base64
import os
import re
import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit Page Configuration
st.set_page_config(
    page_title="RUHI — a little place made for you",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Styling to make the iframe fill the whole screen without margins
st.markdown("""
    
""", unsafe_allow_html=True)

def encode_image_to_base64(filepath):
    """Convert local image files to base64 string so Streamlit iframe can load them."""
    if not os.path.exists(filepath):
        return filepath
    
    ext = os.path.splitext(filepath)[1].lower().replace('.', '')
    if ext == 'jpg':
        ext = 'jpeg'
        
    with open(filepath, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    return f"data:image/{ext};base64,{encoded}"

def load_and_process_html(html_path):
    """Read ruhi.html and convert image paths into inline Base64 data."""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace all occurrences of "ruhi/pX.jpg" with encoded image data
    def replace_match(match):
        img_path = match.group(1)
        return f'"{encode_image_to_base64(img_path)}"'

    processed_content = re.sub(r'["\'](ruhi/[^"\']+)["\']', replace_match, content)
    return processed_content

# 3. Render HTML
if os.path.exists("ruhi.html"):
    html_data = load_and_process_html("ruhi.html")
    components.html(html_data, height=1200, scrolling=True)
else:
    st.error("ruhi.html file not found in the root directory.")
