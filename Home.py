import streamlit as st

# ✅ Set Page Title & Layout
st.set_page_config(
    page_title="🌾 Smart Agriculture Assistant",
    page_icon="🌱",
    layout="wide"
)

# ✅ Sidebar with Enhanced UI
st.sidebar.image("Graphics/Logo.jpeg", use_column_width=True)  # Add your logo (Replace with actual image)
st.sidebar.markdown("<h2 style='text-align: center; color: #4CAF50;'>🌱 Smart Agriculture Assistant</h2>", unsafe_allow_html=True)

# 📌 Sidebar Sections
st.sidebar.markdown("---")  # Divider
st.sidebar.markdown("## 🏠 **Home**")
if st.sidebar.button("🏡 Home"):
    st.rerun()  # ✅ Correct function in latest Streamlit versions


st.sidebar.markdown("---")  # Divider

st.sidebar.markdown("## 🌾 **Core Features**")
st.sidebar.markdown("🔍 **AI-Powered Tools:**")

# 📌 Features List
st.sidebar.markdown("📌 **1. Crop Suggestion**")
st.sidebar.markdown("📌 **2. Yield Prediction**")
st.sidebar.markdown("📌 **3. Price Prediction**")
st.sidebar.markdown("📌 **4. Plant Disease Detection**")
st.sidebar.markdown("📌 **5. Fertilizer Recommendation**")
st.sidebar.markdown("📌 **6. Insurance Claim Prediction**")

st.sidebar.markdown("---")  # Divider

st.sidebar.markdown("## 📞 **Need Help?**")
st.sidebar.info("💬 Contact Support at: **support@agriassist.com**")

# ✅ Home Page Content
#st.title("🏡 Welcome To AgroTechHub")
st.markdown("<h1 style='text-align: center; color: #008000;'> 🏡 AgroTechHub</h1>", unsafe_allow_html=True)
st.markdown("""
🌱 **Empowering Farmers with AI & Data-Driven Insights!**  
🔍 Explore cutting-edge agricultural tools designed to **boost productivity, reduce risks, and maximize profits**.
""")


# ✅ Problem Statement
st.header("🚨 The Problem")
st.write("""
🌍 **Agriculture is the backbone of our economy, but farmers face critical challenges:**  
- **Unpredictable crop yields** due to climate change & poor planning  
- **Price fluctuations** leading to losses for farmers  
- **Plant diseases** destroying crops & reducing productivity  
- **Lack of data-driven decision-making** for choosing crops, fertilizers, and insurance  
- **Difficulties in claiming crop insurance** due to complex policies  

These challenges **lead to financial losses, food shortages, and economic instability**.
""")

# ✅ Significance of the Problem
st.header("📊 Why Is This Important?")
st.write("""
✅ **50%+ of farmers lack access to modern technology** and make decisions based on intuition.  
✅ **Crop diseases cause 30-40% yield losses globally** every year.  
✅ **Over 60% of insurance claims get rejected** due to improper documentation or incorrect estimates.  
✅ **Farmers struggle to get real-time market price predictions**, leading to losses.  

By solving these issues, we can **increase farmer income, optimize resources, and ensure food security.**  
""")

# ✅ Our Solution: Smart Agriculture Assistant
st.header("🌟 Our Solution: AI-Powered Farming")
st.write("""
The **Smart Agriculture Assistant** is an **AI-driven decision-making tool** that helps farmers **increase efficiency, minimize risks, and maximize profits.**  

### 🔥 **How We Solve It?**
✔ **Crop Suggestion** – AI recommends the best crop based on **soil & weather conditions**  
✔ **Yield Prediction** – Estimate crop output **before planting** to plan effectively  
✔ **Price Prediction** – Predict **market trends** & get the best price for crops  
✔ **Plant Disease Detection** – Upload an image & detect **diseases instantly**  
✔ **Fertilizer Recommendation** – Find the best **fertilizer for maximum yield**  
✔ **Insurance Claim Prediction** – Check if **your crop insurance will be approved**  

With **data-driven insights**, farmers can make **smarter, faster, and more profitable decisions.** 🚀  
""")

# ✅ Features Overview
st.header("🛠️ How to Use the App?")

## 1️⃣ Crop Suggestion
st.subheader("🌱 1. Crop Suggestion")
st.write("""
**Find the Best Crop for Your Soil & Climate**  
Based on **soil type, temperature, and rainfall**, the app suggests the most **suitable crop** for your land.
""")
st.info("📌 Example: If you enter Soil Type = 'Clay', Temperature = 28°C, Rainfall = 200mm, the model might suggest growing 'Rice'.")

## 2️⃣ Yield Prediction
st.subheader("🌾 2. Yield Prediction")
st.write("""
**Estimate Your Crop Production Output**  
Enter details like **crop type, area size, and weather conditions**, and the model predicts **expected yield (kg/hectare)**.
""")
st.info("📌 Example: If you enter Crop = 'Wheat', Area = 5 Hectares, Temperature = 25°C, Rainfall = 150mm, the model might predict '4.2 tons'.")  

## 3️⃣ Price Prediction
st.subheader("💰 3. Crop Price Prediction")
st.write("""
**Get Future Price Estimates for Your Crops**  
Based on **market trends, past prices, and weather**, the model predicts **expected selling prices**.
""")
st.info("📌 Example: If you enter Crop = 'Tomato', Month = 'December', Region = 'Delhi', it might predict a price of '$1.5 per kg'.")

## 4️⃣ Plant Disease Detection
st.subheader("🦠 4. Plant Disease Detection")
st.write("""
**Detect & Identify Crop Diseases Using AI**  
Upload an **image of your infected plant**, and the AI will detect the disease and suggest possible treatments.
""")
st.info("📌 Example: Upload a picture of a **leaf with brown spots**, and the model may detect 'Leaf Blight' with a solution.")

## 5️⃣ Fertilizer Suggestion
st.subheader("🌿 5. Fertilizer Recommendation")
st.write("""
**Get the Best Fertilizer for Maximum Yield**  
Based on **soil nutrients (N, P, K), crop type, and weather conditions**, the model recommends the best **fertilizer**.
""")
st.info("📌 Example: If your **Nitrogen is low**, it may suggest 'Urea' fertilizer.")

## 6️⃣ Insurance Claim Prediction
st.subheader("📜 6. Insurance Claim Prediction")
st.write("""
**Check if Your Insurance Claim Will Be Approved**  
Enter details like **crop type, location, damage type, and claim amount**, and the AI predicts if your claim will be **approved or rejected**.
""")
st.info("📌 Example: If you enter Crop = 'Corn', Damage = 'Flood', Claim Amount = $5000, the model might predict 'Claim Approved ✅'.")

# ✅ Call to Action
st.header("🚀 Get Started!")
st.write("""
Select a feature from the **sidebar** and start making data-driven agricultural decisions today! 🌱
""")
