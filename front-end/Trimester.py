import streamlit as st

# Add page title with custom styling
#st.markdown("<h1 style='color: #5D9E7F;'>Trimester Selection</h1>", unsafe_allow_html=True)

# Define pastel green colors
primary_green = "#8FBC8F"  # Dark Sea Green (pastel)
secondary_green = "#C1E1C1"  # Light pastel green
hover_green = "#A9D0A9"  # Medium pastel green
bg_color = "#F0FFF0"  # Honeydew (very light pastel green)

# Custom CSS for styling
st.markdown(f"""
<style>
    .stApp {{
        background-color: #e6f3e6; /* Pastel green background */
        }}
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color:#F0FFF0;
        height:400px;
        width:300px;
        border:1px solid black;
    }}
    
    
    /* Styling for trimester buttons */
    div.stButton > button {{
        background-color: {primary_green};
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 4px;
        transition: background-color 0.3s;
    }}
    div.stButton > button:hover {{
        background-color: {hover_green};
    }}
    div.stButton > button:active {{
        background-color: {hover_green};
    }}
    
    /* Styling for content cards */
    .css-1r6slb0, .css-1kyxreq {{  /* Target Streamlit card elements */
        background-color: {secondary_green};
        border: 1px solid {primary_green};
        border-radius: 10px;
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%;
    }}
    
    .css-1r6slb0:hover, .css-1kyxreq:hover {{
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        background-color: {hover_green};
    }}
    
    /* Style for read more button */
    .read-more-btn {{
        background-color: white;
        color: {primary_green};
        border: 1px solid {primary_green};
        padding: 5px 15px;
        border-radius: 4px;
        font-size: 14px;
        cursor: pointer;
        transition: all 0.3s;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
    }}
    .read-more-btn:hover {{
        background-color: {primary_green};
        color: white;
    }}
    
    /* Additional element styling */
    h1, h2, h3, h4 {{
        color: #3A5F3A;
    }}
    
    img {{
        border-radius: 6px;
    }}
</style>
""", unsafe_allow_html=True)
def show_trimester_content():
# Define the content for each trimester's boxes
 trimester_content = {
    1: [
        {
            "title": "Morning Sickness and Nausea",
            "text": "Common in early pregnancy, often triggered by hormonal changes. Eating small, frequent meals and staying hydrated can help manage symptoms. Consult your doctor if nausea becomes severe or persistent.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Fatigue",
            "text": "Increased progesterone levels can cause extreme tiredness. Prioritize rest, maintain a balanced diet, and consider light exercise to boost energy. Listen to your body and avoid overexertion.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Breast Tenderness",
            "text": "Hormonal shifts may make breasts sore or sensitive. Wearing a supportive bra and applying warm or cold compresses can provide relief. This symptom often subsides after the first trimester.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Frequent Urination",
            "text": "Pressure on the bladder from a growing uterus leads to more bathroom trips. Stay hydrated but reduce fluid intake before bedtime to minimize nighttime disruptions.",
            "image":"https://via.placeholder.com/200*150"
        },
        {
            "title": "Mood Swings",
            "text": "Hormonal fluctuations can cause emotional ups and downs. Practice relaxation techniques, communicate with loved ones, and seek support if mood swings feel overwhelming.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Food Cravings/Aversions",
            "text": "Hormonal changes may alter taste preferences. Embrace healthy cravings in moderation and find alternatives for aversions to maintain proper nutrition.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Spotting/Bleeding",
            "text": "Light spotting can be normal, but heavy bleeding requires immediate medical attention. Always report any bleeding to your healthcare provider to rule out complications.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Cramping",
            "text": "Mild cramping is common as the uterus expands. However, severe or persistent cramps should be evaluated by a doctor to ensure everything is progressing normally.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Constipation",
            "text": "Hormonal changes slow digestion, leading to constipation. Increase fiber intake, drink plenty of water, and stay active to promote regular bowel movements.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Anxiety/Fear",
            "text": "Pregnancy can bring uncertainty and worry. Join support groups, practice mindfulness, and discuss concerns with your healthcare provider to ease anxiety and feel more confident.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Ectopic Pregnancy",
            "text": "Occurs when a fertilized egg implants outside the uterus, usually in a fallopian tube. Symptoms include sharp abdominal pain, vaginal bleeding, and dizziness. It’s a medical emergency requiring immediate treatment to prevent complications like rupture.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Molar Pregnancy",
            "text": "A rare condition where abnormal tissue grows inside the uterus instead of a healthy embryo. Symptoms include severe nausea, vaginal bleeding, and unusually high hCG levels. Treatment involves removing the tissue, and follow-up care is essential to monitor for complications.",
            "image": "https://via.placeholder.com/200*150"
        }
    ],
    2: [
        {
            "title": "Back Pain",
            "text": "Caused by weight gain and shifting posture. Practice good posture, use supportive pillows, and try prenatal yoga or gentle stretches for relief.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Baby Bump Growth",
            "text": "Understanding your changing body and what's normal for the second trimester.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Feeling First Movements",
            "text": "When and how you might experience your baby's first kicks and movements.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Maternity Wardrobe Essentials",
            "text": "Key clothing items to keep you comfortable as your body changes.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Sleep Solutions",
            "text": "Tips for getting restful sleep as your pregnancy progresses.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Pregnancy Superfoods",
            "text": "Nutrient-rich foods that support your baby's development in the second trimester.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Fetal Development: Weeks 13-17",
            "text": "Your baby's growth and development during the early second trimester.",
            "image":"https://via.placeholder.com/200*150"
        },
        {
            "title": "Fetal Development: Weeks 18-22",
            "text": "Major milestones in your baby's development during the middle of pregnancy.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Fetal Development: Weeks 23-27",
            "text": "How your baby is growing and preparing for the third trimester.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Creating a Baby Registry",
            "text": "Tips for selecting must-have items and creating your perfect baby registry.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Prenatal Yoga Benefits",
            "text": "How yoga can help with common pregnancy discomforts and prepare for birth.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Second Trimester Checklist",
            "text": "Important tasks to complete during this middle phase of pregnancy.",
            "image": "https://via.placeholder.com/200*150"
        }
    ],
    3: [
        {
            "title": "Preparing for Labor",
            "text": "Signs of labor, when to go to the hospital, and what to expect during delivery.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Birth Plan Basics",
            "text": "How to create a flexible birth plan that reflects your preferences and priorities.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Hospital Bag Essentials",
            "text": "Complete packing list for mom, partner, and baby during your hospital stay.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Managing Late Pregnancy Discomfort",
            "text": "Relief strategies for common third trimester symptoms like back pain and swelling.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Preparing Siblings",
            "text": "How to help older children adjust to the idea of a new baby in the family.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Nursery Setup Guide",
            "text": "Essential items and safety considerations for creating your baby's space.",
            "image":"https://via.placeholder.com/200*150"
        },
        {
            "title": "Fetal Development: Weeks 28-31",
            "text": "Your baby's remarkable growth and development in the early third trimester.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Fetal Development: Weeks 32-36",
            "text": "How your baby is preparing for birth during these crucial weeks.",
            "image":"https://via.placeholder.com/200*150"
        },
        {
            "title": "Fetal Development: Weeks 37-40",
            "text": "Final development stages as your baby reaches full term and prepares for arrival.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Breastfeeding Basics",
            "text": "Preparation and essential information for successful breastfeeding.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Newborn Care 101",
            "text": "Essential skills and knowledge for caring for your newborn in the first days.",
            "image": "https://via.placeholder.com/200*150"
        },
        {
            "title": "Third Trimester Checklist",
            "text": "Final preparations and arrangements before your baby arrives.",
            "image":"https://via.placeholder.com/200*150"
        }
    ]
}

# Create three buttons in a horizontal layout
 col1, col2, col3 = st.columns(3)

 with col1:
    trimester1_button = st.button("Trimester 1", use_container_width=True)

 with col2:
    trimester2_button = st.button("Trimester 2", use_container_width=True)

 with col3:
    trimester3_button = st.button("Trimester 3", use_container_width=True)

# Store which trimester is active in session state
 if 'active_trimester' not in st.session_state:
    st.session_state.active_trimester = None

# Handle button clicks
 if trimester1_button:
    st.session_state.active_trimester = 1
 elif trimester2_button:
    st.session_state.active_trimester = 2
 elif trimester3_button:
    st.session_state.active_trimester = 3

# Function to display a read more button
 def read_more_button(title):
    st.markdown(f'<a href="#" class="read-more-btn">Read More</a>', unsafe_allow_html=True)
    

# Create a container for the boxes
 box_container = st.container()

# Display the appropriate set of boxes based on which trimester is active
 with box_container:
    if st.session_state.active_trimester:
        st.markdown(f"<h2 style='color: #5D9E7F; margin-top: 20px;'>Trimester {st.session_state.active_trimester} Resources</h2>", unsafe_allow_html=True)
        
        # Get content for the active trimester
        active_content = trimester_content[st.session_state.active_trimester]
        
        # Create 4 rows with 3 boxes each
        for row in range(4):
            # Create columns for each row
            cols = st.columns(3)
            
            for col_idx in range(3):
                box_num = row * 3 + col_idx
                
                # Make sure we don't exceed the content list
                if box_num < len(active_content):
                    content = active_content[box_num]
                    
                    # Use Streamlit's native components
                    with cols[col_idx]:
                        # Use st.container to create a styled box
                        with st.container():
                            # Display the image
                             if content["image"]:
                                try:
                                    st.image(content["image"], use_container_width=True)
                                except:
                                    st.warning("Image not available")
                            
                            # Display title and text
                             st.markdown(f"#### {content['title']}")
                             st.markdown(content["text"])
                            
                            # Add read more button
                             st.markdown(f'<a href="#" class="read-more-btn">Read More</a>', unsafe_allow_html=True)
                             