import streamlit as st
import google.generativeai as genai

# 🎯 Configure Gemini API Key (Replace with your actual API key)
GEMINI_API_KEY = "AIzaSyC43bxonVWRd0v-cDb8dORqqGSm4lGutC8"  # Add your API key here 
genai.configure(api_key=GEMINI_API_KEY)

# 🌾 Available Crop Types (Dropdown options)
crop_types = [
    'Rice', 'Jowar(Sorghum)', 'Barley(JAV)', 'Maize', 'Ragi( naachnnii)',
    'Chickpeas(Channa)', 'French Beans(Farasbi)', 'Fava beans (Papdi - Val)',
    'Lima beans(Pavta)', 'Cluster Beans(Gavar)'
]

# ================================
# 🌱 Streamlit UI
# ================================

st.set_page_config(page_title="Fertilizer Recommendation", page_icon="🌿", layout="centered")

# 🎨 Title & Description
st.markdown("<h1 style='text-align: center; color: #008000;'>🌿 Fertilizer Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter soil parameters to get the best fertilizer recommendation for your crop.</p>", unsafe_allow_html=True)
st.divider()

# 📌 Crop Selection Dropdown
crop = st.selectbox("🔽 Select a Crop Type", crop_types)

# 🧪 Soil Parameter Inputs
col1, col2 = st.columns(2)
with col1:
    nitrogen = st.number_input("🌱 Enter Nitrogen (N) value", min_value=0.0, format="%.2f")
    potassium = st.number_input("🍀 Enter Potassium (K) value", min_value=0.0, format="%.2f")

with col2:
    phosphorus = st.number_input("🌾 Enter Phosphorus (P) value", min_value=0.0, format="%.2f")
    ph = st.number_input("🧪 Enter Soil pH Level", min_value=0.0, format="%.2f")

# ================================
# 🚀 Gemini AI Fertilizer Recommendation
# ================================
def get_fertilizer_recommendation(crop, nitrogen, phosphorus, potassium, ph):
    """Queries Gemini AI for fertilizer recommendation."""
    prompt = (
        f"Crop: {crop}\n"
        f"Soil Nitrogen (N): {nitrogen}\n"
        f"Soil Phosphorus (P): {phosphorus}\n"
        f"Soil Potassium (K): {potassium}\n"
        f"Soil pH: {ph}\n"
        "\nBased on these soil conditions, recommend the best fertilizers to improve crop yield."
    )

    model = genai.GenerativeModel("gemini-2.0-flash")  # Using Gemini AI for predictions
    response = model.generate_content(prompt)
    return response.text if response else "No recommendation received."

# 🌱 Organic Solution Recommendation
def get_organic_recommendation(crop, nitrogen, phosphorus, potassium, ph):
    """Queries Gemini AI for organic fertilizer solutions."""
    prompt = (
        f"Crop: {crop}\n"
        f"Soil Nitrogen (N): {nitrogen}\n"
        f"Soil Phosphorus (P): {phosphorus}\n"
        f"Soil Potassium (K): {potassium}\n"
        f"Soil pH: {ph}\n"
        "\nBased on these soil conditions, recommend natural or organic fertilizers to improve soil health and crop yield."
    )

    model = genai.GenerativeModel("gemini-2.0-flash")  # Using Gemini AI for organic recommendations
    response = model.generate_content(prompt)
    return response.text if response else "No organic solution available."

# 📌 Generate Recommendation Button
if st.button("📊 Get Fertilizer Recommendation"):
    if nitrogen and phosphorus and potassium and ph:
        recommendation = get_fertilizer_recommendation(crop, nitrogen, phosphorus, potassium, ph)
        
        # 🎯 Display Recommendation in a Styled Card
        st.markdown(
            f"""
            <div style="background-color: #d4edda; color: #155724; padding: 15px; border-radius: 10px; 
            border-left: 5px solid #28a745; font-weight: bold;">
            ✅ <strong>Fertilizer Recommendation for {crop}</strong> <br>{recommendation}
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.error("⚠️ Please enter valid values for all soil parameters!")

# 📌 Organic Solution Button
if st.button("🌿 Get Organic Solution"):
    if nitrogen and phosphorus and potassium and ph:
        organic_solution = get_organic_recommendation(crop, nitrogen, phosphorus, potassium, ph)
        
        # 🎯 Display Organic Solution in a Styled Card
        st.markdown(
            f"""
            <div style="background-color: #f8f9fa; color: #155724; padding: 15px; border-radius: 10px; 
            border-left: 5px solid #198754; font-weight: bold;">
            🍃 <strong>Organic Fertilizer Recommendation for {crop}</strong> <br>{organic_solution}
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.error("⚠️ Please enter valid values for all soil parameters!")
