import streamlit as st
import base64
import os
import pickle
import hashlib
import time
import re
from datetime import datetime
from pathlib import Path

def show_login_content():

# Initialize session state variables if they don't exist
 if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
 if 'username' not in st.session_state:
    st.session_state.username = None
 if 'registration_mode' not in st.session_state:
    st.session_state.registration_mode = False

# File paths
USER_DB_PATH = "user_data.pkl"
SESSION_DB_PATH = "session_data.pkl"
VIDEO_PATH = "background_video.mp4"  # Replace with your video path

# Helper functions
def get_base64_video(video_path):
    """Convert local video to base64 string for embedding"""
    with open("C:/Pregnancy_risk_Prediction-master/images/video1.mp4", "rb") as video_file:
        return base64.b64encode(video_file.read()).decode()

def set_video_background(video_path):
    """Set a local video as the background of a Streamlit app"""
    try:
        # Get the video as base64 string
        video_base64 = get_base64_video("C:/Pregnancy_risk_Prediction-master/images/video1.mp4")
        
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
            background-color: rgba(255, 255, 255, 0.9);
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
    if st.session_state.authenticated:
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
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title("Welcome to Our Application")
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
            
        
        # Interests (optional)
       
        
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
    st.write("© 2025 Your Application Name | Privacy Policy | Terms of Service")
    st.markdown('</div>', unsafe_allow_html=True)

def show_welcome_page():
    """Display the welcome page after successful login"""
    user_db = load_user_db()
    user_data = user_db.get(st.session_state.username, {})
    
    # Get user's first name for personalized greeting
    first_name = user_data.get("first_name", st.session_state.username) if isinstance(user_data, dict) else st.session_state.username
    
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title(f"Welcome, {first_name}!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("You have successfully logged in to the application.")
    
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
    
    st.write("---")
    if st.button("Sign Out"):
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
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.write("© 2025 Your Application Name | Privacy Policy | Terms of Service")
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application function"""
    try:
        # Set the video background
        set_video_background(VIDEO_PATH)
        
        # Check if user is already logged in
        is_logged_in = check_auto_login()
        
        # Show appropriate page based on authentication status
        if is_logged_in:
            show_welcome_page()
        else:
            show_login_page()
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
