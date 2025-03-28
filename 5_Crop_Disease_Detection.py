import streamlit as st
import google.generativeai as genai
from pathlib import Path
import base64
import os

# ================================
# 🚀 Configure Google Gemini API
# ================================
GEMINI_API_KEY = "AIzaSyC43bxonVWRd0v-cDb8dORqqGSm4lGutC8"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# ================================
# 🚀 Model Configuration
# ================================
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {"category": f"HARM_CATEGORY_{category}", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
    for category in ["HARASSMENT", "HATE_SPEECH", "SEXUALLY_EXPLICIT", "DANGEROUS_CONTENT"]
]

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# ================================
# 🚀 Function to Read Image Data
# ================================
def read_image_data(image_file):
    return {"mime_type": "image/jpeg", "data": image_file.read()}

# ================================
# 🚀 Function to Get AI Response
# ================================
def generate_gemini_response(prompt, image_data):
    response = model.generate_content([prompt, image_data])
    return response.text if response else "No response received."

# ================================
# 🚀 Plant Pathology Prompt
# ================================
input_prompt = """
As a highly skilled plant pathologist, your expertise is indispensable in our pursuit of maintaining optimal plant health.
You will be provided with information or samples related to plant diseases, and your role involves conducting a detailed analysis to identify the specific issues, propose solutions, and offer recommendations.

**Analysis Guidelines:**
1. **Disease Identification:** Examine the provided image to accurately identify plant diseases.
2. **Detailed Findings:** Provide in-depth details on affected plant parts, symptoms, and potential causes.
3. **Treatment Suggestions:** Suggest treatment options, preventive measures, or further investigations.
4. **Prevention Strategies:** Offer recommendations to maintain plant health and prevent future diseases.

**Disclaimer:**
*"Please note that this analysis is based on AI predictions and should not replace professional agricultural advice. Consult with experts before implementing any treatments."*
"""

# ================================
# 🚀 Streamlit UI
# ================================
st.set_page_config(page_title="🌿 Plant Disease Detector", layout="wide")


st.markdown("<h1 style='text-align: center; color: #008000;'> 🌿 AI-Powered Plant Disease Detector </h1>", unsafe_allow_html=True)
st.divider()

st.subheader("🔍 Upload an image of a plant leaf to detect potential diseases.")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["📸 Upload Image", "ℹ️ About"])

# ================================
# 🚀 Image Upload Section
# ================================
if page == "📸 Upload Image":
    uploaded_image = st.file_uploader("📤 Upload an image of the affected plant", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        # Display Uploaded Image
        st.image(uploaded_image, caption="📷 Uploaded Image", use_column_width=True)

        # Convert image for AI processing
        image_data = read_image_data(uploaded_image)

        # Analyze Image with AI
        if st.button("🔍 Analyze Plant Health"):
            with st.spinner("🧠 Analyzing the plant health..."):
                response = generate_gemini_response(input_prompt, image_data)

                # Display AI Analysis in a Card
                st.markdown(
                    f"""
                    <div style="background-color:#f9f9f9;padding:15px;border-radius:10px;border:1px solid #ddd;">
                        <h4>📢 AI-Powered Plant Disease Report</h4>
                        <p>{response}</p>
                    </div>
                    """, unsafe_allow_html=True
                )

# ================================
# ℹ️ About Section
# ================================
elif page == "ℹ️ About":
    st.write("""
    This AI-powered tool helps farmers and researchers identify plant diseases by analyzing leaf images.
    - 🌱 Upload an image of an affected plant.
    - 🤖 AI will analyze and provide insights.
    - 🚀 Powered by **Google Gemini AI**.
    """)
