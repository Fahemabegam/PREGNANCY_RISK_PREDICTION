import streamlit as st
import base64
from io import BytesIO

def show_excercise_content():
# Custom CSS for pastel green theme with boxed content
 st.markdown("""
<style>
    body {
        background-color: #e8f5e9;
    }
    .stApp {
        background-color: #e8f5e9;
    }
    .main-card {
        background-color: #c8e6c9;
        border-radius: 10px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-left: 5px solid #2e7d32;
    }
    .content-box {
        background-color: #f1f8e9;
        border-radius: 8px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .exercise-box {
        background-color: #f1f8e9;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        border-left: 3px solid #81c784;
    }
    .read-more-content {
        display: none;
    }
    .read-more-content.show {
        display: block;
    }
    h1, h2, h3, h4 {
        color: #2e7d32;
    }
    .trimester-header {
        background-color: #a5d6a7;
        padding: 10px 15px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .safety-tips {
        background-color: #e8f5e9;
        border: 1px dashed #2e7d32;
        border-radius: 8px;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Page title
 st.title(" Exercise Guide")
 st.markdown("""
<div class="content-box">
    <strong>Stay active and healthy during your pregnancy with these trimester-specific exercise recommendations.</strong>
</div>
""", unsafe_allow_html=True)

# Convert your image to base64 (run this once to get the string)
 def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
# Trimester selection
 trimester = st.radio("Select Your Trimester:", 
                    ["First Trimester", "Second Trimester", "Third Trimester"],
                    horizontal=True)

# Exercise data for each trimester
 exercise_data = {
    "First Trimester": {
        "image": f"data:image/webp;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/frist_trimester.webp')}",
        "summary": "During the first trimester, focus on maintaining your regular exercise routine with some modifications. Low-impact activities are ideal.",
        "recommendations": [
            "<h3>Walking</h3>Walking is what our bodies are made for and it makes for great pregnancy exercise. An easy stroll gets you moving, and you can build upper body strength by swinging your arms. Get your heart pumping by picking up the pace.",
            "<h3>Swimming and Water aerobics</h3> The pool is your friend during pregnancy. The water is soothing, the exercise is low-impact, and you won’t fall over. Water exercise expert Sara Haley has a helpful series of prenatal exercises that focus on building core strength.\n\n If you’re already doing water exercise, there’s no need to change your routine. As in all exercise, avoid twisting your middle too much, and pay attention to your energy limits. If you get tired, it’s not time to push yourself — it’s time to get out of the pool. If you’re starting water exercise during pregnancy, ask a swim coach or trainer at your pool about safe routines.",
            "<h3>Prenatal yoga</h3> Many moms-to-be love yoga for its ability to tone muscle and improve flexibility without placing stress on tender joints. Skip the Bikram and hot yoga classes – the pregnant body cannot disperse heat as effectively – and for peak heart health, mix in a light jog or a swimming session once or twice a week.",
            
        ],
        "benefits": [
            "<strong>Reduced Back Pain and Other Discomforts</strong>: Exercise can help alleviate common pregnancy symptoms like back pain, fatigue, and constipation. ",
            "<strong>Improved Mood and Reduced Stress</strong>: Physical activity can boost mood and reduce stress levels, which are common during pregnancy. ",
            "<strong>Healthy Weight Gain</strong>: Exercise can help manage weight gain during pregnancy, ensuring a healthy weight gain for both the mother and the baby. ",
            "<strong>Reduced Risk of Certain Conditions</strong>: Some studies suggest that exercise may lower the risk of certain conditions like low birth weight and macrosomia",
            "<strong>Improved Sleep</strong>: Regular exercise can help improve sleep quality, which is often disrupted during pregnancy. ",
            "<strong>Potential Reduction in Pregnancy Complications</strong>: Some studies suggest that exercise may decrease the risk of gestational diabetes, preeclampsia, and cesarean birth",
        ],
        "exercises": [
            {
                "name": "Pilates",
                "description": "Pilates can be a safe and beneficial form of exercise during pregnancy, especially when modified and guided by a prenatal-trained instructor. It focuses on strengthening core muscles, improving posture, and increasing flexibility, all of which are helpful for expectant mothers. Pilates can also help prepare for labor and delivery by strengthening the pelvic floor and improving breathing techniques.<h5>How to do? </h5><p>Your centre of gravity will change during pregnancy so you are more likely to lose your balance. Move slowly and use support, such as a wall or a chair.</p>",
                "image": f"data:image/jpg;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/pilates.jpg')}"
            },
            {
                "name": "Pelvic floor exercises",
                "description": "Pelvic floor exercises, often called Kegels, are beneficial during pregnancy to strengthen these muscles, which support the pelvic organs and bladder. These exercises can improve bladder control, reduce the risk of urinary incontinence, and help prepare the body for childbirth. <h5>How to do? </h5><li><strong>Identify the muscles:</strong> Imagine you are trying to stop urination or prevent passing gas. The muscles you tighten are your pelvic floor muscles. </li><li><strong>Squeeze and lift:</strong>Tighten and lift your pelvic floor muscles upwards and inwards, as if you are trying to pull the muscles up and in towards your body. </li><li><strong>Hold and release:</strong> Hold the contraction for a few seconds, then slowly release the muscles. </li><li><strong>Repeat:</strong> Try to repeat this process 10-15 times, several times a day.</li> ",
                "image": f"data:image/jpeg;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/pelvic.jpeg')}"
            },
            {
                "name": "Kneeling push-ups",
                "description": "Kneeling push-ups can be a safe and effective exercise during pregnancy, particularly when performed with proper form and modifications. This exercise strengthens upper body and core muscles, which can be beneficial throughout pregnancy and for preparing for childbirth. <h5>How to do?</h5><li><strong> Start in a modified push-up position:</strong> Begin on your hands and knees, with your knees directly under your hips and your hands directly under your shoulders</li><li><strong>Engage your core:</strong>2. Engage your core:Pull your belly button in and engage your pelvic floor muscles to stabilize your spine. </li><li><strong>Lower your chest:</strong>Slowly lower your chest towards the floor, bending your elbows while keeping your back straight and core engaged. </li><li><strong>Push back up:</strong>Exhale as you push back up to the starting position, using your arms and core to return to the upright position. </li><li><strong> Repeat:</strong>Perform 6-10 repetitions, gradually working up to 20-24 reps as you get stronger. </li>",
                "image": f"data:image/jpeg;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/knee.jpeg')}"
            }
        ]
    },
    "Second Trimester": {
        "image": f"data:image/jpg;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/second.jpg')}",
        "summary": "The second trimester is often the most comfortable time to exercise. Focus on posture and core strength as your belly grows.",
        "recommendations": [
            "<h3>Squat And Rotate</h3> Squats are among the most popular and effective exercises for lower body strength. There are many variations of squats that can be done with or without equipment.\nWhen you’re pregnant, your lower body has more weight to support. Strengthening your lower body with squats can help reduce pregnancy-related discomfort and fatigue. Squats may even offer some benefits during labor and throughout the postpartum period.",
            "<h3>Seated Forward Bend</h3> Seated forward bends, like Paschimottanasana, are generally safe during pregnancy with some modifications and precautions. However, it's important to be mindful of your body and listen to any discomfort. Deep twists or positions that heavily compress the abdomen should be avoided, particularly in later trimesters, according to Life Cell. ",
            "<h3>Bee Breath</h3> Bee breath, also known as Bhramari Pranayama, is a calming breathing exercise safe to practice during the second trimester of pregnancy. It involves inhaling deeply through both nostrils and exhaling with a soft, buzzing sound, like a bee, while keeping the mouth closed. This technique can help reduce stress and anxiety, and promote relaxation during pregnancy. ",
        ],
        "benefits": [
            "<strong>Improved Physical Health</strong>: Exercise can help manage weight gain, prevent gestational diabetes, and promote healthy fetal growth. ",
            "<strong>Enhanced Mental Well-being</strong>: It can improve mood, reduce stress, and boost energy levels",
            "<strong>Relief of Common Pregnancy Discomforts</strong>: Exercise can ease back pain, constipation, and swelling in the legs and ankles",
            "<strong>Preparation for Labor and Delivery</strong>: Certain exercises, like pelvic floor exercises, can strengthen the muscles needed for labor and delivery.",
            "<strong>Reduced Risk of Pregnancy Complications</strong>: Exercise may reduce the risk of gestational diabetes, preeclampsia, and the need for a Cesarean birth.",
        ],
        "exercises": [
            {
                "name": "Cat-Cow Stretch",
                "description": "The cat-cow stretch, also known as Marjaryasana-Bitilasana, is a safe and beneficial exercise during pregnancy for improving back flexibility, relieving back pain, and promoting overall well-being. It involves gently alternating between arching and rounding the back while on all fours. This movement can help mobilize the spine, stretch back muscles, and improve circulation. Relieves back tension and improves spinal flexibility.<h5>How to do?</h5><li>Kneel on the floor with your hands shoulder-width apart and your knees under your hips.</li> <li>Arch your back, lift your head and tailbone towards the ceiling, and drop your belly down towards the floor.</li><li>Round your spine, tuck your chin towards your chest, and draw your belly button towards your spine.</li><li>Continue to alternate between cow and cat poses, breathing deeply with each movement.</li>",
                "image": f"data:image/jpg;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/cat_cow.jpg')}"
            },
            {
                "name": "Squats",
                "description": "squats are generally safe and beneficial for most pregnant women during the second trimester. It Strengthens legs and prepares for labor. And it can help maintain strength in the lower body, improve posture, and potentially assist with labor and delivery.<h5>How to do?</h5><li>Stand with feet shoulder-width apart.</li><li>If you don't have weights or a bar, hold your arms straight out in front of your body for balance.</li><li>Lower yourself into a squat position.</li><li>Return to the starting position, squeezing your glutes on the way up.</li><li>Perform 3 sets of 10 to 15 repetitions.",
                "how_to": "Stand with feet shoulder-width apart, lower as if sitting in a chair, keep knees behind toes",
                "image": f"data:image/avif;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/squats.avif')}"
            },
             {
                "name": "Low-impact cardio",
                "description": "Low-impact cardio during pregnancy refers to exercise that puts less strain on joints and muscles compared to high-impact activities. Examples include walking, swimming, and stationary cycling, all of which are generally considered safe and beneficial for pregnant women. <h5>How to do?</h5><li>A brisk walk provides a good cardiovascular workout and is accessible to most pregnant women. </li><li>Riding a stationary bike offers a controlled and safe workout without the risk of falls associated with regular cycling. </li><li>Engaging in water exercises, like aqua aerobics, provides a low-impact workout with the benefits of water buoyancy and resistance. </li>",
                "image": f"data:image/avif;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/low.avif')}"
            },
        ]
    },
    "Third Trimester": {
        "image": f"data:image/jpg;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/third.jpg')}",
        "summary": "In the third trimester, focus on gentle movements and preparation for labor. Listen to your body and modify as needed.",
        "recommendations": [
            "<h3>Lying down</h3> Lying down exercises can be beneficial during pregnancy, offering a way to strengthen muscles and relieve pain while avoiding high-impact activities. Some safe exercises include pelvic tilts, side-lying leg raises, and clamshells, all of which can help strengthen the core and pelvic floor. It's important to consult with a doctor or healthcare provider before starting any new exercise routine during pregnancy. ",
            "<h3>Lunges</h3> Lunges, when performed correctly and with modifications, can be a safe and beneficial exercise during pregnancy, especially as they help strengthen lower body muscles and improve balance. However, it's crucial to listen to your body and adjust the exercise as needed throughout your pregnancy",
            "<h3>Arm Lifts</h3> Many arm lifts exercises are safe and beneficial during pregnancy, helping to maintain muscle strength and tone. Some examples include bicep curls, tricep extensions, shoulder presses, and rows, which can be performed with weights or resistance bands. It's crucial to consult with a healthcare provider before starting any new exercise program during pregnancy and to listen to your body, stopping if you experience any pain or discomfort. ",
        ],
        "benefits": [
            "<strong>Reduces back pain :</strong> The expanding uterus can put pressure on the back, causing discomfort. Exercise, especially activities like prenatal yoga and Pilates, can strengthen muscles and improve posture, alleviating back pain",
            "<strong>Improves mood and reduces stress :</strong> Exercise releases endorphins, which have mood-boosting effects and can help manage stress and anxiety, common during pregnancy. ",
            "<strong>Reduce the risk of gestational diabetes and preeclampsia :</strong> These conditions can develop during pregnancy and may be linked to a sedentary lifestyle. Exercise can help improve insulin sensitivity and blood pressure, potentially reducing the risk of these complications. ",
            "<strong>Ease constipation: </strong> Pregnancy can cause hormonal changes that lead to constipation. Exercise can stimulate bowel movements and help alleviate this discomfort. ",
            "<strong>Prepares the body for labor and delivery:</strong> Exercise can strengthen muscles and improve cardiovascular fitness, which can be beneficial during labor and delivery",
            "<strong>Lead to a shorter labor: </strong> Studies suggest that physically fit mothers may experience a shorter labor and fewer medical interventions. ",
        ],
        
        "exercises": [
            {
                "name": "Pelvic Circles on Birth Ball",
                "description": "This exercise helps to increase flexibility around your hips and pelvis. Keep the movement small to start with and increase by small amounts as you feel comfortable.Promotes pelvic mobility and can help with back pain<h5>How to do?</h5><li>Sit with your feet flat on the floor</li><li> Ensuring your knees are lower than your hips</li><li> And gently move your hips in a circular motion</li>",
                "image": f"data:image/jpg;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/ball.jpg')}"
            },
            {
                "name": "Side-Lying Leg Lifts",
                "description": "These side-lying leg lifts are great because they are great in helping to minimize (and even prevent) back pain + hip pain. Even better news is that this movement can be done throughout your ENTIRE pregnancy as well as postpartum.<h5>How to do?</h5><li>Lie on your left side with your body in a straight line (shoulders, hips, ankles). You can use a pillow under your side for extra support.</li><li>Keep your bottom leg bent and your top leg straight. You can also place a pillow or bolster under your top leg for added support. </li><li>Keeping your core engaged and your hips stacked, gently lift the top leg upward towards the ceiling, as high as you can without causing back pain or feeling your hips roll backward. </li><li>Lower the leg slowly and with control back down to the starting position. </li><li> Perform 10-15 repetitions on one side, then switch to the other side. </li> ",
                "how_to": "Lie on your side, keep leg straight and lift gently",
                "image": f"data:image/webp;base64,{image_to_base64('C:/Pregnancy_risk_Prediction-master/images/lying.webp')}"
            }
        ]
    }
}

# Display selected trimester content
 data = exercise_data[trimester]

# Main content card
 st.markdown(f"""
<div class="main-card">
    <div class="trimester-header">
        <h2>{trimester} Exercises</h2>
    </div>
    
    
""", unsafe_allow_html=True)

# Create columns for image and recommendations
 col1, col2 = st.columns([1, 2])

 with col1:
    st.image(data["image"], caption=f"Exercise during {trimester.lower()}", width=400)

 with col2:
    st.markdown(f"""
    <div class="content-box">
        <h2>Recommendations</h2>
        <ul>
            {''.join(f'<li>{item}</li>' for item in data['recommendations'])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Continue main card content
 st.markdown(f"""
    <div class="content-box">
        <h3>Benefits</h3>
        <ul>
            {''.join(f'<li>{item}</li>' for item in data['benefits'])}
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Exercises section
 st.markdown(f"""
<div class="main-card">
    <div class="trimester-header">
        <h2>Specific Exercises</h2>
    </div>
""", unsafe_allow_html=True)

 for exercise in data.get("exercises", []):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(exercise["image"], width=500,)
    with col2:
        st.markdown(f"""
        <div class="exercise-box">
            <h4>{exercise['name']}</h4>
            <p> {exercise['description']}</p>
           
        </div>
        """, unsafe_allow_html=True)

 st.markdown("</div>", unsafe_allow_html=True)  # Close main-card div

# Only show safety tips and other questions sections for the Third Trimester
 if trimester == "Third Trimester":
    # General safety tips
    st.markdown("""
    <div class="main-card">
        <div class="trimester-header">
            <h2>Exercising Safely</h2>
        </div>
        <div class="safety-tips">
            <ul>
                <h3>What are some safe exercises I can do during pregnancy ? </h3>
                <h6>Experts agree these exercises are safest for pregnant women :</h6>
                <li>Walking—Brisk walking gives a total body workout and is easy on the joints and muscles.</li>
                <li>Swimming and water workouts—Water workouts use many of the body's muscles. The water supports your weight so you avoid injury and muscle strain.</li>
                <li>Stationary bicycling—Because your growing belly can affect your balance and make you more prone to falls, riding a standard bicycle during pregnancy can be risky. Cycling on a stationary bike is a better choice.</li>
                <li>Modified yoga and modified Pilates—Yoga reduces stress, improves flexibility, and encourages stretching and focused breathing. There are prenatal yoga and Pilates classes designed for pregnant women. These classes often teach modified poses that accommodate a pregnant woman's shifting balance. You should avoid poses that require you to be still or lie on your back for long periods.</li><br>
                <p>If you are an experienced runner, jogger, or racquet-sports player, you may be able to keep doing these activities during pregnancy. Discuss these activities with your ob-gyn.</p>
                <br>
                <h3>What exercises should I avoid during pregnancy?</h3>
                <h6>While pregnant, avoid activities that put you at increased risk of injury, such as the following :</h6>
                <li>Contact sports and sports that put you at risk of getting hit in the abdomen, including ice hockey, boxing, soccer, and basketball.</li>
                <li>Skydiving</li>
                <li>Activities that may result in a fall, such as downhill snow skiing, water skiing, surfing, off-road cycling, gymnastics, and horseback riding</li>
                <li>"Hot yoga" or "hot Pilates," which may cause you to become overheated</li>
                <li>Activities performed above 6,000 feet (if you do not already live at a high altitude)</li>
                <br>
                <h3>How much exercise do you need during pregnancy?</h3>
                <li>Healthy pregnant women need at least 2½ hours of moderate-intensity aerobic activity each week. Aerobic activities make you breathe faster and deeply and make your heart beat faster. Moderate-intensity means you’re active enough to sweat and increase your heart rate. Taking a brisk walk is an example of moderate-intensity aerobic activity. If you can’t talk normally during an activity, you may be working too hard.</li>
                <li>You don’t have to do all 2½ hours at once. Instead, break it up through the week. For example, do 30 minutes of exercise on most or all days. If this sounds like a lot, split up the 30 minutes by doing something active for 10 minutes 3 times each day.</li>
                <br>
                <h3>Why is physical activity during pregnancy good for you?</h3>
                <h6>For healthy pregnant women, regular exercise can:</h6>
                <li>Keep your mind and body healthy. Physical activity can help you feel good and give you extra energy. It also makes your heart, lungs and blood vessels strong and helps you stay fit.</li>
                <li>Help you gain the right amount of weight during pregnancy</li>
                <li>Ease some common discomforts of pregnancy, such as constipation, back pain and swelling in your legs, ankles and feet</li>
                <li>Help reduce your risk of pregnancy complications, like gestational diabetes and preeclampsia. Gestational diabetes is a kind of diabetes that can happen during pregnancy. It happens when your body has too much sugar (called glucose) in the blood. Preeclampsia is a type of high blood pressure some women get after the 20th week of pregnancy or after giving birth. These conditions can increase your risk of having complications during pregnancy, like preterm birth (birth before 37 weeks of pregnancy).</li>
                <li>Prepare your body for labor and birth. Activities such as prenatal yoga and Pilates can help you practice breathing, meditation and other calming methods that may help you manage labor pain. Regular exercise can help give you energy and strength to get through labor. </li>
                <br>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Other Questions section
    st.markdown("""
    <div class="main-card">
        <div class="trimester-header">
            <h2>More Caution</h2>
        </div>
        <div class="safety-tips">
            <ul>
                <h3>What kinds of activities aren’t safe during pregnancy?</h3>
                <h6>Be careful and check with your provider when choosing your activities. During pregnancy, don’t do:</h6>
                <li>Any activity that has a lot of jerky, bouncing movements that may cause you to fall, like horseback riding, downhill skiing, off-road cycling, gymnastics or skating.</li>
                <li>Any sport in which you can get hit in the belly, like ice hockey, boxing, soccer or basketball.</li>
                <li>Any exercise that makes you lie flat on your back (after the third month of pregnancy), like sit-ups. When you lie on your back, your uterus puts pressure on a vein that brings blood to your heart. Lying on your back can cause your blood pressure to drop and limit the flow of blood to your baby.</li>
                <li>Activities that can cause you to hit water with great force, like water skiing, surfing or diving.</li>
                <li>Skydiving or scuba diving. Scuba diving can lead to decompression sickness. This is when dangerous gas bubbles form in your baby's body.</li>
                <br>
                <h3>When should you stop exercising? What are the warning signs you should watch for when exercising?</h3>
                <h6>When you’re being physically active, drink lots of water and pay attention to your body and how you feel. Stop your activity and call your provider if you have any of these signs or symptoms:</h6>
                <li>Bleeding from the vagina or fluid leaking from the vagina</li>
                <li>Muscle weakness, trouble walking or pain or swelling in your lower legs. Pain or swelling in your lower legs may be signs of deep vein thrombosis (also called DVT). DVT happens when a blood clot forms in a vein deep in the body, usually in the lower leg or thigh. If untreated, it can cause serious health problems and even death.</li>
                <li>Regular, painful contractions. A contraction is when the muscles of your uterus get tight and then relax. Contractions help push your baby out of your uterus.</li>
                <li>Your baby stops moving. This may be a symptom of stillbirth (when a baby dies in the womb after 20 weeks of pregnancy.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    # Other Questions section
    st.markdown("""
    <div class="main-card">
        <div class="trimester-header">
            <h2>Call Your Doctor</h2>
        </div>
        <div class="safety-tips">
            <ul>
            <h4>Stop exercising right away and call your doctor or midwife if you have any of the symptoms below:</h4>
            <p><strong>Warning signs of preterm labor: </strong> It may be possible to avoid preterm labor if you and your doctor or midwife act quickly. Be on the lookout for:</p>
            <li>Contractions, especially if they continue after you rest and drink water</li>
            <li>Vaginal bleeding</li>
            <li>Unusual pain in your belly</li>
            <li>Fluid leaking or gushing from your vagina</li>
            <p><strong>Trouble breathing: </strong> Breathing conditions, such as asthma, can be more serious when you’re pregnant. If you have asthma, always carry your inhaler. Phone your doctor or midwife if you have:</p>
            <li>Lightheadedness or feeling like you might faint</li>
            <li>Chest pain,Pounding heart</li>
            <li>Rapid heartbeat</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    #disclaimer
    st.markdown("""
    <div class="main-card">
        <div class="trimester-header">
            <h2>Disclaimer</h2>
        </div>
        <div class="safety-tips">
            <ul>
            <p>This application provides pregnancy risk level prediction and guidance for informational purposes only and should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult with a healthcare professional for personalized guidance regarding your pregnancy. This application's predictions are based on current data and may not be entirely accurate, so rely on professional medical advice for making critical decisions about your health and pregnancy. </p>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)