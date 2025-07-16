import streamlit as st
import pandas as pd

# Custom CSS for better appearance
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .title {
        font-size: 2.5rem;
        color: #ff6699;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .symptom-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #ff6699;
    }
    .disclaimer {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 10px;
        margin-top: 20px;
        font-style: italic;
    }
    .example-text {
        color: #6c757d;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Create the pregnancy symptoms database
@st.cache_data
def load_symptoms_data():
    # This would typically be loaded from a CSV or database, but we're creating it directly here
    data = {
        "symptom": [
            "nausea", "morning sickness", "vomiting", "throw up", "throwing up",
            "fatigue", "tiredness", "exhaustion", "tired", "no energy",
            "headache", "headaches", "migraine", "head pain", "head pressure",
            "backache", "back pain", "back ache", "back hurts", "sore back",
            "swelling", "edema", "swollen feet", "swollen ankles", "swollen hands",
            "heartburn", "acid reflux", "indigestion", "acid", "burning chest",
            "constipation", "difficult bowel movements", "hard stool", "can't poop",
            "insomnia", "trouble sleeping", "sleep problems", "can't sleep", "poor sleep",
            "frequent urination", "peeing often", "bathroom trips", "urge to pee",
            "breast tenderness", "sore breasts", "sensitive breasts", "breast pain",
            "mood swings", "emotional changes", "irritability", "moody", "emotions",
            "cravings", "food aversions", "appetite changes", "hunger", "wanting foods",
            "stretch marks", "skin changes", "itchy skin", "belly marks",
            "shortness of breath", "breathlessness", "hard to breathe", "out of breath",
            "leg cramps", "muscle cramps", "leg pain", "calf pain", "sore legs",
            "dizziness", "lightheadedness", "fainting", "dizzy", "spinning",
            "bleeding gums", "dental issues", "gum sensitivity", "gum pain"
        ],
        "category": [
            "digestive", "digestive", "digestive", "digestive", "digestive",
            "energy", "energy", "energy", "energy", "energy",
            "pain", "pain", "pain", "pain", "pain",
            "pain", "pain", "pain", "pain", "pain",
            "circulation", "circulation", "circulation", "circulation", "circulation",
            "digestive", "digestive", "digestive", "digestive", "digestive",
            "digestive", "digestive", "digestive", "digestive",
            "sleep", "sleep", "sleep", "sleep", "sleep",
            "urinary", "urinary", "urinary", "urinary",
            "physical", "physical", "physical", "physical",
            "emotional", "emotional", "emotional", "emotional", "emotional",
            "digestive", "digestive", "digestive", "digestive", "digestive",
            "skin", "skin", "skin", "skin",
            "respiratory", "respiratory", "respiratory", "respiratory",
            "muscular", "muscular", "muscular", "muscular", "muscular",
            "neurological", "neurological", "neurological", "neurological", "neurological",
            "oral", "oral", "oral", "oral"
        ],
        "primary_term": [
            "nausea", "nausea", "nausea", "nausea", "nausea",
            "fatigue", "fatigue", "fatigue", "fatigue", "fatigue",
            "headache", "headache", "headache", "headache", "headache",
            "back pain", "back pain", "back pain", "back pain", "back pain",
            "swelling", "swelling", "swelling", "swelling", "swelling",
            "heartburn", "heartburn", "heartburn", "heartburn", "heartburn",
            "constipation", "constipation", "constipation", "constipation",
            "insomnia", "insomnia", "insomnia", "insomnia", "insomnia",
            "frequent urination", "frequent urination", "frequent urination", "frequent urination",
            "breast tenderness", "breast tenderness", "breast tenderness", "breast tenderness",
            "mood swings", "mood swings", "mood swings", "mood swings", "mood swings",
            "cravings", "cravings", "cravings", "cravings", "cravings",
            "stretch marks", "stretch marks", "stretch marks", "stretch marks",
            "shortness of breath", "shortness of breath", "shortness of breath", "shortness of breath",
            "leg cramps", "leg cramps", "leg cramps", "leg cramps", "leg cramps",
            "dizziness", "dizziness", "dizziness", "dizziness", "dizziness",
            "bleeding gums", "bleeding gums", "bleeding gums", "bleeding gums"
        ]
    }
    return pd.DataFrame(data)

# Load the detailed information for each primary symptom
@st.cache_data
def load_symptom_details():
    details = {
        "nausea": {
            "description": "Nausea and vomiting (morning sickness) are common during the first trimester, though they can persist throughout pregnancy for some women.",
            "common_timing": "Most common in first trimester (weeks 6-12), but can occur anytime during pregnancy.",
            "self_care": [
                "Eat small, frequent meals instead of large ones",
                "Avoid foods with strong smells that trigger nausea",
                "Try ginger tea, ginger candies, or ginger supplements",
                "Eat plain crackers before getting out of bed in the morning",
                "Stay hydrated with small sips of water throughout the day",
                "Try acupressure wristbands designed for motion sickness",
                "Avoid lying down immediately after eating"
            ],
            "when_to_call": [
                "You can't keep any food or fluids down for 24 hours",
                "You're urinating less frequently or your urine is dark in color",
                "You feel dizzy or faint when standing up",
                "You have severe vomiting with pain or fever",
                "You vomit blood or material that looks like coffee grounds"
            ]
        },
        "fatigue": {
            "description": "Extreme tiredness is very common during pregnancy, especially in the first and third trimesters.",
            "common_timing": "Most intense during first trimester and late in the third trimester.",
            "self_care": [
                "Accept that you need more rest and sleep when possible",
                "Take short naps during the day if you can",
                "Maintain light exercise like walking to boost energy",
                "Stay hydrated and eat iron-rich foods",
                "Ask for help with household tasks and responsibilities",
                "Prioritize essential activities and rest when needed",
                "Consider prenatal yoga or gentle stretching"
            ],
            "when_to_call": [
                "Fatigue is severe and doesn't improve with rest",
                "You experience dizziness or shortness of breath with fatigue",
                "You have symptoms of depression alongside fatigue",
                "You have a rapid or irregular heartbeat"
            ]
        },
        "headache": {
            "description": "Headaches during pregnancy can be caused by hormonal changes, increased blood volume, stress, and other factors.",
            "common_timing": "Common throughout pregnancy, though patterns may vary.",
            "self_care": [
                "Practice relaxation techniques and stress management",
                "Apply a cold or warm compress to your head or neck",
                "Maintain regular sleep patterns",
                "Stay hydrated and avoid skipping meals",
                "Practice good posture, especially late in pregnancy",
                "Try prenatal massage or gentle neck stretches",
                "Avoid known triggers like certain foods or bright lights"
            ],
            "when_to_call": [
                "Headache is severe or different from your usual headaches",
                "You experience blurred vision, spots, or other visual disturbances",
                "Your headache is accompanied by swelling or sudden weight gain",
                "You have a fever or stiff neck with your headache",
                "Your headache doesn't respond to acetaminophen (after consulting your doctor)"
            ]
        },
        "back pain": {
            "description": "Back pain, especially lower back pain, is very common during pregnancy due to weight gain, posture changes, and hormones that relax joints.",
            "common_timing": "Usually begins in second trimester and intensifies in third trimester.",
            "self_care": [
                "Practice good posture and avoid standing for long periods",
                "Wear supportive, low-heeled shoes",
                "Use a maternity support belt to reduce strain",
                "Sleep on your side with pillows between knees and under abdomen",
                "Apply heat or cold to the painful area",
                "Try gentle stretching, prenatal yoga, or water exercises",
                "Consider prenatal massage from a certified therapist"
            ],
            "when_to_call": [
                "Pain is severe, constant, or progressively worsening",
                "Back pain is accompanied by vaginal bleeding or discharge",
                "You have fever along with back pain",
                "Pain radiates to legs or is accompanied by numbness",
                "You experience difficulty urinating or burning with urination"
            ]
        },
        "swelling": {
            "description": "Edema (swelling), especially in the feet, ankles, and hands, is normal during pregnancy due to increased blood volume and pressure on veins.",
            "common_timing": "Usually begins in second trimester and increases in third trimester.",
            "self_care": [
                "Elevate your feet when sitting or lying down",
                "Avoid standing for long periods of time",
                "Wear comfortable, supportive shoes and loose socks",
                "Drink plenty of water (counterintuitively helps reduce water retention)",
                "Reduce sodium intake in your diet",
                "Exercise regularly with gentle activities like walking or swimming",
                "Sleep on your left side to reduce pressure on major blood vessels"
            ],
            "when_to_call": [
                "Swelling is sudden or severe, especially in your face or around your eyes",
                "One leg is significantly more swollen than the other",
                "Swelling is accompanied by headache, vision changes, or abdominal pain",
                "You gain more than 1 pound (0.5 kg) in a day",
                "You have decreased urination despite swelling"
            ]
        },
        "heartburn": {
            "description": "Heartburn and acid reflux are common during pregnancy due to hormonal changes and pressure from the growing uterus.",
            "common_timing": "Can begin in first trimester but typically worsens in second and third trimesters.",
            "self_care": [
                "Eat smaller, more frequent meals instead of large ones",
                "Avoid lying down immediately after eating (wait 2-3 hours)",
                "Sleep with your upper body elevated on pillows",
                "Avoid spicy, fatty, or fried foods that trigger symptoms",
                "Drink fluids between meals rather than with meals",
                "Avoid tight-fitting clothes that put pressure on your abdomen",
                "Chew gum after eating to increase saliva production"
            ],
            "when_to_call": [
                "Heartburn is severe and not relieved by lifestyle changes or approved antacids",
                "You experience difficulty swallowing or painful swallowing",
                "You have severe chest pain that might be confused with heart issues",
                "You notice weight loss due to difficulty eating",
                "You have persistent nausea and vomiting with heartburn"
            ]
        },
        "constipation": {
            "description": "Constipation during pregnancy is caused by hormonal changes, prenatal vitamins (especially iron), and pressure from the growing uterus.",
            "common_timing": "Can occur throughout pregnancy but often worsens as pregnancy progresses.",
            "self_care": [
                "Increase dietary fiber with fruits, vegetables, and whole grains",
                "Drink plenty of water throughout the day (at least 8-10 glasses)",
                "Exercise regularly with walking or swimming",
                "Establish a regular bathroom routine",
                "Don't ignore the urge to have a bowel movement",
                "Consider prune juice or dried prunes as natural remedies",
                "Ask your doctor about changing prenatal vitamins or adding a fiber supplement"
            ],
            "when_to_call": [
                "Constipation is severe or accompanied by abdominal pain",
                "You notice blood in your stool",
                "You haven't had a bowel movement for more than a week",
                "You experience alternating constipation and diarrhea",
                "You have severe hemorrhoids causing significant pain"
            ]
        },
        "insomnia": {
            "description": "Sleep problems during pregnancy can be caused by physical discomfort, hormonal changes, anxiety, and frequent urination.",
            "common_timing": "Common throughout pregnancy, especially in the third trimester.",
            "self_care": [
                "Create a consistent sleep schedule and bedtime routine",
                "Use pillows to support your back, abdomen, and between knees",
                "Avoid screen time before bed and create a dark, cool sleeping environment",
                "Practice relaxation techniques like deep breathing or meditation",
                "Reduce fluid intake before bedtime to minimize nighttime bathroom trips",
                "Exercise regularly, but not close to bedtime",
                "Consider a pregnancy massage or warm bath before bed"
            ],
            "when_to_call": [
                "Insomnia is severe and affecting your daily functioning",
                "You experience symptoms of depression or anxiety with insomnia",
                "You have restless legs syndrome symptoms that severely disturb sleep",
                "You experience frequent waking with heart palpitations or shortness of breath",
                "You snore loudly or seem to stop breathing during sleep (sleep apnea)"
            ]
        },
        "frequent urination": {
            "description": "Needing to urinate frequently is normal during pregnancy due to hormonal changes and increased pressure on the bladder from the growing uterus.",
            "common_timing": "Common in first trimester, improves in second, returns in third trimester.",
            "self_care": [
                "Continue drinking plenty of water despite the inconvenience",
                "Lean forward when urinating to help empty your bladder completely",
                "Avoid bladder irritants like caffeine and artificial sweeteners",
                "Practice pelvic floor (Kegel) exercises regularly",
                "Empty your bladder before going to bed and before exercise",
                "Wear panty liners if you experience minor leakage",
                "Don't reduce fluid intake to avoid urination (can cause dehydration)"
            ],
            "when_to_call": [
                "You experience burning or pain when urinating",
                "Your urine is cloudy, bloody, or has a strong odor",
                "You have fever, chills, or back pain with urinary symptoms",
                "You experience leaking or inability to hold urine",
                "You notice decreased urination despite normal fluid intake"
            ]
        },
        "breast tenderness": {
            "description": "Breast tenderness and sensitivity are common early pregnancy symptoms due to hormonal changes preparing breasts for lactation.",
            "common_timing": "Often one of the earliest symptoms, can continue throughout pregnancy.",
            "self_care": [
                "Wear a supportive, well-fitted maternity or sports bra",
                "Wear a soft bra during sleep if needed for comfort",
                "Use warm or cold compresses for relief",
                "Avoid harsh soaps or irritating lotions on breasts",
                "Wear loose-fitting, comfortable clothing",
                "Consider breast pads if nipples are sensitive to fabric friction",
                "Use gentle massage with safe moisturizers if skin feels stretched"
            ],
            "when_to_call": [
                "You notice a new lump that persists for more than a week",
                "You have redness, warmth or inflammation in breast tissue",
                "You experience discharge other than normal clear colostrum",
                "One breast becomes significantly more painful than the other",
                "You have fever along with breast pain"
            ]
        },
        "mood swings": {
            "description": "Emotional changes and mood swings during pregnancy are caused by hormonal fluctuations, physical discomfort, and preparation for major life changes.",
            "common_timing": "Can occur throughout pregnancy, often most pronounced in first and third trimesters.",
            "self_care": [
                "Acknowledge that mood changes are normal during pregnancy",
                "Get adequate rest and prioritize sleep",
                "Engage in gentle exercise like walking or prenatal yoga",
                "Practice stress reduction techniques like meditation or deep breathing",
                "Maintain open communication with your partner and support system",
                "Join a pregnancy support group to share experiences",
                "Maintain a healthy diet with regular meals to stabilize mood"
            ],
            "when_to_call": [
                "You have persistent feelings of sadness or hopelessness",
                "You lose interest in activities you normally enjoy",
                "You have thoughts of harming yourself or others",
                "Anxiety is interfering with daily activities or sleep",
                "Mood changes are severe or feel unmanageable"
            ]
        },
        "cravings": {
            "description": "Food cravings and aversions are common during pregnancy and may be related to hormonal changes, nutritional needs, or sensory changes.",
            "common_timing": "Often begin in first trimester and can continue throughout pregnancy.",
            "self_care": [
                "Indulge cravings in moderation, especially if they're for healthy foods",
                "Find healthier substitutes for unhealthy cravings when possible",
                "Keep healthy snacks readily available",
                "Stay well-hydrated and don't confuse thirst with hunger",
                "Eat regular meals to avoid extreme hunger that intensifies cravings",
                "Be aware of non-food cravings (pica) and discuss with your doctor",
                "Try small portions of foods you're averse to or find substitutions"
            ],
            "when_to_call": [
                "You have cravings for non-food items like clay, dirt, or laundry starch (pica)",
                "Food aversions are so severe you cannot maintain a balanced diet",
                "You're losing weight due to food aversions",
                "Your cravings lead to excessive weight gain",
                "You have diabetes and cravings affect blood sugar management"
            ]
        },
        "stretch marks": {
            "description": "Stretch marks are pink, red, or purple streaks that appear as skin stretches during pregnancy, usually on abdomen, breasts, hips, and thighs.",
            "common_timing": "Usually appear in second and third trimesters as skin stretches.",
            "self_care": [
                "Keep skin moisturized with pregnancy-safe lotions or oils",
                "Stay hydrated to maintain skin elasticity",
                "Gain weight gradually within recommended guidelines",
                "Eat a balanced diet rich in vitamins C, D, E, zinc, and protein",
                "Exercise regularly to improve circulation and skin tone",
                "Consider gentle massage when applying moisturizers",
                "Accept that genetics play a large role in stretch mark development"
            ],
            "when_to_call": [
                "Stretch marks become extremely itchy or painful",
                "You notice significant swelling along with stretch marks",
                "Skin appears infected, inflamed, or has unusual discharge",
                "You develop a widespread rash with your stretch marks",
                "Stretch marks appear suddenly along with other symptoms"
            ]
        },
        "shortness of breath": {
            "description": "Breathlessness during pregnancy occurs due to increased oxygen demand and pressure from the growing uterus on the diaphragm.",
            "common_timing": "Mild in early pregnancy, often more pronounced in third trimester.",
            "self_care": [
                "Practice good posture to give lungs maximum space",
                "Sleep propped up on pillows if breathlessness occurs at night",
                "Take breaks and rest when needed during activities",
                "Practice deep breathing exercises regularly",
                "Avoid overexertion while still maintaining gentle activity",
                "Wear loose, comfortable clothing that doesn't restrict your chest",
                "Stay cool as overheating can worsen breathlessness"
            ],
            "when_to_call": [
                "Shortness of breath is sudden, severe, or getting progressively worse",
                "You experience chest pain with breathlessness",
                "You have a cough or wheezing with difficulty breathing",
                "You notice blue lips or fingers",
                "You feel like you can't catch your breath even at rest"
            ]
        },
        "leg cramps": {
            "description": "Muscle cramps, especially in the calves, are common in pregnancy due to fatigue, circulation changes, and possibly calcium/magnesium imbalances.",
            "common_timing": "Most common in second and third trimesters, often occurring at night.",
            "self_care": [
                "Stretch your calf muscles regularly, especially before bed",
                "Stay physically active with walking or swimming",
                "Apply heat to tight muscles and cold to painful areas",
                "Stay hydrated throughout the day",
                "Consider calcium and magnesium-rich foods in your diet",
                "Avoid standing or sitting in one position for too long",
                "Gently massage cramping muscles"
            ],
            "when_to_call": [
                "One leg becomes swollen, red, or warm to touch",
                "You have persistent pain in one leg, not just during cramps",
                "Cramping is severe and not relieved by self-care measures",
                "You notice reduced movement or changes in the baby after severe cramps",
                "Cramps are accompanied by significant swelling or headaches"
            ]
        },
        "dizziness": {
            "description": "Dizziness or lightheadedness during pregnancy is usually caused by hormonal changes, low blood sugar, or pressure on blood vessels from the uterus.",
            "common_timing": "Can occur throughout pregnancy but common in the first and third trimesters.",
            "self_care": [
                "Change positions slowly, especially when getting up from lying down",
                "Avoid standing for long periods or in hot, crowded areas",
                "Eat regular, small meals to maintain blood sugar levels",
                "Stay well hydrated throughout the day",
                "Lie on your left side when resting to improve circulation",
                "Wear loose, comfortable clothing",
                "Avoid triggers like hot showers or overheated rooms"
            ],
            "when_to_call": [
                "You experience fainting or loss of consciousness",
                "Dizziness is severe or persistent",
                "You have visual disturbances, headache, or ringing in ears with dizziness",
                "You notice heart palpitations or chest pain with dizziness",
                "Dizziness occurs with vaginal bleeding or abdominal pain"
            ]
        },
        "bleeding gums": {
            "description": "Bleeding gums during pregnancy are common due to hormonal changes that make gums more sensitive to plaque and bacteria.",
            "common_timing": "Can occur throughout pregnancy, starting as early as the first trimester.",
            "self_care": [
                "Brush gently with a soft-bristled toothbrush twice daily",
                "Floss carefully once a day",
                "Use an antimicrobial or saltwater rinse",
                "Continue regular dental check-ups during pregnancy",
                "Maintain a healthy diet rich in vitamin C and calcium",
                "Avoid sugary foods and drinks that contribute to plaque",
                "Inform your dentist that you're pregnant before any procedures"
            ],
            "when_to_call": [
                "Gums are severely swollen, very painful, or bleed excessively",
                "You develop sores or white patches in your mouth",
                "You have persistent bad breath that doesn't improve with brushing",
                "You experience loose teeth or changes in how your teeth fit together",
                "You have facial swelling or fever along with dental symptoms"
            ]
        }
    }
    return details


def show_search_content():
 symptoms_df = load_symptoms_data()
 symptom_details = load_symptom_details()
# Header section
 st.markdown('<h1 class="title">Pregnancy Symptoms Guide</h1>', unsafe_allow_html=True)
 st.markdown('<h2 class="subtitle">Get advice for common pregnancy symptoms</h2>', unsafe_allow_html=True)

# Search section
 st.markdown("### Search for symptoms")
 search_query = st.text_input("Enter your symptoms", placeholder="e.g., nausea, vomiting and leg pain")
 st.markdown('<p class="example-text">You can enter multiple symptoms separated by commas or "and" (e.g., "vomiting and leg pain")</p>', unsafe_allow_html=True)

# Display results based on search
 if search_query:
    # Clean and tokenize the search query
    # Split by common separators (comma, "and", "&")
    search_query_clean = search_query.lower().replace(" and ", ",").replace("&", ",")
    search_terms = [term.strip().lower() for term in search_query_clean.split(',')]
    
    # Find matching symptoms
    matching_primary_terms = set()
    matched_terms = []
    
    for term in search_terms:
        found_match = False
        # Check for exact or partial matches
        for idx, row in symptoms_df.iterrows():
            if term in row['symptom']:
                matching_primary_terms.add(row['primary_term'])
                matched_terms.append(term)
                found_match = True
                break
        
        # If no direct match, try to find the most similar symptom
        if not found_match and len(term) > 3:  # Only for terms with more than 3 characters
            for symptom in symptoms_df['symptom']:
                # Check if the search term is at least partially contained in any symptom
                if any(term in s for s in symptom.split()):
                    primary = symptoms_df[symptoms_df['symptom'] == symptom]['primary_term'].values[0]
                    matching_primary_terms.add(primary)
                    matched_terms.append(term)
                    found_match = True
                    break
    
    # Display results
    if matching_primary_terms:
        st.markdown(f"### Guidance for: {', '.join(matched_terms)}")
        
        for symptom in matching_primary_terms:
            if symptom in symptom_details:
                details = symptom_details[symptom]
                
                # Create expandable section for each symptom
                with st.expander(f"**{symptom.title()}**", expanded=True):
                    st.markdown(f"**Description:**  \n{details['description']}")
                    st.markdown(f"**When it occurs:**  \n{details['common_timing']}")
                    
                    st.markdown("**Self-care measures:**")
                    for item in details['self_care']:
                        st.markdown(f"- {item}")
                    
                    st.markdown("**When to call your healthcare provider:**")
                    for item in details['when_to_call']:
                        st.markdown(f"- {item}")
    else:
        st.info("No matching symptoms found. Try different terms or check your spelling. You can enter multiple symptoms like 'nausea and headache' or 'vomiting, leg pain'.")

# Common symptoms section
 with st.expander("Common Pregnancy Symptoms", expanded=False):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**First Trimester**")
        st.markdown("- Nausea/Morning sickness")
        st.markdown("- Fatigue")
        st.markdown("- Frequent urination")
        st.markdown("- Breast tenderness")
        st.markdown("- Food cravings/aversions")
    
    with col2:
        st.markdown("**Second Trimester**")
        st.markdown("- Back pain")
        st.markdown("- Stretch marks")
        st.markdown("- Heartburn")
        st.markdown("- Leg cramps")
        st.markdown("- Swelling (edema)")
    
    with col3:
        st.markdown("**Third Trimester**")
        st.markdown("- Shortness of breath")
        st.markdown("- Insomnia")
        st.markdown("- Increased swelling")
        st.markdown("- Frequent urination")
        st.markdown("- Braxton Hicks contractions")

# Important disclaimer
 st.markdown('<div class="disclaimer">DISCLAIMER: This tool provides general information and is not a substitute for professional medical advice. Always consult with your healthcare provider about symptoms during pregnancy. If you experience severe symptoms or emergencies, contact your healthcare provider immediately or seek emergency care.</div>', unsafe_allow_html=True)

