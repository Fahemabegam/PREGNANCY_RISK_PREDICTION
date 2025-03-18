import streamlit as st
import pandas as pd
import datetime
import numpy as np
from PIL import Image
import base64


# CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 36px;
        font-weight: bold;
        color: #ff6b6b;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 24px;
        font-weight: bold;
        color: #4b778d;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .nutrition-card {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 4px solid #4b778d;
    }
    .recommendation {
        color: #28a745;
        font-weight: bold;
    }
    .warning {
        color: #dc3545;
        font-weight: bold;
    }
    .center-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .stButton > button {
       background-color: #4b778d;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        margin: 5px;
        width: 150px;  /* Fixed width for all buttons */
        height: 40px;  /* Fixed height for all buttons */
        text-align: center;  /* Center text inside buttons */
    }
    .stButton > button:hover {
        background-color: #ff6b6b;
    }
    .active-button {
        background-color: #ff6b6b !important;
    }
    .button-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# Sample data for the application
nutrient_requirements = pd.DataFrame({
    'Nutrient': ['Calories', 'Protein', 'Calcium', 'Iron', 'Folate', 'Vitamin D', 'Omega-3 DHA', 'Fiber', 'Water'],
    'First Trimester': ['~1,800 kcal', '75-100g', '1,000mg', '27mg', '600-800mcg', '600 IU', '200mg', '25-30g', '~10 cups'],
    'Second Trimester': ['~2,200 kcal', '75-100g', '1,000mg', '27mg', '600-800mcg', '600 IU', '200mg', '25-30g', '~10 cups'],
    'Third Trimester': ['~2,400 kcal', '75-100g', '1,000mg', '27mg', '600-800mcg', '600 IU', '200mg', '25-30g', '~10 cups'],
    'Food Sources': [
        'Whole grains, lean proteins, healthy fats, fruits & vegetables',
        'Lean meats, poultry, fish, beans, tofu, eggs, dairy',
        'Dairy products, fortified plant milks, leafy greens, almonds',
        'Lean red meat, spinach, beans, fortified cereals',
        'Leafy greens, citrus fruits, beans, fortified cereals',
        'Fatty fish, egg yolks, fortified foods, sunshine',
        'Fatty fish (salmon, sardines), walnuts, flaxseed, chia seeds',
        'Whole grains, fruits, vegetables, beans, nuts',
        'Water, herbal teas, fruits & vegetables with high water content'
    ]
  })

foods_to_avoid = {
    "High-Mercury Fish": ["Shark", "Swordfish", "King mackerel", "Tilefish", "Bigeye tuna"],
    "Undercooked Foods": ["Raw eggs", "Raw or undercooked meat", "Unpasteurized milk", "Raw sprouts", "Sushi with raw fish"],
    "Highly Processed Foods": ["Sugary drinks", "Fast food", "Foods with artificial additives", "Excessive caffeine", "Alcohol"],
  }

healthy_meal_ideas = {
    "Breakfast": [
        "Oatmeal with berries, nuts, and a dash of cinnamon",
        "Greek yogurt parfait with granola and fresh fruit",
        "Whole grain toast with avocado and a boiled egg",
        "Spinach and feta omelet with whole grain toast",
        "Smoothie with banana, berries, yogurt, and spinach",
    ],
    "Lunch": [
        "Quinoa salad with roasted vegetables and chickpeas",
        "Lentil soup with whole grain bread",
        "Whole grain wrap with hummus, vegetables, and grilled chicken",
        "Mediterranean salad with olives, feta, cucumbers, and tomatoes",
        "Baked sweet potato topped with black beans and greek yogurt",
    ],
    "Dinner": [
        "Baked salmon with asparagus and brown rice",
        "Vegetable stir-fry with tofu and quinoa",
        "Whole grain pasta with tomato sauce and turkey meatballs",
        "Roasted chicken with steamed vegetables and wild rice",
        "Bean and vegetable chili with avocado",
    ],
    "Snacks": [
        "Apple slices with almond butter",
        "Carrot sticks with hummus",
        "Greek yogurt with berries",
        "Trail mix with nuts and dried fruits",
        "Half an avocado with lemon juice",
    ]
  }

# Function to create meal plan
def generate_meal_plan():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meal_plan = {}
    
    for day in days:
        meal_plan[day] = {
            'Breakfast': np.random.choice(healthy_meal_ideas['Breakfast']),
            'Lunch': np.random.choice(healthy_meal_ideas['Lunch']),
            'Dinner': np.random.choice(healthy_meal_ideas['Dinner']),
            'Snack 1': np.random.choice(healthy_meal_ideas['Snacks']),
            'Snack 2': np.random.choice(healthy_meal_ideas['Snacks'])
        }
    
    return meal_plan

# Function to generate a food diary template
def create_food_diary():
    diary = pd.DataFrame(columns=['Date', 'Meal', 'Food Item', 'Portion Size', 'Feelings/Notes'])
    return diary

# Sample nutrition tracking data
def sample_nutrition_data():
    # Generate 30 days of sample data
    dates = [datetime.datetime.now() - datetime.timedelta(days=x) for x in range(30)]
    
    data = pd.DataFrame({
        'Date': dates,
        'Calories': np.random.randint(1800, 2500, 30),
        'Protein': np.random.randint(60, 110, 30),
        'Water': np.random.randint(6, 12, 30),
        'Fruits & Veg': np.random.randint(3, 9, 30)
    })
    
    return data

# Load images from URL function
def get_image_from_url(url, width=None):
    st.image(url, width=width)

# Main application
def show_food_content():
    # Header
    st.markdown('<div class="main-header">Pregnancy Nutrition Tracker</div>', unsafe_allow_html=True)
    
    # Add header image
    header_img_url = "https://img.freepik.com/free-photo/pregnant-woman-eating-healthy-food_23-2148725746.jpg"
    get_image_from_url(header_img_url, width=800)
     
    # Get user info
    if 'trimester' not in st.session_state:
        st.session_state.trimester = 'First Trimester'
    if 'week' not in st.session_state:
        st.session_state.week = 1
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'
    
    # Create navigation buttons
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        if st.button("Home", key="home_btn", help="Go to home page"):
            st.session_state.page = 'Home'
    
    with col2:
        if st.button("Nutrition Guide", key="guide_btn", help="View nutrition guidelines"):
            st.session_state.page = 'Nutrition Guide'
    
    with col3:
        if st.button("Meal Planner", key="meal_btn", help="Plan your meals"):
            st.session_state.page = 'Meal Planner'
    
    with col4:
        if st.button("Food Diary", key="diary_btn", help="Record your meals"):
            st.session_state.page = 'Food Diary'
    
    with col5:
        if st.button("Progress", key="progress_btn", help="Track your progress"):
            st.session_state.page = 'Progress Tracker'
    
    with col6:
        if st.button("Q&A", key="qa_btn", help="Ask nutrition questions"):
            st.session_state.page = 'Ask a Question'
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Highlight the active button with custom JS
    st.markdown(f"""
    <script>
        const buttons = document.querySelectorAll('.stButton button');
        buttons.forEach(button => {{
            if (button.innerText === '{st.session_state.page}' || 
                (button.innerText === 'Home' && '{st.session_state.page}' === 'Home') ||
                (button.innerText === 'Nutrition Guide' && '{st.session_state.page}' === 'Nutrition Guide') ||
                (button.innerText === 'Meal Planner' && '{st.session_state.page}' === 'Meal Planner') ||
                (button.innerText === 'Food Diary' && '{st.session_state.page}' === 'Food Diary') ||
                (button.innerText === 'Progress' && '{st.session_state.page}' === 'Progress Tracker') ||
                (button.innerText === 'Q&A' && '{st.session_state.page}' === 'Ask a Question')) {{
                button.classList.add('active-button');
            }}
        }});
    </script>
    """, unsafe_allow_html=True)
    
    # Display current page content based on selection
    st.title(st.session_state.page)
    st.markdown("---")
    
    # Content for each page
    if st.session_state.page == 'Home':
        show_home_page()
    elif st.session_state.page == 'Nutrition Guide':
        show_nutrition_guide()
    elif st.session_state.page == 'Meal Planner':
        show_meal_planner()
    elif st.session_state.page == 'Food Diary':
        show_food_diary()
    elif st.session_state.page == 'Progress Tracker':
        show_progress_tracker()
    elif st.session_state.page == 'Ask a Question':
        show_qa_section()

# Home page
def show_home_page():
    # Add a welcoming image
    welcome_img_url = "https://img.freepik.com/free-photo/side-view-pregnant-woman-holding-fruits-vegetables_23-2148748257.jpg"
    get_image_from_url(welcome_img_url, width=600)
    
    # Key nutrients needed
    st.markdown('<div class="sub-header">Key Nutrients for This Week</div>', 
                unsafe_allow_html=True)
    
    # Get trimester-specific nutrients
    current_nutrients = nutrient_requirements[['Nutrient', st.session_state.trimester, 'Food Sources']]
    
    for _, row in current_nutrients.iterrows():
        st.markdown(f"""
        <div class="nutrition-card">
            <h3>{row['Nutrient']}</h3>
            <p><b>Recommended:</b> {row[st.session_state.trimester]}</p>
            <p><b>Food Sources:</b> {row['Food Sources']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    
    # Nutritional tip of the day
    st.markdown('<div class="sub-header">Tip of the Day</div>', 
                unsafe_allow_html=True)
    
    tips = [
        "Stay hydrated! Drink at least 8-10 glasses of water daily.",
        "Include a source of protein with every meal.",
        "Keep healthy snacks handy to avoid unhealthy choices when hungry.",
        "Don't skip meals - eat regular, balanced meals throughout the day.",
        "Include a variety of colorful fruits and vegetables in your diet."
    ]
    
    st.markdown(f"""
    <div class="info-box">
        <p>{np.random.choice(tips)}</p>
    </div>
    """, unsafe_allow_html=True)

# Nutrition Guide page
def show_nutrition_guide():
    st.markdown('<div class="sub-header">Pregnancy Nutrition Guidelines</div>', 
                unsafe_allow_html=True)
    
    # Add nutrition plate image
    nutrition_plate_url = "https://img.freepik.com/free-photo/top-view-vegetables-fruits-table_23-2148365900.jpg"
    get_image_from_url(nutrition_plate_url, width=500)
    
    # Display nutrient requirements
    st.markdown('<div class="sub-header">Essential Nutrients During Pregnancy</div>', 
                unsafe_allow_html=True)
    st.dataframe(nutrient_requirements.set_index('Nutrient'))
    
    # Foods to Avoid
    st.markdown('<div class="sub-header">Foods to Avoid During Pregnancy</div>', 
                unsafe_allow_html=True)
    
    # Add foods to avoid image
    avoid_foods_url = "https://img.freepik.com/free-photo/different-kinds-junk-food-dark-concrete-background_1150-42661.jpg"
    get_image_from_url(avoid_foods_url, width=400)
    
    for category, items in foods_to_avoid.items():
        st.markdown(f"**{category}**: {', '.join(items)}")
    
    # Add more nutritional information
    st.markdown('<div class="sub-header">Important Nutrition Facts</div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="nutrition-card">
            <h3>Morning Sickness Tips</h3>
            <ul>
                <li>Eat small, frequent meals</li>
                <li>Avoid spicy or greasy foods</li>
                <li>Try ginger tea or lemon water</li>
                <li>Keep crackers by your bedside</li>
                <li>Eat protein-rich snacks</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        morning_sickness_url = "https://img.freepik.com/free-photo/nauseous-pregnant-woman-lying-sofa_23-2148748183.jpg"
        get_image_from_url(morning_sickness_url, width=300)
        
    with col2:
        st.markdown("""
        <div class="nutrition-card">
            <h3>Managing Gestational Diabetes</h3>
            <ul>
                <li>Monitor carbohydrate intake</li>
                <li>Choose complex carbs over simple sugars</li>
                <li>Pair carbs with protein or healthy fats</li>
                <li>Stay physically active (with doctor's approval)</li>
                <li>Eat regularly - don't skip meals</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        diabetes_management_url = "https://img.freepik.com/free-photo/measuring-blood-sugar-level-with-glucometer_144627-43168.jpg"
        get_image_from_url(diabetes_management_url, width=300)

# Meal Planner page
def show_meal_planner():
    st.markdown('<div class="sub-header">Weekly Meal Planner</div>', 
                unsafe_allow_html=True)
    
    # Add meal planning image
    meal_planning_url = "https://img.freepik.com/free-photo/top-view-vegetables-fruits-paper-bag-scales-cutting-board-dark-surface_176474-2151.jpg"
    get_image_from_url(meal_planning_url, width=500)
    
    st.markdown("""
    <div class="info-box">
        Create a balanced meal plan tailored to your pregnancy nutritional needs. 
        Hit the button below to generate a week's worth of meal ideas.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Generate Meal Plan", key="gen_meal_plan"):
        meal_plan = generate_meal_plan()
        
        for day, meals in meal_plan.items():
            st.markdown(f"### {day}")
            for meal_type, meal in meals.items():
                st.markdown(f"**{meal_type}**: {meal}")
            st.markdown("---")
    
    st.markdown('<div class="sub-header">Healthy Meal Ideas</div>', 
                unsafe_allow_html=True)
    
    # Meal selection with buttons instead of tabs
    meal_selection = st.radio("Select meal type:", 
                             ["Breakfast", "Lunch", "Dinner", "Snacks"],
                             horizontal=True)
    
    # Add meal type images
    meal_images = {
        "Breakfast": "https://img.freepik.com/free-photo/top-view-breakfast-assortment-with-copy-space_23-2148866033.jpg",
        "Lunch": "https://img.freepik.com/free-photo/top-view-delicious-healthy-salad-plate_23-2148712835.jpg",
        "Dinner": "https://img.freepik.com/free-photo/baked-salmon-garnished-with-asparagus-tomatoes-with-herbs_2829-19758.jpg",
        "Snacks": "https://img.freepik.com/free-photo/healthy-snacks-bowl_144627-24917.jpg"
    }
    
    get_image_from_url(meal_images[meal_selection], width=400)
    for meal in healthy_meal_ideas[meal_selection]:
        st.markdown(f"- {meal}")

# Food Diary page
def show_food_diary():
    st.markdown('<div class="sub-header">Food Diary</div>', 
                unsafe_allow_html=True)
    
    # Add food diary image
    food_diary_url = "https://img.freepik.com/free-photo/woman-planning-diet_23-2148773882.jpg"
    get_image_from_url(food_diary_url, width=500)
    
    st.markdown("""
    <div class="info-box">
        Track your daily food intake to ensure you're getting all the nutrients you need.
        This can also help identify triggers for any pregnancy-related discomfort.
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize the diary entries in session state if it doesn't exist
    if 'diary_entries' not in st.session_state:
        st.session_state.diary_entries = pd.DataFrame(columns=['Date', 'Meal', 'Food Item', 'Portion', 'Notes'])
    
    
    # Date selector
    selected_date = st.date_input("Select Date", datetime.date.today())
    
    # Meal type selector
    meal_type = st.selectbox("Meal Type", ["Breakfast", "Morning Snack", "Lunch", 
                                          "Afternoon Snack", "Dinner", "Evening Snack"])
    
    # Food entry
    col1, col2 = st.columns(2)
    
    with col1:
        food_item = st.text_input("Food Item")
        portion = st.text_input("Portion Size")
    
    with col2:
        notes = st.text_area("Feelings / Notes")
    
    if st.button("Add to Diary", key="add_diary"):
         # Create a new entry
        new_entry = pd.DataFrame({
            'Date': [selected_date],
            'Meal': [meal_type],
            'Food Item': [food_item],
            'Portion': [portion],
            'Notes': [notes]
        })
        
        # Add to existing entries
        st.session_state.diary_entries = pd.concat([new_entry, st.session_state.diary_entries], ignore_index=True)
        st.success(f"Added {food_item} to your diary for {selected_date}")
        
         # Rerun the app to show the updated diary
        st.rerun()
    
    # Show sample diary entries
    st.markdown('<div class="sub-header">Recent Entries</div>', 
                unsafe_allow_html=True)
    # Display the diary entries
    if not st.session_state.diary_entries.empty:
        st.dataframe(st.session_state.diary_entries)
    else:
        st.info("No entries yet. Add your first meal above!")
    
    

# Progress Tracker page
def show_progress_tracker():
    st.markdown('<div class="sub-header">Nutrition Progress Tracker</div>', 
                unsafe_allow_html=True)
    
    # Add progress tracker image
    progress_tracker_url = "https://img.freepik.com/free-photo/woman-measuring-herself-to-document-progress_23-2148748164.jpg"
    get_image_from_url(progress_tracker_url, width=500)
    
    # Get sample data
    data = sample_nutrition_data()
    
    # Display line chart
    st.markdown("### Daily Nutrient Intake")
    
    metric = st.selectbox("Select Nutrient to Track", 
                        ["Calories", "Protein", "Water", "Fruits & Veg"])
    
    # Create chart
    st.line_chart(data.set_index('Date')[metric])
    
    # Weekly summary
    st.markdown("### Weekly Summary")
    
    # Last 7 days of data
    weekly_data = data.iloc[:7]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Avg. Calories", f"{weekly_data['Calories'].mean():.0f} kcal", 
                f"{weekly_data['Calories'].mean() - 2000:.0f}")
    
    with col2:
        st.metric("Avg. Protein", f"{weekly_data['Protein'].mean():.0f}g", 
                f"{weekly_data['Protein'].mean() - 75:.0f}")
    
    with col3:
        st.metric("Avg. Water", f"{weekly_data['Water'].mean():.1f} cups", 
                f"{weekly_data['Water'].mean() - 8:.1f}")
    
    with col4:
        st.metric("Avg. Fruits & Veg", f"{weekly_data['Fruits & Veg'].mean():.1f} servings", 
                f"{weekly_data['Fruits & Veg'].mean() - 5:.1f}")

# Q&A section
def show_qa_section():
    st.markdown('<div class="sub-header">Nutrition Questions & Answers</div>', 
                unsafe_allow_html=True)
    
    # Add Q&A image
    qa_image_url = "https://img.freepik.com/free-photo/pregnant-woman-consultation-with-doctor_23-2148748181.jpg"
    get_image_from_url(qa_image_url, width=500)
    
    st.markdown("""
    <div class="info-box">
        Have questions about your pregnancy nutrition? Type your question below!
        <br><br>
        <b>Note:</b> This tool provides general guidance based on common pregnancy nutrition
        principles. Always consult with your healthcare provider for personalized advice.
    </div>
    """, unsafe_allow_html=True)
    
    user_question = st.text_input("Your Question", "")
    
    if user_question:
        st.markdown("### Answer")
        
        # Sample Q&A database with images
        qa_database = {
            "can I drink coffee": {
                "answer": """
                    <p>It's generally advised to limit caffeine intake during pregnancy to 200mg per day
                    (about one 12oz cup of coffee). Too much caffeine has been linked to increased risk
                    of miscarriage and low birth weight.</p>
                    <p class="recommendation">Recommendation: Limit to one small cup of coffee per day, 
                    or switch to decaf options.</p>
                """,
                "image": "https://img.freepik.com/free-photo/cup-coffee-with-heart-drawn-foam_1286-70.jpg"
            },
            "morning sickness": {
                "answer": """
                    <p>Morning sickness affects many pregnant women, especially in the first trimester.
                    Some nutritional strategies that may help include:</p>
                    <ul>
                        <li>Eating small, frequent meals throughout the day</li>
                        <li>Keeping crackers by your bed to eat before getting up</li>
                        <li>Staying hydrated with small, frequent sips of water</li>
                        <li>Trying ginger tea or ginger candies</li>
                        <li>Avoiding strong smells and greasy foods</li>
                    </ul>
                """,
                "image": "https://img.freepik.com/free-photo/ginger-tea-with-lemon-honey-white-cup_114579-66461.jpg"
            },
            "fish": {
                "answer": """
                    <p>Fish is an excellent source of protein and omega-3 fatty acids, which are important
                    for your baby's brain development. However, some fish contain high levels of mercury,
                    which can be harmful.</p>
                    <p class="recommendation">Safe fish options include salmon, trout, light canned tuna, 
                    and shrimp. Avoid high-mercury fish like shark, swordfish, king mackerel, and tilefish.</p>
                    <p>Aim for 2-3 servings (8-12 oz total) of low-mercury fish per week.</p>
                """,
                "image": "https://img.freepik.com/free-photo/grilled-salmon-steak-with-vegetables_2829-10278.jpg"
            }
        }
        
        # Simple keyword matching
        answer_found = False
        for keyword, qa_item in qa_database.items():
            if keyword in user_question.lower():
                st.markdown(qa_item["answer"], unsafe_allow_html=True)
                get_image_from_url(qa_item["image"], width=400)
                answer_found = True
                break
        
        if not answer_found:
            st.markdown("""
                <p>I don't have specific information about that question in my database. 
                Here are some general guidelines:</p>
                <ul>
                    <li>Focus on nutrient-dense whole foods</li>
                    <li>Stay hydrated with water</li>
                    <li>Consult with your healthcare provider for personalized advice</li>
                    <li>Consider speaking with a registered dietitian specializing in prenatal nutrition</li>
                </ul>
            """, unsafe_allow_html=True)
            general_nutrition_url = "https://img.freepik.com/free-photo/healthy-eating-healthy-food-wooden-table_1150-38012.jpg"
            get_image_from_url(general_nutrition_url, width=400)

