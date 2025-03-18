import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import numpy as np
from PIL import Image
import io

# --- Helper Functions ---
def calculate_trimester(weeks):
    if weeks <= 12:
        return "First Trimester"
    elif weeks <= 28:
        return "Second Trimester"
    else:
        return "Third Trimester"

# Function to generate a simple placeholder image
def create_placeholder_image(width, height, color=(135, 206, 235)):
    """Create a simple colored placeholder image"""
    img = Image.new('RGB', (width, height), color=color)
    return img

def get_safe_exercises(trimester):
    exercises = {
        "First Trimester": [
            {"name": "Walking", "description": "Low-impact cardiovascular exercise", "duration": "20-30 minutes", "frequency": "Most days", "video_link": "https://example.com/walking"},
            {"name": "Swimming", "description": "Full body workout with no impact", "duration": "20-30 minutes", "frequency": "2-3 times per week", "video_link": "https://example.com/swimming"},
            {"name": "Prenatal Yoga", "description": "Gentle stretching and breathing", "duration": "15-30 minutes", "frequency": "2-3 times per week", "video_link": "https://example.com/yoga1"},
            {"name": "Light Strength Training", "description": "Using light weights or resistance bands", "duration": "15-20 minutes", "frequency": "2-3 times per week", "video_link": "https://example.com/strength1"}
        ],
        "Second Trimester": [
            {"name": "Walking", "description": "Low-impact cardiovascular exercise", "duration": "20-30 minutes", "frequency": "Most days", "video_link": "https://example.com/walking"},
            {"name": "Swimming", "description": "Full body workout with no impact", "duration": "20-30 minutes", "frequency": "2-3 times per week", "video_link": "https://example.com/swimming"},
            {"name": "Modified Prenatal Yoga", "description": "Focuses on balance and stretching", "duration": "15-30 minutes", "frequency": "2-3 times per week", "video_link": "https://example.com/yoga2"},
            {"name": "Stationary Cycling", "description": "Low-impact cardio that's safe as your center of gravity shifts", "duration": "15-20 minutes", "frequency": "2-3 times per week", "video_link": "https://example.com/cycling"}
        ],
        "Third Trimester": [
            {"name": "Walking", "description": "Gentle pace, shorter distances", "duration": "15-20 minutes", "frequency": "Most days, as comfortable", "video_link": "https://example.com/walking_gentle"},
            {"name": "Swimming", "description": "Excellent for reducing swelling and supporting weight", "duration": "15-20 minutes", "frequency": "2-3 times per week", "video_link": "https://example.com/swimming_third"},
            {"name": "Pelvic Floor Exercises", "description": "Kegels and gentle pelvic tilts", "duration": "5-10 minutes", "frequency": "Daily", "video_link": "https://example.com/pelvic_floor"},
            {"name": "Seated Exercise", "description": "Chair yoga and upper body stretches", "duration": "10-15 minutes", "frequency": "Daily", "video_link": "https://example.com/seated"}
        ]
    }
    return exercises.get(trimester, [])

# --- App Layout ---
def show_Exercise_content():
    # Initialize session state to store exercise logs if it doesn't exist
    if 'exercise_logs' not in st.session_state:
        # Create some default exercise history
        st.session_state.exercise_logs = pd.DataFrame({
            "Date": [datetime.now().date() - timedelta(days=x) for x in range(7, 0, -1)],
            "Exercise": ["Walking", "Prenatal Yoga", "Swimming", "Rest Day", "Walking", "Light Strength", "Swimming"],
            "Duration (min)": [30, 20, 25, 0, 35, 15, 30],
            "Intensity": ["Light", "Light", "Moderate", "None", "Moderate", "Light", "Moderate"],
            "Notes": ["Felt good", "Relaxing", "Tired after", "", "Energetic", "Challenging", "Enjoyable"]
        })

    # Add a header - using generated placeholder instead of URL
    header_img = create_placeholder_image(1200, 300, color=(159, 226, 191))
    st.image(header_img, caption="Pregnancy Fitness Journey", use_container_width=True)
    
    st.title("Pregnancy Exercise Companion")
    
    # User information section - moved from sidebar to main content
    st.header("Your Pregnancy Journey")
    
    # Create three columns for user info layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        # Add profile picture placeholder using generated image
        profile_img = create_placeholder_image(200, 200, color=(230, 190, 220))
        # Using placeholder since the image path might not be accessible
        try:
            st.image("C:/Pregnancy_risk_Prediction-master/images/pregnant.jpg", caption="Picture")
        except:
            st.image(profile_img, caption="Profile Picture")
    
    with col2:
        # User inputs
        user_name = st.text_input("Your Name", "")
        
        # Get due date or gestational age
        input_method = st.radio("Enter your pregnancy information:", 
                              ["Due Date", "Current Week of Pregnancy"])
        
        if input_method == "Due Date":
            due_date = st.date_input("Your Due Date", datetime.now() + timedelta(days=280))
            today = datetime.now().date()
            days_difference = (due_date - today).days
            if days_difference > 280:
                st.warning("Due date seems too far in the future.")
                weeks_pregnant = 0
            else:
                weeks_pregnant = max(0, int((280 - days_difference) / 7))
        else:
            weeks_pregnant = st.slider("Current Week of Pregnancy", 1, 42, 20)
    
    with col3:
        # Health metrics tracking
        st.subheader("Track Your Health")
        weight = st.number_input("Current Weight (kg)", min_value=0.0, format="%.1f")
        
        if st.button("Log Today's Data"):
            # In a real app, save this to a database
            st.success("Data logged successfully!")
            st.balloons()
    
    # Calculate trimester
    current_trimester = calculate_trimester(weeks_pregnant)
    
    # Information about current progress - moved from sidebar
    progress_col1, progress_col2 = st.columns(2)
    
    with progress_col1:
        # Display pregnancy info with a visual indicator
        st.write(f"You are in week {weeks_pregnant}")
        st.write(f"Trimester: {current_trimester}")
    
    with progress_col2:
        # Visual pregnancy progress bar
        st.write("Pregnancy Progress")
        st.progress(min(weeks_pregnant / 40, 1.0))
    
    st.markdown("---")
    
    # Welcome message
    if user_name:
        st.write(f"Welcome, {user_name}! We're here to support your fitness journey during pregnancy.")
    else:
        st.write("Welcome! We're here to support your fitness journey during pregnancy.")
    
    # Display current trimester image - using generated placeholder
    trimester_img = create_placeholder_image(800, 400, color=((100, 180, 220) if current_trimester == "First Trimester" else 
                                                             (100, 220, 180) if current_trimester == "Second Trimester" else
                                                             (220, 180, 100)))
    st.image(trimester_img, caption=f"{current_trimester} - Week {weeks_pregnant}", use_container_width=True)
    
    # Information tabs
    tab1, tab2, tab3 = st.tabs(["Recommended Exercises", "Exercise Tracker", "Health Information"])
    
    with tab1:
        st.header(f"Safe Exercises for the {current_trimester}")
        
        # Display exercises for current trimester
        exercises = get_safe_exercises(current_trimester)
        
        # Create columns for exercise cards
        cols = st.columns(2)
        
        for i, exercise in enumerate(exercises):
            # Create image with color based on exercise name (just for visual variety)
            color = (
                (100, 150, 220) if "Walking" in exercise["name"] else
                (100, 200, 220) if "Swimming" in exercise["name"] else
                (150, 220, 150) if "Yoga" in exercise["name"] else
                (200, 180, 150) if "Strength" in exercise["name"] else
                (180, 180, 220) if "Cycling" in exercise["name"] else
                (220, 150, 150) if "Floor" in exercise["name"] else
                (150, 220, 200)
            )
            exercise_img = create_placeholder_image(400, 300, color=color)
            
            with cols[i % 2]:
                # Display exercise image
                st.image(exercise_img, caption=exercise["name"])
                st.subheader(exercise["name"])
                st.write(f"**Description:** {exercise['description']}")
                st.write(f"**Recommended duration:** {exercise['duration']}")
                st.write(f"**Frequency:** {exercise['frequency']}")
                st.write(f"[Watch instructional video]({exercise['video_link']})")
                st.write("---")
        
        # General exercise guidelines with icon
        st.subheader("General Exercise Guidelines During Pregnancy")
        
        # Create two columns for guidelines - text and image
        guide_col1, guide_col2 = st.columns([2, 1])
        
        with guide_col1:
            st.write("""
            - Always consult with your healthcare provider before starting any exercise program
            - Stay hydrated before, during, and after exercise
            - Avoid exercising in hot, humid conditions
            - Avoid exercises that involve lying flat on your back after the first trimester
            - Stop if you feel dizzy, short of breath, or uncomfortable
            - Wear supportive clothing and proper footwear
            """)
        
        with guide_col2:
            guidelines_img = create_placeholder_image(300, 300, color=(220, 200, 150))
            st.image(guidelines_img, caption="Exercise Guidelines")
        
    with tab2:
        st.header("Track Your Exercise")
        
        # Form for logging exercise
        with st.form("exercise_log"):
            st.write("Log your daily exercise")
            
            form_col1, form_col2 = st.columns(2)
            
            with form_col1:
                exercise_date = st.date_input("Date", datetime.now())
                exercise_type = st.selectbox("Exercise Type", 
                                           [ex["name"] for ex in get_safe_exercises(current_trimester)])
                duration = st.number_input("Duration (minutes)", min_value=5, max_value=120, step=5)
            
            with form_col2:
                tracking_img = create_placeholder_image(300, 200, color=(200, 220, 170))
                st.image(tracking_img, caption="Activity Tracking")
                intensity = st.select_slider("Intensity", options=["Very Light", "Light", "Moderate", "Somewhat Hard"])
                notes = st.text_area("Notes (How did you feel?)")
            
            submitted = st.form_submit_button("Log Exercise")
            if submitted:
                # Add the new exercise log to the dataframe
                new_log = pd.DataFrame({
                    "Date": [exercise_date],
                    "Exercise": [exercise_type],
                    "Duration (min)": [duration],
                    "Intensity": [intensity],
                    "Notes": [notes]
                })
                
                # Add new log to the top of the existing logs
                st.session_state.exercise_logs = pd.concat([new_log, st.session_state.exercise_logs]).reset_index(drop=True)
                
                st.success("Exercise logged successfully!")
                st.rerun()  # Rerun the app to show the updated logs
        
        # Show exercise history
        st.subheader("Your Exercise History")
        
        # Display data and visualization side by side if we have logs
        if not st.session_state.exercise_logs.empty:
            hist_col1, hist_col2 = st.columns([2, 3])
            
            with hist_col1:
                st.dataframe(st.session_state.exercise_logs)
            
            with hist_col2:
                # Create visualization
                fig = px.bar(st.session_state.exercise_logs, x="Date", y="Duration (min)", color="Exercise", 
                             title="Your Weekly Exercise Summary")
                st.plotly_chart(fig)
        else:
            st.info("Your exercise history will appear here once you start logging activities.")
            tracking_dashboard = create_placeholder_image(800, 300, color=(150, 190, 230))
            st.image(tracking_dashboard, caption="Sample Exercise Tracking Dashboard")
    
    with tab3:
        st.header("Health Information by Trimester")
        
        # Create tabs for each trimester
        trim1, trim2, trim3 = st.tabs(["First Trimester", "Second Trimester", "Third Trimester"])
        
        with trim1:
            # Two column layout - text and image
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.subheader("Weeks 1-12")
                st.write("""
                During the first trimester, you may experience morning sickness and fatigue. 
                Listen to your body and don't push yourself too hard.
                
                **Exercise Benefits:**
                - Helps reduce morning sickness
                - Improves sleep quality
                - Reduces stress and anxiety
                
                **Precautions:**
                - Stay well hydrated
                - Avoid overheating
                - Modify exercises if experiencing nausea
                """)
            
            with col2:
                trim1_img = create_placeholder_image(400, 300, color=(100, 180, 220))
                st.image(trim1_img, caption="First Trimester")
        
        with trim2:
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.subheader("Weeks 13-28")
                st.write("""
                Many women find the second trimester more comfortable for exercise 
                as energy levels increase and morning sickness subsides.
                
                **Exercise Benefits:**
                - Helps prepare your body for childbirth
                - May reduce back pain
                - Can help prevent gestational diabetes
                
                **Precautions:**
                - Avoid exercises lying flat on your back
                - Modify balance exercises as your center of gravity shifts
                - Be mindful of joint laxity
                """)
            
            with col2:
                trim2_img = create_placeholder_image(400, 300, color=(100, 220, 180))
                st.image(trim2_img, caption="Second Trimester")
        
        with trim3:
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.subheader("Weeks 29-40+")
                st.write("""
                In the third trimester, you'll need to modify exercises more significantly 
                as your body changes.
                
                **Exercise Benefits:**
                - Can help position baby for delivery
                - May make labor and delivery easier
                - Helps maintain fitness for postpartum recovery
                
                **Precautions:**
                - Avoid high-impact activities
                - Be cautious with balance
                - Use support props when needed
                - Stop immediately if you feel contractions
                """)
            
            with col2:
                trim3_img = create_placeholder_image(400, 300, color=(220, 180, 100))
                st.image(trim3_img, caption="Third Trimester")
        
        # Warning signs section with attention-grabbing image
        st.subheader("⚠️ Warning Signs: When to Stop Exercising")
        
        warning_col1, warning_col2 = st.columns([3, 1])
        
        with warning_col1:
            st.write("""
            Stop exercising and contact your healthcare provider if you experience:
            - Vaginal bleeding
            - Dizziness or feeling faint
            - Increased shortness of breath
            - Chest pain
            - Headache
            - Muscle weakness
            - Calf pain or swelling
            - Regular, painful contractions
            - Fluid leaking from the vagina
            """)
        
        with warning_col2:
            warning_img = create_placeholder_image(200, 200, color=(240, 100, 100))
            st.image(warning_img, caption="Warning Signs")
    
