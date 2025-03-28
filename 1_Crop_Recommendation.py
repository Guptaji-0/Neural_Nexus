import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # Import Seaborn
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import google.generativeai as genai  # Import Gemini AI

# ==============================
# 🚀 Load and Prepare the Dataset
# ==============================
df = pd.read_csv("DATA/crop_recommendation.csv")

# Define features and target variable
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']  # Target: Crop Label

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features for better model performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Random Forest Model
RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(X_train, y_train)

# ==============================
# 🚀 Initialize Gemini AI
# ==============================
genai.configure(api_key=" ")  # Add your Gemini API Key 

def ask_gemini(question):
    """Queries Gemini API for crop advice."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(question)
    return response.text if response else "AI is unable to fetch an answer right now."

# ==============================
# 🌿 Streamlit UI
# ==============================

# Sidebar Navigation
st.sidebar.title("🌱 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Want to Grow Another Crop?"])

if page == "Home":
    # 🎨 Title & Description
    st.markdown("<h1 style='text-align: center; color: #008000;'> 🌾 AI-Powered Crop Recommendation System</h1>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<h4 style='text-align: center;'>Enter soil and climate details to predict the best crop</h4>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🌱 Enter Soil & Climate Details")

        # Maintain Inputs Across Refresh
        if "input_values" not in st.session_state:
            st.session_state.input_values = {"N": 0.0, "P": 0.0, "K": 0.0, "temperature": 0.0, "humidity": 0.0, "ph": 0.0, "rainfall": 0.0}

        # User Inputs (Fixed Type Mismatch by Ensuring Floats)
        N = float(st.number_input("🌱 Nitrogen (N)", min_value=0.0, max_value=150.0, step=1.0, value=st.session_state.input_values["N"]))
        P = float(st.number_input("🌾 Phosphorus (P)", min_value=0.0, max_value=150.0, step=1.0, value=st.session_state.input_values["P"]))
        K = float(st.number_input("🍀 Potassium (K)", min_value=0.0, max_value=150.0, step=1.0, value=st.session_state.input_values["K"]))
        temperature = float(st.number_input("🌡️ Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1, value=st.session_state.input_values["temperature"]))
        humidity = float(st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, step=0.1, value=st.session_state.input_values["humidity"]))
        ph = float(st.number_input("🧪 Soil pH", min_value=0.0, max_value=14.0, step=0.1, value=st.session_state.input_values["ph"]))
        rainfall = float(st.number_input("🌧️ Rainfall (mm)", min_value=0.0, max_value=1000.0, step=1.0, value=st.session_state.input_values["rainfall"]))

        # Button to Predict Crop
        if st.button("🔍 Predict Best Crop"):
            st.session_state.input_values = {"N": N, "P": P, "K": K, "temperature": temperature, "humidity": humidity, "ph": ph, "rainfall": rainfall}
            
            input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            input_data_scaled = scaler.transform(input_data)
            
            # Predict crop
            predicted_crop = RF.predict(input_data_scaled)[0]

            # Store in session state to prevent loss on refresh
            st.session_state.predicted_crop = predicted_crop
            st.session_state.show_recommendations = True

    # Show Recommendations
    if st.session_state.get("show_recommendations", False):
        predicted_crop = st.session_state.get("predicted_crop", "Unknown")
        st.success(f"✅ **Recommended Crop:** {predicted_crop}")

        # Generate a trend graph using Seaborn
        st.subheader(f"📈 {predicted_crop} Yield Trend Over Time")

        years = list(range(2010, 2024))
        yield_data = np.random.uniform(2.5, 5.5, len(years))  # Simulating yield data

        # Create a DataFrame for Seaborn
        trend_df = pd.DataFrame({"Year": years, "Yield (Tonnes/Hectare)": yield_data})

        # Seaborn Area Plot
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=trend_df, x="Year", y="Yield (Tonnes/Hectare)", marker='o', color='green', linewidth=2.5, ax=ax)
        ax.fill_between(trend_df["Year"], trend_df["Yield (Tonnes/Hectare)"], alpha=0.3, color='green')

        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Crop Yield (Tonnes/Hectare)", fontsize=12)
        ax.set_title(f"{predicted_crop} Yield Trend (2010-2024)", fontsize=14)
        ax.grid(True, linestyle="--", alpha=0.6)

        st.pyplot(fig)

        # Display AI-generated insights
        with st.expander("💡 AI Insights on Crop Cultivation"):
            ideal_conditions = ask_gemini(f"What are the ideal growing conditions for {predicted_crop}?")
            st.success(f"🌱 **Ideal Growing Conditions for {predicted_crop}:**\n{ideal_conditions}")

            challenges = ask_gemini(f"What are the biggest challenges in growing {predicted_crop}?")
            st.warning(f"⚠️ **Challenges in Growing {predicted_crop}:**\n{challenges}")

elif page == "Want to Grow Another Crop?":
    st.markdown("<h2 style='text-align: center;'>🌾 Choose a Different Crop</h2>", unsafe_allow_html=True)

    other_crop = st.text_input("Enter the name of the crop you want to grow:")

    if st.button("🚀 Get AI Guidance") and other_crop:
        query = f"What changes should a farmer make to grow {other_crop} instead of {st.session_state.get('predicted_crop', 'Unknown')}?"
        st.session_state.ai_guidance = ask_gemini(query)
        st.session_state.show_ai_guidance = True

    if st.session_state.get("show_ai_guidance", False):
        st.info(f"🌱 **AI Guidance for Growing {other_crop}:**\n{st.session_state.ai_guidance}")
