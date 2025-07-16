import streamlit as st
import pandas as pd
import numpy as np
import json
import re
from datetime import datetime
import random

# Define simplified color scheme
primary_green = "#8FBC8F"  # Dark Sea Green (pastel)
secondary_green = "#C1E1C1"  # Light pastel green
bg_color = "#F0FFF0"  # Honeydew (very light pastel green)

def show_food_content():
      
# Load food database with nutritional info
 @st.cache_data
 def load_food_database():
    # This is a simplified food database - in a real app, you would use a more comprehensive database
    food_db = {
        "apple": {
            "calories": 95,
            "protein": 0.5,
            "carbs": 25,
            "fat": 0.3,
            "fiber": 4,
            "vitamins": {"A": 2, "C": 14, "B6": 5},
            "minerals": {"potassium": 195, "magnesium": 9},
            "folic_acid": 3
        },
        "banana": {
            "calories": 105,
            "protein": 1.3,
            "carbs": 27,
            "fat": 0.4,
            "fiber": 3.1,
            "vitamins": {"A": 1, "C": 10, "B6": 20},
            "minerals": {"potassium": 422, "magnesium": 32},
            "folic_acid": 24
        },
        "chicken breast": {
            "calories": 165,
            "protein": 31,
            "carbs": 0,
            "fat": 3.6,
            "fiber": 0,
            "vitamins": {"A": 0, "B6": 30, "B12": 10},
            "minerals": {"potassium": 220, "magnesium": 29},
            "folic_acid": 4
        },
        "salmon": {
            "calories": 206,
            "protein": 22,
            "carbs": 0,
            "fat": 13,
            "fiber": 0,
            "vitamins": {"A": 2, "D": 100, "B12": 80},
            "minerals": {"potassium": 380, "magnesium": 31},
            "folic_acid": 12
        },
        "brown rice": {
            "calories": 216,
            "protein": 5,
            "carbs": 45,
            "fat": 1.8,
            "fiber": 3.5,
            "vitamins": {"A": 0, "E": 5, "B6": 15},
            "minerals": {"potassium": 84, "magnesium": 86},
            "folic_acid": 8
        },
        "spinach": {
            "calories": 23,
            "protein": 2.9,
            "carbs": 3.6,
            "fat": 0.4,
            "fiber": 2.2,
            "vitamins": {"A": 56, "C": 14, "K": 181},
            "minerals": {"potassium": 558, "magnesium": 79, "iron": 15},
            "folic_acid": 194
        },
        "egg": {
            "calories": 78,
            "protein": 6.3,
            "carbs": 0.6,
            "fat": 5.3,
            "fiber": 0,
            "vitamins": {"A": 5, "D": 10, "B12": 11},
            "minerals": {"potassium": 69, "zinc": 5},
            "folic_acid": 24
        },
        "oatmeal": {
            "calories": 158,
            "protein": 6,
            "carbs": 27,
            "fat": 3.2,
            "fiber": 4,
            "vitamins": {"B1": 15, "B5": 10},
            "minerals": {"magnesium": 63, "iron": 10},
            "folic_acid": 14
        },
        "avocado": {
            "calories": 240,
            "protein": 3,
            "carbs": 12,
            "fat": 22,
            "fiber": 10,
            "vitamins": {"C": 17, "E": 14, "K": 26},
            "minerals": {"potassium": 728, "magnesium": 58},
            "folic_acid": 82
        },
        "sweet potato": {
            "calories": 114,
            "protein": 2,
            "carbs": 27,
            "fat": 0.1,
            "fiber": 4,
            "vitamins": {"A": 368, "C": 30, "B6": 15},
            "minerals": {"potassium": 448, "magnesium": 31},
            "folic_acid": 11
        },
        "greek yogurt": {
            "calories": 100,
            "protein": 10,
            "carbs": 3.6,
            "fat": 5,
            "fiber": 0,
            "vitamins": {"B12": 12, "B2": 14},
            "minerals": {"calcium": 11, "phosphorus": 15},
            "folic_acid": 7
        },
        "broccoli": {
            "calories": 55,
            "protein": 3.7,
            "carbs": 11.2,
            "fat": 0.6,
            "fiber": 5.1,
            "vitamins": {"A": 11, "C": 135, "K": 116},
            "minerals": {"potassium": 288, "calcium": 4},
            "folic_acid": 108
        },
        "milk": {
            "calories": 103,
            "protein": 8,
            "carbs": 12,
            "fat": 2.4,
            "fiber": 0,
            "vitamins": {"A": 5, "D": 24, "B12": 18},
            "minerals": {"calcium": 28, "phosphorus": 22},
            "folic_acid": 12
        },
        "almonds": {
            "calories": 164,
            "protein": 6,
            "carbs": 6,
            "fat": 14,
            "fiber": 3.5,
            "vitamins": {"E": 37, "B2": 17},
            "minerals": {"magnesium": 76, "phosphorus": 15},
            "folic_acid": 10
        },
        "beans": {
            "calories": 127,
            "protein": 8.7,
            "carbs": 22.8,
            "fat": 0.5,
            "fiber": 7.4,
            "vitamins": {"B1": 13, "B9": 30},
            "minerals": {"iron": 13, "magnesium": 16},
            "folic_acid": 46
        },
        "quinoa": {
            "calories": 120,
            "protein": 4.4,
            "carbs": 21.3,
            "fat": 1.9,
            "fiber": 2.8,
            "vitamins": {"B1": 13, "B6": 11},
            "minerals": {"magnesium": 30, "phosphorus": 28},
            "folic_acid": 42
        },
        "blueberries": {
            "calories": 84,
            "protein": 1.1,
            "carbs": 21.4,
            "fat": 0.5,
            "fiber": 3.6,
            "vitamins": {"C": 16, "K": 24},
            "minerals": {"manganese": 17, "potassium": 77},
            "folic_acid": 6
        },
        "lentils": {
            "calories": 115,
            "protein": 9,
            "carbs": 20,
            "fat": 0.4,
            "fiber": 8,
            "vitamins": {"B1": 15, "B6": 18},
            "minerals": {"iron": 19, "potassium": 140},
            "folic_acid": 179
        },
        "bread": {
            "calories": 79,
            "protein": 3.6,
            "carbs": 13.8,
            "fat": 1,
            "fiber": 1.2,
            "vitamins": {"B1": 8, "B3": 7},
            "minerals": {"sodium": 152, "iron": 5},
            "folic_acid": 20
        },
        "pasta": {
            "calories": 131,
            "protein": 5,
            "carbs": 25.1,
            "fat": 1.1,
            "fiber": 1.2,
            "vitamins": {"B1": 10, "B9": 7},
            "minerals": {"sodium": 1, "iron": 4},
            "folic_acid": 15
        }
    }
    return food_db

# Load meal suggestions database
 @st.cache_data
 def load_meal_suggestions():
    breakfast_meals = [
        {"name": "Oatmeal with Berries", "items": ["oatmeal", "blueberries", "almonds", "milk"], "description": "Hearty oatmeal topped with fresh blueberries, crunchy almonds, and a splash of milk."},
        {"name": "Avocado Toast", "items": ["bread", "avocado", "egg"], "description": "Whole grain toast topped with mashed avocado and a perfectly poached egg."},
        {"name": "Greek Yogurt Parfait", "items": ["greek yogurt", "blueberries", "almonds"], "description": "Creamy Greek yogurt layered with fresh blueberries and crunchy almonds."},
        {"name": "Spinach Omelet", "items": ["egg", "spinach", "milk"], "description": "Fluffy omelet filled with nutrient-rich spinach."},
        {"name": "Quinoa Breakfast Bowl", "items": ["quinoa", "almonds", "blueberries"], "description": "Protein-packed quinoa topped with almonds and sweet blueberries."}
    ]
    
    lunch_meals = [
        {"name": "Chicken Salad", "items": ["chicken breast", "spinach", "avocado"], "description": "Grilled chicken over fresh spinach with creamy avocado."},
        {"name": "Lentil Soup", "items": ["lentils", "broccoli", "bread"], "description": "Hearty lentil soup with broccoli, served with a slice of whole grain bread."},
        {"name": "Quinoa Bowl", "items": ["quinoa", "sweet potato", "beans"], "description": "Nutritious quinoa bowl with roasted sweet potato and protein-rich beans."},
        {"name": "Salmon Plate", "items": ["salmon", "brown rice", "broccoli"], "description": "Omega-rich salmon served with brown rice and steamed broccoli."},
        {"name": "Bean Burrito", "items": ["beans", "avocado", "bread"], "description": "Protein-packed beans with avocado wrapped in a whole grain tortilla."}
    ]
    
    dinner_meals = [
        {"name": "Baked Salmon", "items": ["salmon", "sweet potato", "broccoli"], "description": "Oven-baked salmon with roasted sweet potato and steamed broccoli."},
        {"name": "Chicken Stir-fry", "items": ["chicken breast", "brown rice", "broccoli"], "description": "Lean chicken breast stir-fried with broccoli, served over brown rice."},
        {"name": "Vegetable Quinoa", "items": ["quinoa", "spinach", "sweet potato"], "description": "Fluffy quinoa tossed with sautéed spinach and roasted sweet potato cubes."},
        {"name": "Lentil Curry", "items": ["lentils", "brown rice", "spinach"], "description": "Spiced lentil curry with wilted spinach, served with brown rice."},
        {"name": "Bean Chili", "items": ["beans", "sweet potato", "avocado"], "description": "Hearty bean chili topped with diced sweet potato and avocado."}
    ]
    
    snack_options = [
        {"name": "Apple with Almond Butter", "items": ["apple", "almonds"], "description": "Crisp apple slices with creamy almond butter."},
        {"name": "Greek Yogurt with Berries", "items": ["greek yogurt", "blueberries"], "description": "Protein-rich Greek yogurt topped with sweet blueberries."},
        {"name": "Hard-boiled Egg", "items": ["egg"], "description": "Simple and protein-packed hard-boiled egg."},
        {"name": "Trail Mix", "items": ["almonds", "blueberries"], "description": "Energy-boosting mix of almonds and dried blueberries."},
        {"name": "Avocado Toast Bites", "items": ["avocado", "bread"], "description": "Mini toasts topped with creamy mashed avocado."}
    ]
    
    return {
        "breakfast": breakfast_meals,
        "lunch": lunch_meals,
        "dinner": dinner_meals,
        "snack": snack_options
    }

# Function to calculate BMR (Basal Metabolic Rate) using Mifflin-St Jeor Equation
 def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

# Function to calculate daily calorie needs based on activity level
 def calculate_calorie_needs(bmr, activity_level):
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Super active": 1.9
    }
    return bmr * activity_multipliers[activity_level]

# Function to calculate macronutrient needs based on goals
 def calculate_macros(calories, goal):
    if goal == "Weight loss":
        protein_percent = 0.4
        carbs_percent = 0.3
        fat_percent = 0.3
    elif goal == "Muscle gain":
        protein_percent = 0.3
        carbs_percent = 0.45
        fat_percent = 0.25
    else:  # Maintenance
        protein_percent = 0.3
        carbs_percent = 0.4
        fat_percent = 0.3
    
    protein_calories = calories * protein_percent
    carbs_calories = calories * carbs_percent
    fat_calories = calories * fat_percent
    
    protein_grams = protein_calories / 4
    carbs_grams = carbs_calories / 4
    fat_grams = fat_calories / 9
    
    return {
        "protein": round(protein_grams),
        "carbs": round(carbs_grams),
        "fat": round(fat_grams)
    }

# Function to analyze food input text
 def analyze_food_input(text, food_db):
    text = text.lower()
    results = []
    
    # Try to identify food items and their quantities
    for food in food_db.keys():
        if food in text:
            # Look for quantity before the food item
            quantity_pattern = r'(\d+(?:\.\d+)?)\s*(?:serving|servings|cup|cups|g|gram|grams|oz|ounce|ounces|tbsp|tablespoon|tablespoons|tsp|teaspoon|teaspoons|slice|slices|piece|pieces)?\s+(?:of\s+)?' + re.escape(food)
            match = re.search(quantity_pattern, text)
            quantity = 1  # Default quantity
            if match:
                try:
                    quantity = float(match.group(1))
                except:
                    pass
            
            results.append({"food": food, "quantity": quantity})
    
    return results

# Function to calculate nutrition from food list
 def calculate_nutrition(food_list, food_db):
    total_nutrition = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "fiber": 0,
        "vitamins": {},
        "minerals": {},
        "folic_acid": 0
    }
    
    for item in food_list:
        food = item["food"]
        quantity = item["quantity"]
        
        if food in food_db:
            food_data = food_db[food]
            total_nutrition["calories"] += food_data["calories"] * quantity
            total_nutrition["protein"] += food_data["protein"] * quantity
            total_nutrition["carbs"] += food_data["carbs"] * quantity
            total_nutrition["fat"] += food_data["fat"] * quantity
            total_nutrition["fiber"] += food_data["fiber"] * quantity
            total_nutrition["folic_acid"] += food_data["folic_acid"] * quantity
            
            # Accumulate vitamins
            for vitamin, amount in food_data["vitamins"].items():
                if vitamin in total_nutrition["vitamins"]:
                    total_nutrition["vitamins"][vitamin] += amount * quantity
                else:
                    total_nutrition["vitamins"][vitamin] = amount * quantity
            
            # Accumulate minerals
            for mineral, amount in food_data["minerals"].items():
                if mineral in total_nutrition["minerals"]:
                    total_nutrition["minerals"][mineral] += amount * quantity
                else:
                    total_nutrition["minerals"][mineral] = amount * quantity
    
    # Round values for better display
    total_nutrition["calories"] = round(total_nutrition["calories"])
    total_nutrition["protein"] = round(total_nutrition["protein"], 1)
    total_nutrition["carbs"] = round(total_nutrition["carbs"], 1)
    total_nutrition["fat"] = round(total_nutrition["fat"], 1)
    total_nutrition["fiber"] = round(total_nutrition["fiber"], 1)
    total_nutrition["folic_acid"] = round(total_nutrition["folic_acid"], 1)
    
    for vitamin in total_nutrition["vitamins"]:
        total_nutrition["vitamins"][vitamin] = round(total_nutrition["vitamins"][vitamin], 1)
    
    for mineral in total_nutrition["minerals"]:
        total_nutrition["minerals"][mineral] = round(total_nutrition["minerals"][mineral], 1)
    
    return total_nutrition

# Function to generate meal suggestions based on user preferences and goals
 def generate_meal_suggestions(user_data, food_db, meal_suggestions_db):
    goal = user_data.get("goal", "Maintenance")
    calorie_target = user_data.get("calorie_needs", 2000)
    
    # Get foods to avoid
    foods_to_avoid = []
    if "food_preferences" in user_data:
        if "vegetarian" in user_data["food_preferences"] and user_data["food_preferences"]["vegetarian"]:
            foods_to_avoid.extend(["chicken breast", "salmon"])
        if "vegan" in user_data["food_preferences"] and user_data["food_preferences"]["vegan"]:
            foods_to_avoid.extend(["chicken breast", "salmon", "egg", "milk", "greek yogurt"])
        
        # Add allergies to foods to avoid
        if "allergies" in user_data["food_preferences"]:
            foods_to_avoid.extend(user_data["food_preferences"]["allergies"])
    
    breakfast_options = []
    lunch_options = []
    dinner_options = []
    snack_options = []
    
    # Filter breakfast options
    for meal in meal_suggestions_db["breakfast"]:
        if not any(item in foods_to_avoid for item in meal["items"]):
            breakfast_options.append(meal)
    
    # Filter lunch options
    for meal in meal_suggestions_db["lunch"]:
        if not any(item in foods_to_avoid for item in meal["items"]):
            lunch_options.append(meal)
    
    # Filter dinner options
    for meal in meal_suggestions_db["dinner"]:
        if not any(item in foods_to_avoid for item in meal["items"]):
            dinner_options.append(meal)
    
    # Filter snack options
    for meal in meal_suggestions_db["snack"]:
        if not any(item in foods_to_avoid for item in meal["items"]):
            snack_options.append(meal)
    
    # Select random meals for suggestions
    suggested_meals = {}
    if breakfast_options:
        suggested_meals["breakfast"] = random.choice(breakfast_options)
    if lunch_options:
        suggested_meals["lunch"] = random.choice(lunch_options)
    if dinner_options:
        suggested_meals["dinner"] = random.choice(dinner_options)
    if snack_options:
        suggested_meals["snack"] = random.choice(snack_options)
    
    return suggested_meals

# Function to rate nutritional quality of a day's food
 def rate_nutrition_quality(nutrition_data, user_data):
    score = 0
    max_score = 0
    feedback = []
    
    # Check if we're meeting calorie targets
    daily_calories = nutrition_data["calories"]
    target_calories = user_data.get("calorie_needs", 2000)
    calorie_diff_percent = abs(daily_calories - target_calories) / target_calories * 100
    
    max_score += 10
    if calorie_diff_percent <= 10:
        score += 10
        feedback.append("✅ Your calorie intake is within 10% of your target - great job!")
    elif calorie_diff_percent <= 20:
        score += 7
        if daily_calories < target_calories:
            feedback.append("⚠️ Your calorie intake is a bit low. Consider adding a nutritious snack.")
        else:
            feedback.append("⚠️ Your calorie intake is a bit high. Consider reducing portion sizes slightly.")
    else:
        if daily_calories < target_calories:
            feedback.append("❌ Your calorie intake is significantly below your target, which may lead to nutrient deficiencies.")
        else:
            feedback.append("❌ Your calorie intake exceeds your target by more than 20%, which may not align with your goals.")
    
    # Check protein intake
    max_score += 10
    target_protein = user_data.get("macros", {}).get("protein", 0)
    if target_protein > 0:
        protein_percent = nutrition_data["protein"] / target_protein * 100
        if protein_percent >= 90:
            score += 10
            feedback.append("✅ Great job meeting your protein target!")
        elif protein_percent >= 70:
            score += 7
            feedback.append("⚠️ You're close to your protein target, but could benefit from a bit more.")
        else:
            feedback.append("❌ Your protein intake is significantly below target. Consider adding more protein-rich foods.")
    
    # Check fiber intake
    max_score += 5
    recommended_fiber = 25  # General recommendation in grams
    if nutrition_data["fiber"] >= recommended_fiber:
        score += 5
        feedback.append("✅ Excellent fiber intake!")
    elif nutrition_data["fiber"] >= recommended_fiber * 0.7:
        score += 3
        feedback.append("⚠️ You're getting some fiber, but could benefit from eating more whole grains, fruits, and vegetables.")
    else:
        feedback.append("❌ Your fiber intake is low. Try adding more fruits, vegetables, legumes, and whole grains.")
    
    # Check folic acid
    max_score += 5
    recommended_folic_acid = 400  # mcg
    if nutrition_data["folic_acid"] >= recommended_folic_acid:
        score += 5
        feedback.append("✅ Good job getting enough folic acid!")
    elif nutrition_data["folic_acid"] >= recommended_folic_acid * 0.7:
        score += 3
        feedback.append("⚠️ You're getting some folic acid, but could benefit from more leafy greens and legumes.")
    else:
        feedback.append("❌ Your folic acid intake is low. Consider adding more leafy greens, lentils, and beans to your diet.")
    
    # Check for vitamin diversity
    max_score += 10
    vitamin_count = len(nutrition_data["vitamins"])
    if vitamin_count >= 6:
        score += 10
        feedback.append("✅ Excellent vitamin diversity in your diet!")
    elif vitamin_count >= 4:
        score += 7
        feedback.append("⚠️ You have a good variety of vitamins, but could benefit from more diverse food choices.")
    else:
        feedback.append("❌ Your diet lacks vitamin diversity. Try to eat a wider variety of fruits and vegetables.")
    
    # Calculate overall score as a percentage
    overall_score = int(score / max_score * 100) if max_score > 0 else 0
    
    return {
        "score": overall_score,
        "feedback": feedback
    }

# Initialize session state variables
 if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        "name": "",
        "age": 30,
        "weight": 70,  # kg
        "height": 170,  # cm
        "gender": "Male",
        "activity_level": "Moderately active",
        "goal": "Maintenance",
        "bmr": 0,
        "calorie_needs": 0,
        "macros": {},
        "food_preferences": {
            "vegetarian": False,
            "vegan": False,
            "allergies": []
        }
    }

 if 'daily_food_log' not in st.session_state:
    st.session_state.daily_food_log = []

 if 'daily_nutrition' not in st.session_state:
    st.session_state.daily_nutrition = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "fiber": 0,
        "vitamins": {},
        "minerals": {},
        "folic_acid": 0
    }

# Load databases
 food_db = load_food_database()
 meal_suggestions_db = load_meal_suggestions()
 
 st.subheader("Your Personal Nutrition Assistant")

# Create tabs for different sections
 tab1, tab2, tab3, tab4 = st.tabs(["📊 Profile", "🍽️ Food Tracker", "🧠 AI Meal Planner", "📘 Nutrition Education"])
 # Tab 1: User Profile and Nutrition Calculator
 with tab1:
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Personal Information")
        
        name = st.text_input("Name", st.session_state.user_data["name"])
        age = st.number_input("Age", min_value=15, max_value=100, value=st.session_state.user_data["age"])
        gender = st.selectbox("Gender", ["Male", "Female"], index=0 if st.session_state.user_data["gender"] == "Male" else 1)
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=250.0, value=float(st.session_state.user_data["weight"]))
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=float(st.session_state.user_data["height"]))
        
        # Food preferences
        st.subheader("Food Preferences")
        vegetarian = st.checkbox("Vegetarian", value=st.session_state.user_data["food_preferences"]["vegetarian"])
        vegan = st.checkbox("Vegan", value=st.session_state.user_data["food_preferences"]["vegan"])
        allergies = st.multiselect(
            "Food Allergies/Restrictions",
            options=list(food_db.keys()),
            default=st.session_state.user_data["food_preferences"]["allergies"]
        )
    
    with col2:
        st.subheader("Fitness Goals")
        
        activity_level = st.selectbox(
            "Activity Level",
            ["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"],
            index=["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"].index(st.session_state.user_data["activity_level"])
        )
        
        goal = st.selectbox(
            "Primary Goal",
            ["Weight loss", "Maintenance", "Muscle gain"],
            index=["Weight loss", "Maintenance", "Muscle gain"].index(st.session_state.user_data["goal"])
        )
        
        # Calculate button
        if st.button("Calculate My Nutrition Plan"):
            # Calculate BMR
            bmr = calculate_bmr(weight, height, age, gender)
            
            # Calculate daily calorie needs
            calorie_needs = calculate_calorie_needs(bmr, activity_level)
            
            # Calculate macronutrient distribution
            macros = calculate_macros(calorie_needs, goal)
            
            # Update session state
            st.session_state.user_data.update({
                "name": name,
                "age": age,
                "weight": weight,
                "height": height,
                "gender": gender,
                "activity_level": activity_level,
                "goal": goal,
                "bmr": bmr,
                "calorie_needs": calorie_needs,
                "macros": macros,
                "food_preferences": {
                    "vegetarian": vegetarian,
                    "vegan": vegan,
                    "allergies": allergies
                }
            })
            
            st.success("Your nutrition plan has been calculated!")
    
    # Display calculated nutrition plan if available
    if st.session_state.user_data["bmr"] > 0:
        st.subheader("Your Personalized Nutrition Plan")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Daily Calories", f"{int(st.session_state.user_data['calorie_needs'])} kcal")
        
        with col2:
            st.metric("Protein", f"{st.session_state.user_data['macros']['protein']} g")
        
        with col3:
            st.metric("Carbohydrates", f"{st.session_state.user_data['macros']['carbs']} g")
        
        with col4:
            st.metric("Fats", f"{st.session_state.user_data['macros']['fat']} g")
        
        # Recommendations based on goals
        st.subheader("Recommendations Based on Your Goal")
        
        if st.session_state.user_data["goal"] == "Weight loss":
            st.info("""
            **Weight Loss Tips:**
            - Aim for a moderate caloric deficit (300-500 calories below maintenance)
            - Focus on high-protein foods to preserve muscle mass
            - Include plenty of fiber-rich foods to maintain satiety
            - Stay hydrated by drinking water throughout the day
            - Consider intermittent fasting if it fits your lifestyle
            """)
        elif st.session_state.user_data["goal"] == "Muscle gain":
            st.info("""
            **Muscle Gain Tips:**
            - Consume a caloric surplus (300-500 calories above maintenance)
            - Prioritize protein intake to support muscle growth
            - Distribute protein intake evenly throughout the day
            - Focus on nutrient-dense whole foods
            - Consider timing carbohydrates around your workouts
            """)
        else:  # Maintenance
            st.info("""
            **Maintenance Tips:**
            - Focus on nutrient-dense whole foods
            - Maintain consistent meal timing
            - Distribute macronutrients based on your energy needs
            - Stay hydrated and consume adequate fiber
            - Adjust intake based on activity levels day-to-day
            """)

 # Tab 2: Food Tracker
 with tab2:
    st.header("Daily Food Tracker")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add Food to Today's Log")
        food_input_method = st.radio("How would you like to add food?", ["Select from database", "Describe what you ate"])
        
        if food_input_method == "Select from database":
            selected_food = st.selectbox("Select food", list(food_db.keys()))
            quantity = st.number_input("Quantity", min_value=0.25, max_value=10.0, value=1.0, step=0.25)
            
            if st.button("Add to Log"):
                # Add to daily food log
                st.session_state.daily_food_log.append({
                    "time": datetime.now().strftime("%H:%M"),
                    "food": selected_food,
                    "quantity": quantity
                })
                
                # Recalculate daily nutrition
                st.session_state.daily_nutrition = calculate_nutrition(st.session_state.daily_food_log, food_db)
                st.success(f"Added {quantity} {selected_food} to your log!")
        
        else:  # Describe what you ate
            food_description = st.text_area("Describe what you ate (e.g., '2 apples, 1 chicken breast, and a cup of rice')")
            
            if st.button("Analyze & Add"):
                food_items = analyze_food_input(food_description, food_db)
                
                if food_items:
                    # Add all identified food items to the log
                    for item in food_items:
                        st.session_state.daily_food_log.append({
                            "time": datetime.now().strftime("%H:%M"),
                            "food": item["food"],
                            "quantity": item["quantity"]
                        })
                    
                    # Recalculate daily nutrition
                    st.session_state.daily_nutrition = calculate_nutrition(st.session_state.daily_food_log, food_db)
                    st.success(f"Added {len(food_items)} food items to your log!")
                else:
                    st.warning("No known food items were recognized. Try being more specific or use the database selection method.")
    
    with col2:
        st.subheader("Today's Food Log")
        
        if st.session_state.daily_food_log:
            # Create a DataFrame for better display
            log_data = []
            for item in st.session_state.daily_food_log:
                food_nutrients = food_db[item["food"]]
                log_data.append({
                    "Time": item["time"],
                    "Food": item["food"].title(),
                    "Quantity": item["quantity"],
                    "Calories": round(food_nutrients["calories"] * item["quantity"])
                })
            
            log_df = pd.DataFrame(log_data)
            st.dataframe(log_df, use_container_width=True)
            
            # Option to clear log
            if st.button("Clear Today's Log"):
                st.session_state.daily_food_log = []
                st.session_state.daily_nutrition = {
                    "calories": 0,
                    "protein": 0,
                    "carbs": 0,
                    "fat": 0,
                    "fiber": 0,
                    "vitamins": {},
                    "minerals": {},
                    "folic_acid": 0
                }
                st.success("Food log cleared!")
        else:
            st.info("Your food log is empty. Add some food to get started!")
    
    # Display nutrition summary if food has been logged
    if st.session_state.daily_nutrition["calories"] > 0:
        st.subheader("Today's Nutrition Summary")
        
        # Progress toward calorie goal
        calorie_goal = st.session_state.user_data.get("calorie_needs", 2000)
        calorie_progress = min(st.session_state.daily_nutrition["calories"] / calorie_goal, 1.0)
        
        st.write(f"**Calories:** {st.session_state.daily_nutrition['calories']} / {int(calorie_goal)} kcal")
        st.progress(calorie_progress)
        
        # Macronutrient breakdown
        col1, col2, col3 = st.columns(3)
        
        with col1:
            protein_goal = st.session_state.user_data.get("macros", {}).get("protein", 0)
            protein_progress = min(st.session_state.daily_nutrition["protein"] / protein_goal, 1.0) if protein_goal > 0 else 0
            st.write(f"**Protein:** {st.session_state.daily_nutrition['protein']}g / {protein_goal}g")
            st.progress(protein_progress)
        
        with col2:
            carbs_goal = st.session_state.user_data.get("macros", {}).get("carbs", 0)
            carbs_progress = min(st.session_state.daily_nutrition["carbs"] / carbs_goal, 1.0) if carbs_goal > 0 else 0
            st.write(f"**Carbs:** {st.session_state.daily_nutrition['carbs']}g / {carbs_goal}g")
            st.progress(carbs_progress)
        
        with col3:
            fat_goal = st.session_state.user_data.get("macros", {}).get("fat", 0)
            fat_progress = min(st.session_state.daily_nutrition["fat"] / fat_goal, 1.0) if fat_goal > 0 else 0
            st.write(f"**Fat:** {st.session_state.daily_nutrition['fat']}g / {fat_goal}g")
            st.progress(fat_progress)
        
        # More detailed breakdown
        with st.expander("View Detailed Nutrition Breakdown"):
            st.write(f"**Fiber:** {st.session_state.daily_nutrition['fiber']}g")
            st.write(f"**Folic Acid:** {st.session_state.daily_nutrition['folic_acid']}mcg")
            
            # Vitamins
            st.subheader("Vitamins")
            vitamin_data = []
            for vitamin, amount in st.session_state.daily_nutrition["vitamins"].items():
                vitamin_data.append({"Vitamin": vitamin, "Amount (% Daily Value)": amount})
            
            if vitamin_data:
                st.dataframe(pd.DataFrame(vitamin_data), use_container_width=True)
            else:
                st.info("No vitamin data available.")
            
            # Minerals
            st.subheader("Minerals")
            mineral_data = []
            for mineral, amount in st.session_state.daily_nutrition["minerals"].items():
                mineral_data.append({"Mineral": mineral, "Amount (% Daily Value)": amount})
            
            if mineral_data:
                st.dataframe(pd.DataFrame(mineral_data), use_container_width=True)
            else:
                st.info("No mineral data available.")
        
        # Quality rating
        quality_rating = rate_nutrition_quality(st.session_state.daily_nutrition, st.session_state.user_data)
        
        st.subheader("Nutrition Quality Score")
        st.metric("Score", f"{quality_rating['score']}/100")
        
        for feedback in quality_rating["feedback"]:
            st.write(feedback)

 # Tab 3: AI Meal Planner
 with tab3:
    st.header("AI-Powered Meal Planner")
    
    # Generate meal suggestions based on user data
    if st.session_state.user_data["bmr"] > 0:
        if st.button("Generate Meal Suggestions"):
            meal_suggestions = generate_meal_suggestions(st.session_state.user_data, food_db, meal_suggestions_db)
            
            if meal_suggestions:
                st.success("Here are your personalized meal suggestions!")
                
                # Display meal suggestions in a nice format
                for meal_type, meal in meal_suggestions.items():
                    st.subheader(f"{meal_type.title()}: {meal['name']}")
                    
                    # Calculate nutrition for the meal
                    meal_items = [{"food": item, "quantity": 1} for item in meal["items"]]
                    meal_nutrition = calculate_nutrition(meal_items, food_db)
                    
                    # Display description and nutrition
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.write(f"**Description:** {meal['description']}")
                        st.write(f"**Ingredients:** {', '.join([item.title() for item in meal['items']])}")
                    
                    with col2:
                        st.write(f"**Calories:** {meal_nutrition['calories']} kcal")
                        st.write(f"**Protein:** {meal_nutrition['protein']}g")
                        st.write(f"**Carbs:** {meal_nutrition['carbs']}g")
                        st.write(f"**Fat:** {meal_nutrition['fat']}g")
                    
                    # Add to log button
                    if st.button(f"Add {meal_type.title()} to Today's Log", key=f"add_{meal_type}"):
                        for item in meal["items"]:
                            st.session_state.daily_food_log.append({
                                "time": datetime.now().strftime("%H:%M"),
                                "food": item,
                                "quantity": 1
                            })
                        
                        # Recalculate daily nutrition
                        st.session_state.daily_nutrition = calculate_nutrition(st.session_state.daily_food_log, food_db)
                        st.success(f"Added {meal['name']} to your log!")
            else:
                st.warning("Could not generate meal suggestions. Please update your nutrition profile first.")
    else:
        st.info("Please complete your nutrition profile in the Profile tab first.")
    
    # Custom AI meal planning
    st.subheader("Generate Custom Meal Plan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        min_calories = st.number_input("Minimum calories per meal", 200, 1000, 300)
        max_calories = st.number_input("Maximum calories per meal", min_calories, 2000, min_calories + 200)
    
    with col2:
        min_protein = st.number_input("Minimum protein (g)", 10, 100, 20)
        custom_preference = st.text_input("Additional preferences (e.g., 'high fiber', 'low carb', etc.)")
    
    if st.button("Generate Custom Meal"):
        # This is a simplified approach - in a real app, you would use more sophisticated AI
        available_foods = [food for food in food_db.keys() 
                          if food not in st.session_state.user_data["food_preferences"]["allergies"]]
        
        if st.session_state.user_data["food_preferences"]["vegetarian"]:
            available_foods = [food for food in available_foods if food not in ["chicken breast", "salmon"]]
        
        if st.session_state.user_data["food_preferences"]["vegan"]:
            available_foods = [food for food in available_foods 
                              if food not in ["chicken breast", "salmon", "egg", "milk", "greek yogurt"]]
        
        # Simple algorithm to create a meal with desired properties
        meal_items = []
        current_calories = 0
        current_protein = 0
        
        # Add protein source first
        protein_foods = [food for food in available_foods if food_db[food]["protein"] > 5]
        if protein_foods:
            protein_food = random.choice(protein_foods)
            meal_items.append({"food": protein_food, "quantity": 1})
            current_calories += food_db[protein_food]["calories"]
            current_protein += food_db[protein_food]["protein"]
        
        # Add carb source
        carb_foods = [food for food in available_foods if food_db[food]["carbs"] > 15 and food not in [item["food"] for item in meal_items]]
        if carb_foods and current_calories < max_calories:
            carb_food = random.choice(carb_foods)
            meal_items.append({"food": carb_food, "quantity": 1})
            current_calories += food_db[carb_food]["calories"]
            current_protein += food_db[carb_food]["protein"]
        
        # Add vegetable or fruit
        plant_foods = [food for food in ["spinach", "broccoli", "sweet potato", "apple", "blueberries"] 
                      if food in available_foods and food not in [item["food"] for item in meal_items]]
        if plant_foods and current_calories < max_calories:
            plant_food = random.choice(plant_foods)
            meal_items.append({"food": plant_food, "quantity": 1})
            current_calories += food_db[plant_food]["calories"]
            current_protein += food_db[plant_food]["protein"]
        
        # Check if we meet the criteria
        if current_calories >= min_calories and current_calories <= max_calories and current_protein >= min_protein:
            # Calculate meal nutrition
            meal_nutrition = calculate_nutrition(meal_items, food_db)
            
            st.success("Custom meal generated!")
            
            # Display meal
            st.subheader(f"Custom Meal")
            st.write(f"**Ingredients:** {', '.join([item['food'].title() for item in meal_items])}")
            
            # Display nutrition info
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Calories", f"{meal_nutrition['calories']} kcal")
            with col2:
                st.metric("Protein", f"{meal_nutrition['protein']}g")
            with col3:
                st.metric("Carbs", f"{meal_nutrition['carbs']}g")
            with col4:
                st.metric("Fat", f"{meal_nutrition['fat']}g")
            
            # Add to log button
            if st.button("Add Custom Meal to Today's Log"):
                for item in meal_items:
                    st.session_state.daily_food_log.append({
                        "time": datetime.now().strftime("%H:%M"),
                        "food": item["food"],
                        "quantity": item["quantity"]
                    })
                
                # Recalculate daily nutrition
                st.session_state.daily_nutrition = calculate_nutrition(st.session_state.daily_food_log, food_db)
                st.success("Added custom meal to your log!")
        else:
            st.warning("Could not generate a meal meeting your criteria. Try adjusting your parameters.")

 # Tab 4: Nutrition Education
 with tab4:
  # Simplified CSS without animations and popup effects
    st.markdown("""
    <style>
        /* Main app background */
        .stApp {
            background-color: #F0FFF0;
        }
        
        /* Headers */
        h1 {
            color: #4a7c59;
            font-family: 'Georgia', serif;
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #c8e0d2;
        }
        
        h2 {
            color: #3a6650;
            font-family: 'Georgia', serif;
            font-size: 28px;
            margin-top: 30px;
            padding-bottom: 5px;
            border-bottom: 1px solid #c8e0d2;
        }
        
        h3 {
            color: #5a8f72;
            font-family: 'Georgia', serif;
            font-size: 22px;
            margin-top: 20px;
        }
        
        /* Text styling */
        p {
            font-family: 'Arial', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        }
        
        /* Lists */
        ul, ol {
            font-family: 'Arial', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        }
        
        /* Highlights */
        .highlight {
            background-color: #e8f3ec;
            border-left: 5px solid #4a7c59;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
        }
        
        /* Card styling */
        .card {
            background-color: #e8f3ec;
            border: 1px solid #a9d0a9;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }
        
        .card_item{
            background-color:white;
            border: 1px solid #a9d0a9;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }
        
        /* Section divider */
        .divider {
            height: 2px;
            background-color: #c8e0d2;
            margin: 30px 0;
            border: none;
        }
        
        /* Food category badges */
        .food-badge {
            display: inline-block;
            background-color: #d4e8dd;
            color: #3a6650;
            padding: 4px 8px;
            border-radius: 4px;
            margin: 3px;
            font-size: 14px;
            font-weight: 500;
        }
        
        /* Info and warning boxes */
        .info-box {
            background-color: #e8f3ec;
            border-left: 5px solid #4a7c59;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        
        .warning-box {
            background-color: #fff3e0;
            border-left: 5px solid #ff9800;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        
        /* Accent colors */
        .accent-green {
            color: #5a8f72;
            font-weight: bold;
        }
        
        /* Table styling */
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            color: #3a6650;
            font-family: Arial, sans-serif;
            border-radius: 5px;
            overflow: hidden;
            margin-bottom: 30px;
            border: 1px solid #e0eae3;
        }
        
        .custom-table th {
            background-color: #5a8f72;
            color: white;
            padding: 12px;
            text-align: center;
            font-weight: bold;
        }
        
        .custom-table td {
            padding: 10px 12px;
            border-bottom: 1px solid #e0eae3;
        }
        
        .custom-table tr:nth-child(even) {
            background-color: #f0f7f3;
        }
        
        .custom-table tr:nth-child(odd) {
            background-color: white;
        }
        
        /* Image caption */
        .image-caption {
            text-align: center;
            font-style: italic;
            color: #666;
            margin-top: 5px;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1>Healthy Pregnancy Diet Guide</h1>', unsafe_allow_html=True)

    # Introduction with simplified layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("")
        st.markdown("""
        <div class="card">
            <h3>Nourishing You and Your Baby</h3>
            <p>When you're pregnant, your eating habits become more important than ever, affecting your health, the way you feel, and, of course, your baby! Healthy pregnancy meals and snacks contain a good balance of nutrients, including protein, carbohydrates, and fats, helping to keep you well and supporting your little one's growth and development.</p>
            <p>This guide will help you understand:</p>
            <ul>
                <li>What makes a healthy pregnancy diet</li>
                <li>Essential nutrients for you and your baby</li>
                <li>Best foods to include in your meals</li>
                <li>Foods to avoid during pregnancy</li>
                <li>Healthy beverage choices</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.write("")#empty space
        st.write("")
        st.write("")
        st.image("C:/Pregnancy_risk_Prediction-master/images/Pregnancy_Diet_original_720x432.webp")
        st.markdown("""
        <p class="image-caption">A balanced diet is essential during pregnancy</p>
        """, unsafe_allow_html=True)

    # Section divider
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Section 1: What is a Healthy Pregnancy Diet?
    st.markdown("<h2>What is a Healthy Pregnancy Diet?</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
        <p>A healthy pregnancy diet isn't about losing weight or simply "eating for two." It's about consuming a variety of nutrient-rich foods that support your baby's development while maintaining your health.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p>When planning your pregnancy meals, focus on these key principles:</p>

    <div class="card">
        <h3>Key Principles of a Healthy Pregnancy Diet</h3>
        <p><strong>🍽️ Vary your plate</strong>: Aim for a mix of proteins, carbohydrates, fats, minerals, and vitamins from the five food groups: fruits, vegetables, grains, protein, and dairy. A simple approach: fill half your plate with fruits and vegetables and the other half with grains and proteins.</p>
        <p><strong>🥛 Choose low-fat dairy</strong>: Both skim milk and 1-percent milk are excellent choices for getting the calcium you need.</p>
        <p><strong>🌾 Prioritize whole grains</strong>: Whole grains provide more dietary fiber than refined options. Include whole wheat bread, whole grain pasta, quinoa, brown rice, and oatmeal in your diet.</p>
        <p><strong>⚠️ Limit less healthy options</strong>: Minimize foods high in saturated fat, trans fat, added sugar, and sodium. For blood pressure management, try flavoring foods with lemon juice, herbs, and spices rather than salt.</p>
    </div>
    """, unsafe_allow_html=True)

    # Food plate image
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("C:/Pregnancy_risk_Prediction-master/images/Food_For_Pregnancy.webp")
        st.write("Produce containing Vitamin C, like oranges, strawberries, bell peppers, and broccoli, support the baby's growth and improves iron absorption. Foods that have iron, such as beans, lentils, green leafy vegetables, meat, and spinach all support the mother's body in making more blood for both mom and baby.")
        st.write("What you eat during pregnancy affects not only your own health and wellbeing and the development of your baby, but there is also substantial evidence that it can have a lasting impact on the health and wellbeing of your child later in life.")
    
    with col2:
        st.write("Fill your plate with healthy proteins. Foods rich in protein will effectively support your baby's growth and at the same time, provide you the energy that your body needs. It will also promote your baby's healthy brain and heart development.")
        st.image("C:/Pregnancy_risk_Prediction-master/images/Food_Plate.jpg")

    st.markdown("""
    <p class="image-caption">A balanced plate with foods from all food groups is ideal during pregnancy</p>
    """, unsafe_allow_html=True)

    # Quick Nutrition Tips
    st.markdown("""
    <div class="info-box">
        <h3>Quick Nutrition Tips</h3>
        <p>Eating small, frequent meals can help manage morning sickness and maintain stable blood sugar levels.</p>
        <p>Try to include a protein source with each meal to help keep you feeling satisfied.</p>
        <p>Keep healthy snacks readily available for when hunger strikes.</p>
    </div>
    """, unsafe_allow_html=True)

    # Section divider
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Section 2: Pregnancy Nutrition
    st.markdown("<h2>Pregnancy Nutrition: Essential Nutrients</h2>", unsafe_allow_html=True)

    st.markdown("""
    <p>During pregnancy, your body needs additional nutrients to support your changing body and your growing baby. A balanced diet with variety is key to getting what you both need.</p>
    """, unsafe_allow_html=True)

    # Key nutritional needs without animations
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <h3>600</h3>
            <p>mcg Folic Acid Daily</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <h3>27</h3>
            <p>mg Iron Daily</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <h3>1000</h3>
            <p>mg Calcium Daily</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>Spotlight on Key Nutrients</h3>
            <p><strong>Folic Acid</strong>: Critical for preventing birth defects of the brain and spine. Start taking it before conception, if possible.</p>
            <p><strong>Iron</strong>: Helps you produce more blood, which you, your developing baby, and the placenta all need. Not getting enough can lead to anemia and fatigue.</p>
            <p><strong>Calcium</strong>: Essential for building your baby's bones and teeth. If your diet lacks calcium, your body will take it from your bones to give to your baby.</p>
            <p><strong>Vitamin D</strong>: Works with calcium for bone development and helps with immune function.</p>
            <p>While a prenatal vitamin can provide a nutritional boost, a well-rounded diet should be your primary source of nutrients. Talk to your healthcare provider about whether you need additional supplements based on your specific needs.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("C:/Pregnancy_risk_Prediction-master/images/meal plan.jpg")
        st.markdown("""
        <p class="image-caption">Planning nutrient-rich meals is important during pregnancy</p>
        """, unsafe_allow_html=True)

    # Nutrition Table with simplified styling
    st.markdown("<h3>Essential Pregnancy Nutrients Guide</h3>", unsafe_allow_html=True)

    st.markdown("""
    <table class="custom-table">
      <thead>
        <tr>
          <th>Nutrient</th>
          <th>Daily Needs</th>
          <th>Food Sources</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Protein</strong></td>
          <td>About 5-6 ounces daily<br>(1 egg or ½ cup nuts = ~1 oz)</td>
          <td>• Lean meats<br>• Poultry<br>• Fish<br>• Dried beans<br>• Nuts<br>• Eggs<br>• Cheese</td>
        </tr>
        <tr>
          <td><strong>Complex Carbohydrates</strong></td>
          <td>About 5-6 cups daily from mixed sources</td>
          <td>• Whole grains (bread, rice, pasta)<br>• Vegetables (leafy greens, orange vegetables)</td>
        </tr>
        <tr>
          <td><strong>Fats and Oils</strong></td>
          <td>5 teaspoons (1st trimester) to 8 teaspoons (3rd trimester)</td>
          <td>• Olives<br>• Olive oil<br>• Fish<br>• Avocados<br>• Nuts</td>
        </tr>
        <tr>
          <td><strong>Calcium</strong></td>
          <td>1,000 mg daily<br>(1,300 mg if under 19)</td>
          <td>• Green leafy vegetables<br>• Fortified orange juice<br>• Milk (1 cup = 300 mg)<br>• Yogurt<br>• Cheese<br>• Sardines</td>
        </tr>
        <tr>
          <td><strong>Iron</strong></td>
          <td>27 mg daily</td>
          <td>• Poultry<br>• Whole grains<br>• Leafy greens<br>• Beans and peas<br>• Dried fruits<br>• Eggs<br>• Lean red meat<br>• Tofu</td>
        </tr>
        <tr>
          <td><strong>Vitamin D</strong></td>
          <td>600 IU daily</td>
          <td>• Sunlight exposure<br>• Fortified milk and cereal<br>• Fatty fish (salmon and sardines)</td>
        </tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)

    # Section divider
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Section 3: Best Foods to Eat
    st.markdown("<h2>21 Best Foods for a Healthy Pregnancy</h2>", unsafe_allow_html=True)

    st.markdown("""
    <p>Not sure what to include in your pregnancy diet meal plan? Here are 21 nutritious foods that provide essential nutrients for you and your baby:</p>
    """, unsafe_allow_html=True)

    # Create three columns for the food list
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>Protein-Rich Foods</h3>
            <p><span class="food-badge">Eggs</span> Nutritional powerhouses with protein and vitamins</p>
            <p><span class="food-badge">Cheese</span> Rich in calcium (choose pasteurized varieties)</p>
            <p><span class="food-badge">Yogurt</span> Excellent source of calcium and probiotics</p>
            <p><span class="food-badge">Nuts & Seeds</span> Perfect portable snacks with protein and healthy fats</p>
            <p><span class="food-badge">Beans & Lentils</span> Provide fiber, folic acid, iron, and protein</p>
            <p><span class="food-badge">Tofu</span> Great alternative protein for vegetarians</p>
            <p><span class="food-badge">Fatty Fish</span> Contains omega-3 fatty acids for development</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>Fruits & Vegetables</h3>
            <p><span class="food-badge">Avocados</span> Contain many nutrients and healthy fats</p>
            <p><span class="food-badge">Citrus Fruit</span> Great source of vitamin C</p>
            <p><span class="food-badge">Berries</span> Provide vitamin C and antioxidants</p>
            <p><span class="food-badge">Bananas</span> High in fiber to combat constipation</p>
            <p><span class="food-badge">Dark Leafy Greens</span> Packed with nutrients</p>
            <p><span class="food-badge">Orange Vegetables</span> Rich in vitamin A</p>
            <p><span class="food-badge">Broccoli</span> High in fiber and vitamin C</p>
            <p><span class="food-badge">Spinach</span> One of the best iron-rich foods</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>Grains & Other Foods</h3>
            <p><span class="food-badge">Fortified Milk</span> Source of calcium and vitamin D</p>
            <p><span class="food-badge">Fortified Cereals</span> Provide essential vitamins and minerals</p>
            <p><span class="food-badge">Orange Juice</span> Good source of calcium and vitamin C</p>
            <p><span class="food-badge">Brown Rice</span> Includes the entire grain for more nutrients</p>
            <p><span class="food-badge">Whole-Grain Pasta</span> Better choice than refined pasta</p>
            <p><span class="food-badge">Olive Oil</span> Contains unsaturated fats and nutrients</p>
        </div>
        """, unsafe_allow_html=True)

    # Section divider
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Section 4: Foods to Avoid
    st.markdown("<h2>Pregnancy Diet: Foods to Avoid</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
        <p>While knowing what to eat during pregnancy is important, understanding what to avoid is equally crucial for the health of you and your baby.</p>
    </div>
    """, unsafe_allow_html=True)

    # General foods to avoid
    st.markdown("""
    <p>Here are the main categories of foods to be cautious about:</p>
    <ul>
        <li><strong>Certain types of fish</strong> (high in mercury, like shark, swordfish, king mackerel)</li>
        <li><strong>Unpasteurized milk and foods</strong> (which may contain harmful bacteria)</li>
        <li><strong>Raw or undercooked foods</strong> (meat, eggs, seafood)</li>
        <li><strong>Simple carbohydrates from processed foods</strong> (low nutritional value)</li>
        <li><strong>Trans fats</strong> (found in many processed foods)</li>
    </ul>
    """, unsafe_allow_html=True)

    # Create expandable sections for detailed information
    with st.expander("**Raw or Undercooked Meat & Seafood**"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <p>Eating undercooked or raw meat can increase your risk of infection from bacteria or parasites, including Toxoplasma, E. coli, Listeria, and Salmonella.</p>
            
            <p>These bacteria may threaten both your health and your baby's development and safety.</p>
            
            <p>While some whole cuts of meat might be safe when seared on the outside but rare inside, during pregnancy it's best to cook all meat thoroughly.</p>
            
            <p><strong>Remember:</strong> Cut meat, including burgers, patties, minced meat, pork, and poultry should never be consumed undercooked during pregnancy.</p>
            """, unsafe_allow_html=True)
        with col2:
            st.image("C:/Pregnancy_risk_Prediction-master/images/raw_meat.jpg")

    with st.expander("**Trans Fat and Processed Foods**"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <p>Processed meats like hot dogs, lunch meat, pepperoni, and deli meat can become contaminated with bacteria during processing or storage.</p>
            
            <p>Cured meats that aren't cooked may also harbor bacteria or parasites.</p>
            
            <p>Additionally, processed foods often contain high levels of sodium, unhealthy fats, and preservatives that aren't beneficial during pregnancy.</p>
            
            <p><strong>Recommendation:</strong> Avoid deli meats unless heated until steaming hot, and ensure all processed meats are thoroughly cooked.</p>
            """, unsafe_allow_html=True)
        with col2:
            st.image("C:/Pregnancy_risk_Prediction-master/images/processed_food.webp")

    with st.expander("**Raw Sprouts**"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <p>Raw sprouts, including alfalfa, clover, radish, and mung bean sprouts, are popular in salads.</p>       
             
            <p>However, the humid environment in which the seeds need to start sprouting is ideal for the growth of Salmonella, and it's almost impossible to wash off.</p>
            
            <p>For this reason, it's best to avoid raw sprouts altogether, although sprouts are safe to consume when cooked, according to the FDA.</p>
            """, unsafe_allow_html=True)
        with col2:
            st.image("C:/Pregnancy_risk_Prediction-master/images/raw_sprout.jpg")        

    with st.expander("**Unpasteurized Dairy Products**"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            <p>Raw milk and other unpasteurized dairy products can contain harmful bacteria, including Listeria, Salmonella, E. coli, and Campylobacter. These bacteria can cause a range of infections commonly called food poisoning.</p>       
             
            <p>These infections can all have life threatening consequences for an unborn baby.</p>
            
            <p>The bacteria can occur naturally or result from contamination during collection or storage. Pasteurization can kill any harmful bacteria without changing the nutritional value of the products.</p>
            
            <p>To reduce the risk of infections, eat only pasteurized dairy products.</p>
            """, unsafe_allow_html=True)
        with col2:
            st.image("C:/Pregnancy_risk_Prediction-master/images/milk.jpg")        

    st.markdown("""
    <p>Always consult your healthcare provider about specific foods you should avoid based on your personal health history and needs.</p>
    """, unsafe_allow_html=True)

    # Section divider
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Section 5: Beverages
    st.markdown("<h2>Pregnancy Diet: Healthy Beverage Choices</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
        <p>Staying hydrated is crucial during pregnancy. You'll need to drink 8 to 12 cups of fluids daily, with water being the best option.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="card">
            <h3>Recommended Beverages</h3>
            <ul>
                <li><strong>Water:</strong> The ideal choice - helps prevent constipation, maintains skin health, and flushes toxins</li>
                <li><strong>Milk:</strong> Good source of calcium and protein</li>
                <li><strong>Fruit-infused water:</strong> Adds flavor without added sugar</li>
                <li><strong>Limited coffee/tea:</strong> Keep caffeine under 200 mg daily (about 1-2 cups of coffee)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>Beverages to Limit or Avoid</h3>
            <ul>
                <li><strong>Alcohol:</strong> Best avoided completely during pregnancy</li>
                <li><strong>Soda:</strong> High in sugar or artificial sweeteners</li>
                <li><strong>Unpasteurized juices:</strong> May contain harmful bacteria</li>
                <li><strong>Herbal teas:</strong> Some herbs may not be safe - check with your healthcare provider</li>
                <li><strong>Energy drinks:</strong> High in caffeine and other stimulants</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Section divider
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Section 6: Foods that support during pregnancy
    
    st.markdown("<h2>Foods that Support Your Pregnancy Journey</h2>", unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div class="card_item">
        <h3>The Power of Fruits and Vegetables</h3>
        <p>Eating plenty of fruits and vegetables during pregnancy provides:</p>
        <ul>
            <li><strong>Essential vitamins and minerals</strong> for your baby's development</li>
            <li><strong>Dietary fiber</strong> to help with digestion and prevent constipation</li>
            <li><strong>Antioxidants</strong> that support your immune system</li>
            <li><strong>Hydration</strong> from water-rich produce</li>
        </ul>
        <p>Aim for at least 5 portions of varied fruits and vegetables every day. These can be:</p>
        <ul>
            <li>Fresh</li>
            <li>Frozen</li>
            <li>Canned (in water or natural juice)</li>
            <li>Dried</li>
            <li>Juiced (limit to one small glass per day)</li>
        </ul>
        <p><strong>Remember:</strong> Always wash fresh produce thoroughly to remove any potential contaminants.</p>
    </div>
    """, unsafe_allow_html=True)   

    # Final section - Conclusion/Summary
    st.markdown("""
    <div class="highlight">
        <h3>Your Pregnancy Diet: Key Takeaways</h3>
        <ul>
            <li><strong>Focus on variety:</strong> Include foods from all food groups for complete nutrition</li>
            <li><strong>Prioritize nutrient-dense foods:</strong> Choose options rich in protein, iron, calcium, and folic acid</li>
            <li><strong>Stay hydrated:</strong> Drink plenty of water throughout the day</li>
            <li><strong>Avoid risky foods:</strong> Skip raw/undercooked meats, unpasteurized dairy, and high-mercury fish</li>
            <li><strong>Consult your healthcare provider:</strong> For personalized nutrition advice during your pregnancy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <p style="text-align: center; color: #666; margin-top: 30px;">This guide is for informational purposes only and is not a substitute for professional medical advice. Always consult with your healthcare provider regarding your specific pregnancy needs.</p>
    """, unsafe_allow_html=True)

# Main function to run the app
def main():   
 show_food_content()

