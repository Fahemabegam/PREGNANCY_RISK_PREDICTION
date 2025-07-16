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

# Set the page configuration
st.set_page_config(
    page_title="Mom's Care",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Create folders for user data and models if they don't exist
if not os.path.exists("user_data"):
    os.makedirs("user_data")

# Path to the user database
USER_DB_PATH = "user_data/users.csv"

# Initialize session state variables if they don't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = "login"  # Start with login page by default
if 'registration_success' not in st.session_state:
    st.session_state.registration_success = False
if 'login_success' not in st.session_state:
    st.session_state.login_success = False
if 'current_username' not in st.session_state:
    st.session_state.current_username = ""

# Function to create user database if it doesn't exist
def initialize_user_db():
    if not os.path.exists(USER_DB_PATH):
        # Create an empty DataFrame with the required columns
        df = pd.DataFrame(columns=[
            'name', 'username', 'email', 'password_hash', 
            'gender', 'date_of_birth', 'relation_to_patient',
            'country', 'state', 'hospital_name'
        ])
        df.to_csv(USER_DB_PATH, index=False)

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to validate email format
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Function to validate password strength
def is_strong_password(password):
    # At least 8 characters, with at least one uppercase, one lowercase, and one number
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

# Function to check if username already exists
def username_exists(username):
    if os.path.exists(USER_DB_PATH):
        df = pd.read_csv(USER_DB_PATH)
        return username in df['username'].values
    return False

# Function to check if email already exists
def email_exists(email):
    if os.path.exists(USER_DB_PATH):
        df = pd.read_csv(USER_DB_PATH)
        return email in df['email'].values
    return False

# Function to register a new user
def register_user(name, username, email, password, gender, dob, country, state, hospital_name, relation_to_patient=None):
    # Hash the password
    password_hash = hash_password(password)
    
    # Load existing data or create new DataFrame
    if os.path.exists(USER_DB_PATH):
        df = pd.read_csv(USER_DB_PATH)
    else:
        df = pd.DataFrame(columns=[
            'name', 'username', 'email', 'password_hash', 
            'gender', 'date_of_birth', 'relation_to_patient',
            'country', 'state', 'hospital_name'
        ])
    
    # Add new user
    new_user = {
        'name': name,
        'username': username,
        'email': email,
        'password_hash': password_hash,
        'gender': gender,
        'date_of_birth': dob,
        'relation_to_patient': relation_to_patient,
        'country': country,
        'state': state,
        'hospital_name': hospital_name
    }
    
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_csv(USER_DB_PATH, index=False)
    return True

# Function to authenticate user
def authenticate_user(username, password):
    if not os.path.exists(USER_DB_PATH):
        return False
    
    df = pd.read_csv(USER_DB_PATH)
    
    if username not in df['username'].values:
        return False
    
    user_data = df[df['username'] == username].iloc[0]
    password_hash = hash_password(password)
    
    return password_hash == user_data['password_hash']

# Function to get user data
def get_user_data(username):
    df = pd.read_csv(USER_DB_PATH)
    return df[df['username'] == username].iloc[0]

# Initialize the user database
initialize_user_db()

# Custom CSS styling combining both apps
st.markdown(
    """
    <style>
    /* Base styling for auth pages */
    :root {
        --pastel-green-light: #E6F5E9;
        --pastel-green: #A8D5BA;
        --pastel-green-dark: #7DC49A;
        --pastel-green-darker: #57A77B;
        --text-dark: #2C3E50;
        --text-light: #FFFFFF;
        --error-color: #FF6B6B;
        --success-color: #66BB6A;
        --warning-color: #FFA726;
    }

    body {
        color: var(--text-dark);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Header styling */
    .main-header {
        font-size: 2.5rem;
        color: var(--pastel-green-darker);
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    /* Form container */
    .form-container {
        background-color: var(--pastel-green-light);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid var(--pastel-green);
    }

    /* Dashboard container */
    .dashboard-container {
        background-color: var(--pastel-green-light);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid var(--pastel-green);
    }

    /* Form inputs */
    div[data-baseweb="input"] {
        border-radius: 8px !important;
        border: 1px solid var(--pastel-green) !important;
    }

    .stTextInput input {
        border-radius: 8px !important;
        padding: 10px !important;
        border: 1px solid var(--pastel-green) !important;
    }

    .stTextInput input:focus {
        border: 2px solid var(--pastel-green-dark) !important;
        box-shadow: 0 0 5px rgba(168, 213, 186, 0.5) !important;
    }

    .stSelectbox, div[data-baseweb="select"] {
        border-radius: 8px !important;
    }

    /* Buttons styling */
    .stButton button {
        background-color: var(--pastel-green) !important;
        color: var(--text-dark) !important;
        border-radius: 10px !important;
        padding: 10px 15px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        width: 100%;
        margin-top: 10px;
    }

    .stButton button:hover {
        background-color: var(--pastel-green-dark) !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        transform: translateY(-2px) !important;
    }

    /* Messages */
    .success-message {
        background-color: rgba(102, 187, 106, 0.2);
        border-left: 5px solid var(--success-color);
        color: #2E7D32;
        font-weight: 600;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }

    .error-message {
        background-color: rgba(255, 107, 107, 0.2);
        border-left: 5px solid var(--error-color);
        color: #D32F2F;
        font-weight: 600;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }

    /* Info Fields for Dashboard */
    .info-field {
        padding: 12px;
        background-color: white;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid var(--pastel-green-dark);
    }

    .info-label {
        font-weight: 600;
        color: var(--pastel-green-darker);
    }

    .info-value {
        font-weight: 400;
        color: var(--text-dark);
    }

    /* Logo and branding */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .logo {
        height: 80px;
        width: 80px;
        background-color: var(--pastel-green-dark);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 40px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* Divider */
    .divider {
        height: 1px;
        background-color: var(--pastel-green);
        margin: 20px 0;
    }

    /* Link styling */
    .link-text {
        text-align: center;
        margin-top: 15px;
        color: var(--pastel-green-darker);
        cursor: pointer;
        text-decoration: underline;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 20px 0;
        font-size: 0.8rem;
        color: #6c757d;
    }
    
    /* Home Page Styling from Mom's Care */
    .stTextInput>div>div>input {
        background-color: whitesmoke;
        color: black !important;
        border-radius: 6px;
        border: 1px solid #dcede2;
    }

    .stButton>button {
        background-color: #3cb371;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: 600;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .stButton>button:hover {
        background-color: #2e8b57;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    .stMarkdown {
        color: #2e8b57;
    }

    .stRadio>div>label {
        color: #2e8b57 !important;
    }

    .stSuccess {
        color: #2e8b57;
    }

    .stError {
        color: #ff4b4b;
    }

    .stTextInput>label, .stNumberInput>label {
        color: #2e8b57 !important;
        font-weight: bold;
        font-size: 15px !important;
        margin-bottom: 5px;
    }

    h1 {
        color: #2e8b57 !important;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 20px;
    }

    .stMarkdown h3 {
        color: #2e8b57 !important;
        font-weight: 600;
    }

    /* Number input styling */
    .stNumberInput > div > div > input {
        background-color: #f5faf7;
        border: 1px solid #dcede2;
        border-radius: 6px;
        padding: 6px 12px;
        color: #2e8b57 !important;
    }

    /* Improved header styling */
    h1, h2, h3, h4, h5, h6 {
        color: #2e8b57 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Dark pastel green navbar styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 40px;
        padding: 12px 20px;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        border-bottom: 3px solid #1d5e3a;
        margin-bottom: 20px;
    }

    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.85) !important;
        transition: all 0.3s ease;
    }

    /* Style the active tab */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #3cb371;
        border-radius: 8px;
        color: white !important;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }

    /* Style the first tab (Mum's Care) differently */
    .stTabs [data-baseweb="tab"]:first-child {
        background-color: #3cb371;
        border-radius: 8px;
        font-weight: bold;
        color: white !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.15);
        transform: scale(1.05);
        letter-spacing: 0.5px;
        border-bottom: none;
    }

    /* Style tab hover effects */
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #3cb371;
        border-radius: 8px;
        color: white !important;
        transform: translateY(-2px);
    }

    /* App header */
    .app-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #e6f3e6;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-bottom: 3px solid #3cb371;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    }

    .app-title {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .app-title img {
        height: 36px;
    }
    
    /* Logout button styling */
    .logout-btn {
        background-color: #3cb371;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        cursor: pointer;
    }
    
    .logout-btn:hover {
        background-color: #2e8b57;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Card-like sections */
    .content-card {
        background-color: #f5faf7;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 4px solid #3cb371;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# List of countries
countries = [
    "Select Country", "United States", "Canada", "United Kingdom", "Australia", 
    "India", "China", "Japan", "Germany", "France", "Brazil", "Other"
]

# Dictionary of states by country
states_by_country = {
    "United States": [
        "Select State", "Alabama", "Alaska", "Arizona", "Arkansas", "California", 
        "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", 
        "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
        "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", 
        "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
        "Wisconsin", "Wyoming"
    ],
    "Canada": [
        "Select Province", "Alberta", "British Columbia", "Manitoba", "New Brunswick", 
        "Newfoundland and Labrador", "Northwest Territories", "Nova Scotia", "Nunavut", 
        "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon"
    ],
    "United Kingdom": [
        "Select Region", "England", "Scotland", "Wales", "Northern Ireland"
    ],
    "Australia": [
        "Select State", "Australian Capital Territory", "New South Wales", "Northern Territory", 
        "Queensland", "South Australia", "Tasmania", "Victoria", "Western Australia"
    ],
    "India": [
        "Select State", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", 
        "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", 
        "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
        "Uttarakhand", "West Bengal", "Union Territories"
    ],
    "Other": ["Not Applicable"]
}

# Default state options
default_states = ["Select State/Province/Region"]

# Function to display logo
def display_logo():
    st.markdown("""
    <div class="logo-container">
        <div class="logo">MC</div>
    </div>
    """, unsafe_allow_html=True)

# Function to switch to login page
def switch_to_login():
    st.session_state.current_page = "login"

# Function to switch to register page
def switch_to_register():
    st.session_state.current_page = "register"

# Function to switch to home page
def switch_to_home():
    st.session_state.current_page = "home"
    
# Function to handle logout
def logout():
    # Reset all the important session state variables
    st.session_state.login_success = False
    st.session_state.current_username = ""
    st.session_state.current_page = "login"    

# Registration Page
def registration_page():
    display_logo()
    st.markdown("<h1 class='main-header'>Mom's Care Registration</h1>", unsafe_allow_html=True)
        
    with st.form("registration_form", clear_on_submit=False):
            st.markdown("<div class='form-container'>", unsafe_allow_html=True)
            
            # Personal Information
            st.subheader("Personal Information")
            name = st.text_input("Full Name")
            
            # Two columns for username and email
            col_user, col_email = st.columns(2)
            with col_user:
                username = st.text_input("Username")
            with col_email:
                email = st.text_input("Email")
            
            # Two columns for password fields
            col_pass, col_confirm = st.columns(2)
            with col_pass:
                password = st.text_input("Password", type="password")
            with col_confirm:
                confirm_password = st.text_input("Confirm Password", type="password")
            
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            
            # Additional Information
            st.subheader("Additional Information")
            
            # Two columns for gender and DOB
            col_gender, col_dob = st.columns(2)
            with col_gender:
                gender = st.selectbox("Gender", ["Select Gender", "Female", "Male"])
            with col_dob:
                dob = st.date_input("Date of Birth", min_value=datetime.date(1900, 1, 1), 
                                   max_value=datetime.date.today())
            
            relation_to_patient = "None"
            if gender == "Male":
                relation_to_patient = st.selectbox("Relation to Patient", ["Select Relation", "Husband", "Father", "Brother"])
            
            # Hospital information
            st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
            st.subheader("Hospital Information")
            hospital_name = st.text_input("Hospital Name")
            
            # Location information with two columns
            col_country, col_state = st.columns(2)
            with col_country:
                country = st.selectbox("Country", countries)
            
            # Dynamically update state options based on selected country
            with col_state:
                if country != "Select Country" and country in states_by_country:
                    state_options = states_by_country[country]
                else:
                    state_options = default_states
                
                state = st.selectbox("State/Province/Region", state_options)
            
            st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
            submit_button = st.form_submit_button(label="Create Account")
            
            if submit_button:
                # Validate inputs
                if not name or not username or not email or not password or not gender or gender == "Select Gender" or not hospital_name:
                    st.markdown("<p class='error-message'>Please fill all required fields</p>", unsafe_allow_html=True)
                elif password != confirm_password:
                    st.markdown("<p class='error-message'>Passwords do not match</p>", unsafe_allow_html=True)
                elif not is_valid_email(email):
                    st.markdown("<p class='error-message'>Please enter a valid email address</p>", unsafe_allow_html=True)
                elif not is_strong_password(password):
                    st.markdown("<p class='error-message'>Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number</p>", unsafe_allow_html=True)
                elif username_exists(username):
                    st.markdown("<p class='error-message'>Username already exists. Please choose a different username.</p>", unsafe_allow_html=True)
                elif email_exists(email):
                    st.markdown("<p class='error-message'>Email already exists. Please use a different email.</p>", unsafe_allow_html=True)
                elif gender == "Male" and (not relation_to_patient or relation_to_patient == "Select Relation"):
                    st.markdown("<p class='error-message'>Please select your relation to the patient</p>", unsafe_allow_html=True)
                elif country == "Select Country":
                    st.markdown("<p class='error-message'>Please select your country</p>", unsafe_allow_html=True)
                elif state == "Select State" or state == "Select Province" or state == "Select Region" or state == "Select State/Province/Region":
                    st.markdown("<p class='error-message'>Please select your state/province/region</p>", unsafe_allow_html=True)
                else:
                    # All validations passed, register the user
                    register_user(name, username, email, password, gender, dob.strftime('%Y-%m-%d'), country, state, hospital_name, relation_to_patient)
                    st.session_state.registration_success = True
                    st.session_state.current_page = "login"
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Account Login Link
    st.markdown("<p class='link-text' onclick='document.getElementById(\"login_link\").click()'>Already have an account? Login here</p>", unsafe_allow_html=True)
        
        # Hidden button for JavaScript to click
    if st.button("Login", key="login_link", help="Switch to login page"):
            switch_to_login()


# Login Page
def login_page():
    display_logo()
    st.markdown("<h1 class='main-header'>Mom's Care Login</h1>", unsafe_allow_html=True)
    
    # Registration success message
    if st.session_state.registration_success:
        st.markdown("<p class='success-message'>Registration successful! Please log in with your credentials.</p>", unsafe_allow_html=True)
        st.session_state.registration_success = False
    
    # Two-column layout for centering form
    col1, col2,col3 = st.columns([1, 2,1])  
    with col2:
        with st.form("login_form", clear_on_submit=False):
            st.markdown("<div class='form-container'>", unsafe_allow_html=True)
            
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
            submit_button = st.form_submit_button(label="Sign In")
            
            if submit_button:
                if not username or not password:
                    st.markdown("<p class='error-message'>Please enter both username and password</p>", unsafe_allow_html=True)
                elif authenticate_user(username, password):
                    st.session_state.login_success = True
                    st.session_state.current_username = username
                    st.session_state.current_page = "home"
                else:
                    st.markdown("<p class='error-message'>Invalid username or password</p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Register Link
        st.markdown("<p class='link-text' onclick='document.getElementById(\"register_link\").click()'>Don't have an account? Register here</p>", unsafe_allow_html=True)
        
        # Hidden button for JavaScript to click
        if st.button("Register", key="register_link", help="Switch to registration page"):
            switch_to_register()
            
# Helper functions for prediction system
def load_data(file_path):
    data = pd.read_csv("C:/Pregnancy_risk_Prediction-master/csv/finalData.csv")
    return data

def load_model(file_path):
    with open("C:/Pregnancy_risk_Prediction-master/pkl file/trained_model.pkl", 'rb') as file:
        model = pickle.load(file)
    return model

def make_prediction(model, input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction

# Home Page (Mom's Care App)
def home_page():
    if not st.session_state.login_success:
        st.session_state.current_page = "login"
        return
    
    username = st.session_state.current_username
    user_data = get_user_data(username)
    # App header with logo and regular Streamlit logout button
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="width: 36px; height: 36px; background-color: #3cb371; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; margin-right: 10px;">MC</div>
            <h1 style="margin: 0; color: #2e8b57;">Mom's Care</h1>
            <span style="color: #2e8b57; font-weight: 600; margin-left: 20px;">Welcome, {user_data['name']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Direct Streamlit button for logout
        st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
        if st.button("Logout", key="logout_btn"):
            logout()
        st.markdown('</div>', unsafe_allow_html=True) 
    
    # Main application tabs
    tab1, tab2, tab3, tab4, tab5,tab6= st.tabs(["✨ Home ✨", "📊 Prediction","🔍Search symptom", "🥗 Healthy Diet","📚 Guidance", "🧘‍♀️ Exercise",])
    
    with tab1:
       import home
       home.show_home_content()
    
    # Prediction page
    with tab2:
        st.title("Pregnancy Risk Prediction")
    
        # Add a decorative header with icon
        st.markdown("""
        <div style="background-color: #e6f3e6; padding: 20px; border-radius: 10px; margin-bottom: 25px; 
                    border-left: 5px solid #2e8b57; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h3 style="margin: 0; color: #2e8b57; display: flex; align-items: center; gap: 10px;">
                <span>📊 Risk Assessment Tool</span>
            </h3>
            <p style="margin-top: 10px; color: #333333; font-size: 15px; line-height: 1.5;">
                Enter your health metrics below to receive a personalized pregnancy risk assessment.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Load model and data
        model_path = "C:/Pregnancy_risk_Prediction-master/pkl file/trained_model.pkl"
        model = load_model(model_path)
        
        data = load_data("C:/Pregnancy_risk_Prediction-master/csv/finalData.csv")
        target_column = "Risk Level"
        x = data.drop(columns=[target_column])

        scaler_path = "C:/Pregnancy_risk_Prediction-master/pkl file/scaler.pkl"  
        with open(scaler_path, 'rb') as file:
            scaler = pickle.load(file)

        encoder_path = "C:/Pregnancy_risk_Prediction-master/pkl file/label_encoder.pkl"
        with open(encoder_path, 'rb') as file:
            encoder = pickle.load(file)
                
        # Get input data
        st.subheader("Enter Input Data for Prediction")
        st.write("Please provide the following details:")
        
        # Create two columns for input fields
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4 style='color: #2e8b57; margin-bottom: 15px;'>Personal Information</h4>", unsafe_allow_html=True)
            age = st.number_input("Age", min_value=15, max_value=60, value=30, step=1, format="%d", 
                                help="Enter your current age in years")
            
            st.markdown("<h4 style='color: #2e8b57; margin-top: 20px; margin-bottom: 15px;'>Blood Sugar</h4>", unsafe_allow_html=True)
            bs = st.number_input("Blood Sugar Level (mg/dL)", min_value=50, max_value=300, value=100, step=1, format="%d",
                              help="Enter your fasting blood sugar level")
        
        with col2:
            st.markdown("<h4 style='color: #2e8b57; margin-bottom: 15px;'>Body Temperature</h4>", unsafe_allow_html=True)
            body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0, step=0.1, format="%.1f",
                                      help="Enter your body temperature in degrees Celsius")

            st.markdown("<h4 style='color: #2e8b57; margin-top: 20px; margin-bottom: 15px;'>Heart Rate</h4>", unsafe_allow_html=True)
            heart_rate = st.number_input("Heart Rate (BPM)", min_value=40, max_value=200, value=80, step=1, format="%d",
                                       help="Enter your resting heart rate in beats per minute")

        # Create separate section for blood pressure
        st.markdown("<h4 style='color: #2e8b57; margin-top: 20px; margin-bottom: 15px;'>Blood Pressure</h4>", unsafe_allow_html=True)
        bp_col1, bp_col2 = st.columns(2)
        
        with bp_col1:
            systolic_bp = st.number_input("Systolic BP (mmHg)", min_value=80, max_value=200, value=120, step=1, format="%d",
                                        help="The top number in a blood pressure reading")
        
        with bp_col2:
            diastolic_bp = st.number_input("Diastolic BP (mmHg)", min_value=40, max_value=120, value=80, step=1, format="%d",
                                         help="The bottom number in a blood pressure reading")

        feature_names = ['Age', 'Systolic BP', 'Diastolic BP', 'BS', 'Body Temp', 'Heart Rate']
        input_data = pd.DataFrame([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]], columns=feature_names)

        # Add some spacing
        st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)

        # Center the predict button with custom styling
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <style>
            div.stButton > button {
                width: 100%;
                height: 50px;
                font-size: 18px;
                font-weight: bold;
                background-color: #3cb371;
                color: white;
                box-shadow: 0 3px 8px rgba(0,0,0,0.15);
                transition: all 0.3s ease;
            }
            div.stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 12px rgba(0,0,0,0.2);
                background-color: #2e8b57;
            }
            </style>
            """, unsafe_allow_html=True)
            predict_button = st.button("Predict Risk Level", key="predict_risk_button") 
       
        # Prediction result display
        if predict_button:
            # Add a spinner while processing
            with st.spinner('Analyzing your data...'):
                import time
                time.sleep(1)  # Simulate processing time
                
                # Make prediction
                std_data = scaler.transform(input_data)
                prediction = model.predict(std_data)
                predicted_label = encoder.inverse_transform(prediction)
                risk_level = predicted_label[0]
                
                # Display result with better styling
                st.markdown(f"""
                <div style="background-color: #e6f3e6; padding: 20px; border-radius: 10px; margin: 25px 0; 
                            border-left: 5px solid #3cb371; box-shadow: 0 3px 10px rgba(0,0,0,0.08);">
                    <h3 style="margin: 0; color: #2e8b57;">Prediction Result</h3>
                    <p style="margin-top: 15px; font-size: 17px;">
                        🔹 The predicted <strong>Risk Level</strong> is: <strong style="color: #2e8b57; font-size: 19px;">{predicted_label[0]}</strong>
                    </p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab3:
        import search
        search.show_search_content()      
     # Healthy Diet page
    with tab4:
        import food
        food.show_food_content()
        
    # Guidance page
    with tab5:
        import Trimester
        Trimester.show_trimester_content()
        
    # Exercise page
    with tab6:
        import excercise
        excercise.show_excercise_content()

def main():
   if st.session_state.current_page == "login":
        login_page()
   elif st.session_state.current_page == "register":
        registration_page()
   elif st.session_state.login_success:
        if st.session_state.current_page == "home":
         home_page()
        
   else:
        # If user is not logged in, redirect to login page
        st.session_state.current_page = "login"
        login_page()

if __name__ == "__main__":
    main()