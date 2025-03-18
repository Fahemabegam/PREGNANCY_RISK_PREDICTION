import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import os
import hashlib
import time
import re
import json
from datetime import datetime
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier

# Set the page configuration
st.set_page_config(
    page_title="Pregnancy Risk Prediction App",
    page_icon="C:/Pregnancy_risk_Prediction-master/images/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# File paths
USER_DB_PATH = "user_data.pkl"
SESSION_DB_PATH = "session_data.pkl"
VIDEO_PATH = "C:/Pregnancy_risk_Prediction-master/images/video1.mp4"  # Replace with your video path

# Helper functions for authentication
def get_base64_video(video_path):
    """Convert local video to base64 string for embedding"""
    try:
        with open(video_path, "rb") as video_file:
            return base64.b64encode(video_file.read()).decode()
    except Exception as e:
        st.error(f"Error reading video file: {e}")
        return None

def set_video_background(video_path):
    """Set a local video as the background of a Streamlit app"""
    try:
        # Get the video as base64 string
        video_base64 = get_base64_video(video_path)
        if video_base64:
            # Create HTML/CSS to display video as background
            video_html = f"""
            <style>
            .stApp {{
                background: transparent;
            }}
            .video-background {{
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%;
                min-height: 100%;
                width: auto;
                height: auto;
                z-index: -1;
                opacity: 0.7;
            }}
            .card {{
                
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }}
            .header {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                color: rgba(255, 255, 255, 0.7);
            }}
            </style>
            <video autoplay muted loop class="video-background">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
            """
            
            # Inject the HTML/CSS into the Streamlit app
            st.markdown(video_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Video file not found at {video_path}. Using default background.")
    except Exception as e:
        st.error(f"Error setting video background: {e}")

def hash_password(password):
    """Create a hashed version of the password"""
    salt = "a1b2c3d4e5f6g7h8i9j0"  # Add a salt for additional security
    return hashlib.sha256((password + salt).encode()).hexdigest()

def load_user_db():
    """Load the user database from file or create new one"""
    if os.path.exists(USER_DB_PATH):
        try:
            with open(USER_DB_PATH, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            st.error(f"Error loading user database: {e}")
            return {}
    else:
        return {}

def save_user_db(user_db):
    """Save the user database to a file"""
    with open(USER_DB_PATH, "wb") as f:
        pickle.dump(user_db, f)

def load_session_db():
    """Load the session database from file or create new one"""
    if os.path.exists(SESSION_DB_PATH):
        try:
            with open(SESSION_DB_PATH, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            st.error(f"Error loading session database: {e}")
            return {}
    else:
        return {}

def save_session_db(session_db):
    """Save the session database to a file"""
    with open(SESSION_DB_PATH, "wb") as f:
        pickle.dump(session_db, f)

def create_session(username):
    """Create a new session for the user"""
    session_id = hashlib.sha256(f"{username}:{time.time()}".encode()).hexdigest()
    session_db = load_session_db()
    session_db[session_id] = {
        "username": username,
        "created_at": time.time(),
        "expires_at": time.time() + (30 * 24 * 60 * 60),  # 30 days expiry
        "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_session_db(session_db)
    return session_id

def validate_session(session_id):
    """Validate if a session is valid and not expired"""
    session_db = load_session_db()
    if session_id in session_db:
        session = session_db[session_id]
        if session["expires_at"] > time.time():
            # Update last login time
            session_db[session_id]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_session_db(session_db)
            return session["username"]
    return None

def check_auto_login():
    """Check if user has a valid session cookie for auto-login"""
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        return True
        
    if 'session_id' in st.session_state:
        username = validate_session(st.session_state.session_id)
        if username:
            st.session_state.authenticated = True
            st.session_state.username = username
            return True
    return False

def is_valid_email(email):
    """Validate email format"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def is_strong_password(password):
    """Check if password is strong enough"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    
    return True, "Password is strong"

def show_login_page():
    """Display the login page"""
    # Initialize session state variables if they don't exist
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'registration_mode' not in st.session_state:
        st.session_state.registration_mode = False
        
    # Custom CSS for pastel green theme
    st.markdown(
        """
        <style>
        
        .stTextInput>div>div>input {
            background-color: whitesmoke;
            color: black !important; /* Black text for input fields */
        }
        .stButton>button {
            background-color: #3cb371; /* Pastel green button */
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2e8b57; /* Darker green on hover */
        }
        .stMarkdown {
            color: #2e8b57; /* Dark green text for headings */
        }
        .stRadio>div>label {
            color: #2e8b57 !important; /* Dark green for radio button text */
        }
        .stSuccess {
            color: #2e8b57; /* Dark green for success messages */
        }
        .stError {
            color: #ff4b4b; /* Red for error messages */
        }
        /* Style for username and password headers */
        .stTextInput>label {
            color: #2e8b57 !important; /* Dark green for input labels */
            font-weight: bold;
        }
        /* Style for Login Page header */
        h1 {
            color: #2e8b57 !important; /* Dark green for Login Page header */
        }
        /* Style for "Select an option" header */
        .stMarkdown h3 {
            color: #2e8b57 !important; /* Dark green for "Select an option" header */
        }
        /* Style for radio button options */
        .stRadio>div>label>div {
            color: #2e8b57 !important; /* Dark green for radio button options */
        }
        /* Style for sidebar */
        .css-1d391kg {
            background-color: #e6f3e6 !important; /* Pastel green background for sidebar */
        }
        /* Style for sidebar navigation menu */
        .css-1d391kg .stSelectbox>div>div {
            color: #2e8b57 !important; /* Dark green for sidebar navigation menu */
        }
        /* Style for all headers (h1, h2, h3, h4, etc.) */
        h1, h2, h3, h4, h5, h6 {
            color: #2e8b57 !important; /* Dark green for all headers */
        }
        .stDataInput>div>div>input {
            background-color: #e6f3e6;
            color: black !important;
            }
        /* Style for input field headers */
        .stNumberInput>label, .stTextInput>label {
            color: #2e8b57 !important; /* Dark green for input field headers */
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
            
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title("Pregnancy Risk Prediction App")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if st.session_state.registration_mode:
        st.subheader("Create Your Account")
        
        # Basic information
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name*")
            email = st.text_input("Email Address*")
            new_password = st.text_input("Password*", type="password")
        with col2:
            last_name = st.text_input("Last Name*")
            username = st.text_input("Username*")
            confirm_password = st.text_input("Confirm Password*", type="password")
        
        # Additional details
        st.subheader("Additional Details")
        col1, col2 = st.columns(2)
        with col1:
            dob = st.date_input("Date of Birth")
            phone = st.text_input("Phone Number")
        with col2:
            country = st.selectbox("Country", ["Select Country", "United States", "Canada", "United Kingdom", "Australia", "India", "Germany", "France", "Other"])
            
        # Terms and privacy
        st.write("---")
        terms_agree = st.checkbox("I agree to the Terms and Conditions*")
        privacy_agree = st.checkbox("I agree to the Privacy Policy*")
        marketing_agree = st.checkbox("I would like to receive news and special offers (Optional)")
        
        # Registration button
        if st.button("Create Account"):
            # Validate required fields
            if not first_name or not last_name or not email or not username or not new_password or not confirm_password:
                st.error("Please fill in all required fields marked with *")
            elif not is_valid_email(email):
                st.error("Please enter a valid email address")
            elif not terms_agree or not privacy_agree:
                st.error("You must agree to the Terms and Conditions and Privacy Policy")
            elif new_password != confirm_password:
                st.error("Passwords do not match")
            else:
                # Validate password strength
                is_strong, msg = is_strong_password(new_password)
                if not is_strong:
                    st.error(msg)
                else:
                    # Check if username already exists
                    user_db = load_user_db()
                    if username in user_db:
                        st.error("Username already exists. Please choose another one.")
                    else:
                        # Create new user profile
                        user_profile = {
                            "username": username,
                            "password_hash": hash_password(new_password),
                            "first_name": first_name,
                            "last_name": last_name,
                            "email": email,
                            "date_of_birth": str(dob),
                            "phone": phone,
                            "country": country if country != "Select Country" else "",
                            "marketing_consent": marketing_agree,
                            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        
                        user_db[username] = user_profile
                        save_user_db(user_db)
                        
                        st.success("Registration successful! You can now log in with your credentials.")
                        st.session_state.registration_mode = False
                        st.rerun()
        
        # Back to login option
        st.write("---")
        st.write("Already have an account?")
        if st.button("Back to Login"):
            st.session_state.registration_mode = False
            st.rerun()
        
    else:
        st.subheader("Sign In")
        username = st.text_input("Username or Email")
        password = st.text_input("Password", type="password")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            remember_me = st.checkbox("Remember me", value=True)
        with col2:
            st.write("")  # Spacer
            st.write("")  # Spacer
            forgot_password = st.button("Forgot Password?")
        
        if forgot_password:
            st.info("Please contact support to reset your password.")
            
        # Login button with full width
        if st.button("Sign In", use_container_width=True):
            if not username or not password:
                st.error("Please enter both username and password")
            else:
                user_db = load_user_db()
                
                # Check if the username exists
                if username in user_db:
                    stored_user = user_db[username]
                    
                    # If stored_user is a dictionary (new format)
                    if isinstance(stored_user, dict) and stored_user.get("password_hash") == hash_password(password):
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        
                        # Update last login time
                        user_db[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        save_user_db(user_db)
                        
                        if remember_me:
                            session_id = create_session(username)
                            st.session_state.session_id = session_id
                        
                        st.success("Login successful!")
                        st.rerun()
                    # If stored_user is a string (old format with just password)
                    elif isinstance(stored_user, str) and stored_user == hash_password(password):
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        
                        if remember_me:
                            session_id = create_session(username)
                            st.session_state.session_id = session_id
                        
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
                else:
                    # Check if it might be an email login
                    email_found = False
                    for user, data in user_db.items():
                        if isinstance(data, dict) and data.get("email") == username:
                            if data.get("password_hash") == hash_password(password):
                                st.session_state.authenticated = True
                                st.session_state.username = user
                                
                                # Update last login time
                                user_db[user]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                save_user_db(user_db)
                                
                                if remember_me:
                                    session_id = create_session(user)
                                    st.session_state.session_id = session_id
                                
                                email_found = True
                                st.success("Login successful!")
                                st.rerun()
                            else:
                                st.error("Invalid username or password")
                                email_found = True
                                break
                    
                    if not email_found:
                        st.error("Invalid username or password")
                
        st.write("---")
        st.write("Don't have an account?")
        if st.button("Create Account", use_container_width=True):
            st.session_state.registration_mode = True
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.write("© 2025 Pregnancy Risk Prediction App | Privacy Policy | Terms of Service")
    st.markdown('</div>', unsafe_allow_html=True)

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

# Module imports for tabs
def import_trimester_module():
    import sys
    import importlib.util
    
    try:
        # If Trimester.py exists in the same directory
        spec = importlib.util.spec_from_file_location("Trimester", "Trimester.py")
        trimester_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(trimester_module)
        return trimester_module
    except Exception as e:
        st.error(f"Failed to import Trimester module: {e}")
        
        # Create a dummy module with a placeholder function
        class DummyModule:
            @staticmethod
            def show_trimester_content():
                st.subheader("Trimester Information")
                st.write("Trimester module could not be loaded. Please ensure the module is available.")
        
        return DummyModule()

def import_food_module():
    import sys
    import importlib.util
    
    try:
        # If food.py exists in the same directory
        spec = importlib.util.spec_from_file_location("food", "food.py")
        food_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(food_module)
        return food_module
    except Exception as e:
        st.error(f"Failed to import food module: {e}")
        
        # Create a dummy module with a placeholder function
        class DummyModule:
            @staticmethod
            def show_food_content():
                st.subheader("Healthy Diet Information")
                st.write("Food module could not be loaded. Please ensure the module is available.")
        
        return DummyModule()

def import_exercise_module():
    import sys
    import importlib.util
    
    try:
        # If Exercise.py exists in the same directory
        spec = importlib.util.spec_from_file_location("Exercise", "Exercise.py")
        exercise_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(exercise_module)
        return exercise_module
    except Exception as e:
        st.error(f"Failed to import Exercise module: {e}")
        
        # Create a dummy module with a placeholder function
        class DummyModule:
            @staticmethod
            def show_Exercise_content():
                st.subheader("Exercise Information")
                st.write("Exercise module could not be loaded. Please ensure the module is available.")
        
        return DummyModule()

def show_prediction_app():
    # Try to load module imports
    trimester_module = import_trimester_module()
    food_module = import_food_module()
    exercise_module = import_exercise_module()
    
    user_db = load_user_db()
    user_data = user_db.get(st.session_state.username, {})
    
    # Get user's first name for personalized greeting
    first_name = user_data.get("first_name", st.session_state.username) if isinstance(user_data, dict) else st.session_state.username
    
    st.sidebar.title(f"Welcome, {first_name}!")
    
    if st.sidebar.button("Sign Out"):
        st.session_state.authenticated = False
        st.session_state.username = None
        if 'session_id' in st.session_state:
            # Remove session from session database
            session_db = load_session_db()
            if st.session_state.session_id in session_db:
                del session_db[st.session_state.session_id]
                save_session_db(session_db)
            del st.session_state.session_id
        st.rerun()
    
    # Main application
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Guidance", "Prediction", "Healthy Diet", "Exercise"])
    
    with tab1:
        st.title("Welcome to Pregnancy Guidance and Risk Prediction")
        
        # User profile information if available
        if isinstance(user_data, dict):
            st.subheader("Your Profile")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Name:** {user_data.get('first_name', '')} {user_data.get('last_name', '')}")
                st.write(f"**Email:** {user_data.get('email', '')}")
                if user_data.get("phone"):
                    st.write(f"**Phone:** {user_data.get('phone', '')}")
            
            with col2:
                if user_data.get("country"):
                    st.write(f"**Country:** {user_data.get('country', '')}")
                st.write(f"**Last Login:** {user_data.get('last_login', 'First login')}")
                
        st.subheader("About This Application")
        st.write("""
        This application is designed to assist expectant mothers in monitoring and assessing their pregnancy health. 
        Use the tabs above to access different features:
        
        - **Guidance**: Information about different trimesters of pregnancy
        - **Prediction**: Assess your pregnancy risk levels based on health metrics
        - **Healthy Diet**: Recommendations for a healthy diet during pregnancy
        - **Exercise**: Safe exercises for expectant mothers
        """)
    
    # Guidance page
    with tab2:
        st.title("Guidance")
        import Trimester
        Trimester.show_trimester_content()
    
    # Prediction page
    with tab3:
        st.title("Prediction")

        # Load model and data
        try:
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

            age = st.number_input("Age", min_value=0, step=1, format="%d")
            systolic_bp = st.number_input("Systolic Blood Pressure", min_value=0, step=1, format="%d")
            diastolic_bp = st.number_input("Diastolic Blood Pressure", min_value=0, step=1, format="%d")
            bs = st.number_input("Blood Sugar Level", min_value=0, step=1, format="%d")
            body_temp = st.number_input("Body Temperature (°C)", min_value=0, step=1, format="%d")
            heart_rate = st.number_input("Heart Rate", min_value=0, step=1, format="%d")

            feature_names = ['Age', 'Systolic BP', 'Diastolic BP', 'BS', 'Body Temp', 'Heart Rate']
            input_data = pd.DataFrame([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]], columns=feature_names)

            # Prediction button
            if st.button("Predict"):
                std_data = scaler.transform(input_data)
                prediction = model.predict(std_data)
                predicted_label = encoder.inverse_transform(prediction)
                st.success(f"🔹 The predicted **Risk Level** is: **{predicted_label[0]}**")
        except Exception as e:
            st.error(f"Error in prediction module: {e}")
            st.info("Please ensure all prediction model files are available at the correct paths.")
    
    # Healthy Diet page
    with tab4:
        st.title("Healthy Diet")
        import food
        food.show_food_content()
    
    # Exercise page
    with tab5:
        st.title("Exercise")
        import Exercise
        Exercise.show_Exercise_content()

def main():
    """Main application function"""
    try:
        # Initialize session state variables if they don't exist
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        if 'username' not in st.session_state:
            st.session_state.username = None
        if 'registration_mode' not in st.session_state:
            st.session_state.registration_mode = False
            
        # Check if user is already authenticated
        is_authenticated = check_auto_login()
        
        # Show appropriate page based on authentication status
        if is_authenticated:
            show_prediction_app()
        else:
            # Try to set video background for login page
            try:
                set_video_background(VIDEO_PATH)
            except:
                pass  # Continue without video background if it fails
            show_login_page()
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()