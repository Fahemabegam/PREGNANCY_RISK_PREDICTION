import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import hashlib
import os
import datetime
import re
from io import BytesIO
from pathlib import Path

# Convert your image to base64 (run this once to get the string)
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def show_home_content():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #2e8b57; font-size: 36px; font-weight: 700;">Welcome to Mom's Care</h1>
        <p style="font-size: 18px; color: #555; margin-top: 10px;">Your personal companion for a healthy pregnancy journey</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive welcome section with animation
    st.markdown("""
    <div class="welcome-card" style="background: linear-gradient(135deg, #e6f5e9 0%, #dcede2 100%); 
                padding: 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); 
                margin-bottom: 30px; border-left: 5px solid #3cb371; position: relative; overflow: hidden;">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div style="flex: 2;">
                <h2 style="color: #2e8b57; margin-top: 0;">Hello Mom!</h2>
                <p style="font-size: 16px; line-height: 1.6; color: #333;">
                    We're here to support you through every step of your pregnancy journey.
                    Track your health, get personalized advice, and ensure the well-being of you and your baby.
                </p>
            </div>
            <div style="flex: 1; text-align: right;">
                <img src="data:image/jpg;base64,{your_image_base64_string}" style="border-radius: 10px; max-width: 150px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            </div>
        </div>
    </div>
    """.replace("{your_image_base64_string}", ""), unsafe_allow_html=True)
    
   
    
    # Feature Highlights Section
    st.markdown("<h2 style='color: #2e8b57; margin-top: 20px; margin-bottom: 20px;'>Features</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Feature Card 1
        st.markdown("""
        <div class="feature-card" style="background-color: white; padding: 25px; border-radius: 12px; 
                    box-shadow: 0 3px 10px rgba(0,0,0,0.08); height: 100%; 
                    transition: transform 0.3s ease; border-top: 4px solid #FF9A76;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background-color: #fff3e6; width: 50px; height: 50px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                    <span style="font-size: 24px;">📊</span>
                </div>
                <h3 style="margin: 0; color: #FF9A76;">Risk Prediction</h3>
            </div>
            <p style="font-size: 15px; line-height: 1.5; color: #555;">
                Get personalized risk assessments based on your health metrics. Our advanced 
                algorithm analyzes your data to provide accurate pregnancy risk predictions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        
            
        
        # Feature Card 3
        st.markdown("""
        <div class="feature-card" style="background-color: white; padding: 25px; border-radius: 12px; 
                    box-shadow: 0 3px 10px rgba(0,0,0,0.08); height: 100%; margin-top: 20px;
                    transition: transform 0.3s ease; border-top: 4px solid #68B0AB;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background-color: #e8f4f3; width: 50px; height: 50px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                    <span style="font-size: 24px;">🥗</span>
                </div>
                <h3 style="margin: 0; color: #68B0AB;">Healthy Diet</h3>
            </div>
            <p style="font-size: 15px; line-height: 1.5; color: #555;">
                Access nutritional recommendations customized for each trimester. Learn what foods to eat 
                and avoid for a healthy pregnancy and optimal baby development.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        # Feature Card 2
        st.markdown("""
        <div class="feature-card" style="background-color: white; padding: 25px; border-radius: 12px; 
                    box-shadow: 0 3px 10px rgba(0,0,0,0.08); height: 100%;
                    transition: transform 0.3s ease; border-top: 4px solid #6A7FDB;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background-color: #e8eaf6; width: 50px; height: 50px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                    <span style="font-size: 24px;">📚</span>
                </div>
                <h3 style="margin: 0; color: #6A7FDB;">Trimester Guidance</h3>
            </div>
            <p style="font-size: 15px; line-height: 1.5; color: #555;">
                Week-by-week guidance through your pregnancy journey. Get detailed information about 
                what to expect in each trimester and how to prepare.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        
        
        # Feature Card 4
        st.markdown("""
        <div class="feature-card" style="background-color: white; padding: 25px; border-radius: 12px; 
                    box-shadow: 0 3px 10px rgba(0,0,0,0.08); height: 100%; margin-top: 20px;
                    transition: transform 0.3s ease; border-top: 4px solid #C56183;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <div style="background-color: #f9e9f0; width: 50px; height: 50px; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                    <span style="font-size: 24px;">🧘‍♀️</span>
                </div>
                <h3 style="margin: 0; color: #C56183;">Prenatal Exercises</h3>
            </div>
            <p style="font-size: 15px; line-height: 1.5; color: #555;">
                Safe and effective exercises designed specifically for pregnant women. Maintain your 
                fitness and prepare your body for childbirth with our guided routines.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
            
    
    # Health Tips Carousel Section
    st.markdown("<h2 style='color: #2e8b57; margin-top: 40px; margin-bottom: 20px;'>Today's Health Tips</h2>", unsafe_allow_html=True)
    
    # Simple Tips Carousel Implementation
    tips = [
        {
            "title": "Stay Hydrated",
            "content": "Drink at least 8-10 glasses of water daily to maintain amniotic fluid levels and support your baby's development.",
            "icon": "💧"
        },
        {
            "title": "Take Your Prenatal Vitamins",
            "content": "Don't forget your daily prenatal vitamins to ensure you and your baby get essential nutrients like folic acid.",
            "icon": "💊"
        },
        {
            "title": "Monitor Your Baby's Kicks",
            "content": "From week 28, try to count your baby's movements daily. Aim to feel at least 10 movements within 2 hours.",
            "icon": "👣"
        }
    ]
    
    selected_tip = st.selectbox("Select a tip:", ["Tip 1: Stay Hydrated", "Tip 2: Take Your Prenatal Vitamins", "Tip 3: Monitor Your Baby's Kicks"], key="tip_selector")
    tip_index = int(selected_tip.split(":")[0].replace("Tip ", "")) - 1
    
    st.markdown(f"""
    <div style="background-color: white; padding: 25px; border-radius: 12px; box-shadow: 0 3px 10px rgba(0,0,0,0.08);
                border-left: 4px solid #3cb371; margin-bottom: 30px;">
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="background-color: #e6f5e9; width: 50px; height: 50px; border-radius: 50%; 
                        display: flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 24px;">
                {tips[tip_index]["icon"]}
            </div>
            <h3 style="margin: 0; color: #2e8b57;">{tips[tip_index]["title"]}</h3>
        </div>
        <p style="font-size: 16px; line-height: 1.6; color: #333;">
            {tips[tip_index]["content"]}
        </p>
    </div>
    """, unsafe_allow_html=True)   
    
    # Pregnancy Progress Tracker (Interactive Element)
    st.markdown("<h2 style='color: #2e8b57; margin-top: 40px; margin-bottom: 20px;'>Track Your Pregnancy</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        current_week = st.number_input("Current Week of Pregnancy", min_value=1, max_value=42, value=20, step=1)
    
    with col2:
        # Progress bar calculation
        progress_percentage = min(100, (current_week / 40) * 100)
        trimester = "First" if current_week <= 13 else "Second" if current_week <= 26 else "Third"
        
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 3px 10px rgba(0,0,0,0.08);">
            <p style="margin-bottom: 5px; font-weight: 600;">Week {current_week} • {trimester} Trimester</p>
            <div style="background-color: #f0f0f0; border-radius: 10px; height: 20px; position: relative; overflow: hidden;">
                <div style="background-color: #3cb371; width: {progress_percentage}%; height: 100%; border-radius: 10px;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 5px;">
                <span style="font-size: 12px;">Week 1</span>
                <span style="font-size: 12px;">Week 20</span>
                <span style="font-size: 12px;">Week 40</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # If in the third trimester, show a countdown to due date
    if current_week >= 27:
        weeks_remaining = 40 - current_week
        st.markdown(f"""
        <div style="background-color: #fff3e6; padding: 15px; border-radius: 12px; margin-top: 15px; 
                    border-left: 4px solid #FF9A76; text-align: center;">
            <h3 style="margin: 0; color: #e67e22; font-size: 18px;">Countdown to Due Date</h3>
            <p style="font-size: 24px; font-weight: 700; margin: 10px 0; color: #e67e22;">
                {weeks_remaining} weeks remaining
            </p>
            <p style="font-size: 14px; color: #666; margin: 0;">
                Your baby is almost ready to meet you!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add custom CSS for hover effects
    st.markdown("""
    <style>
        /* Hover effects for feature cards */
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        }
        
        /* Animation for welcome card */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .welcome-card {
            animation: fadeIn 0.8s ease-out;
        }
        
        /* Custom styling for number input */
        .stNumberInput > div > div > input {
            border-color: #3cb371 !important;
            border-radius: 8px !important;
        }
        
        /* Custom styling for selectbox */
        .stSelectbox > div > div {
            border-color: #3cb371 !important;
            border-radius: 8px !important;
        }
        
        /* Button hover effects */
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

# Main app structure
def main():
    # Initialize session state for tab navigation
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "Home"
    
    # App title and styling
    st.set_page_config(
        page_title="Mom's Care - Pregnancy Health App",
        page_icon="👶",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for the whole app
    st.markdown("""
    <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Primary color for buttons */
        .stButton > button {
            background-color: #3cb371;
            color: white;
            border: none;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #32a065;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar with logo and navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #2e8b57;">Mom's Care</h1>
            <p style="color: #666;">Your pregnancy companion</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation menu
        st.subheader("Navigation")
        
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state.active_tab = "Home"
           
            
        if st.button("📊 Risk Assessment", key="nav_risk", use_container_width=True):
            st.session_state.active_tab = "Risk Assessment"
            
            
        if st.button("🔍 Symptoms Search", key="nav_symptoms", use_container_width=True):
            st.session_state.active_tab = "Symptoms"
            
            
        if st.button("🥗 Diet Plans", key="nav_diet", use_container_width=True):
            st.session_state.active_tab = "Diet"
            
            
        if st.button("📚 Pregnancy Guides", key="nav_guides", use_container_width=True):
            st.session_state.active_tab = "Guides"
            
            
        if st.button("🧘‍♀️ Prenatal Exercises", key="nav_exercises", use_container_width=True):
            st.session_state.active_tab = "Exercises"
            
    
    # Main content based on active tab
    if st.session_state.active_tab == "Home":
        show_home_content()
    elif st.session_state.active_tab == "Risk Assessment":
        st.title("Pregnancy Risk Assessment")
        st.write("Here you can assess your pregnancy risk factors...")
        # Your risk assessment functionality here
    elif st.session_state.active_tab == "Symptoms":
        st.title("Symptoms Search")
        st.write("Search for common pregnancy symptoms and solutions...")
        # Your symptoms search functionality here
    elif st.session_state.active_tab == "Diet":
        st.title("Pregnancy Diet Plans")
        st.write("Explore healthy eating plans for each trimester...")
        # Your diet plans functionality here
    elif st.session_state.active_tab == "Guides":
        st.title("Pregnancy Guides")
        st.write("Week-by-week guides for your pregnancy journey...")
        # Your guides functionality here
    elif st.session_state.active_tab == "Exercises":
        st.title("Prenatal Exercises")
        st.write("Safe and effective exercises for pregnant women...")
        # Your exercises functionality here

if __name__ == "__main__":
    main()