import streamlit as st
import random

# ------------------ PAGE SETUP ------------------
st.set_page_config(page_title="Medisia", page_icon="💖", layout="wide")

# ------------------ BACKGROUND FUNCTION ------------------
def set_bg(gradient):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(to right, {gradient[0]}, {gradient[1]});
            color: black;
        }}
        /* Center-align Next button properly */
        div.stButton > button {{
            display: block;
            margin: 0 auto;
            font-size: 18px;
            border-radius: 10px;
            padding: 0.4em 1.2em;
            background-color: white;
            color: black;
            border: 2px solid #ddd;
            transition: all 0.3s ease;
        }}
        div.stButton > button:hover {{
            background-color: #f4b8c1;
            color: white;
            border-color: #f4b8c1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ------------------ INITIAL SESSION STATE ------------------
if "page" not in st.session_state:
    st.session_state.page = 0
if "name" not in st.session_state:
    st.session_state.name = ""
if "medicines" not in st.session_state:
    st.session_state.medicines = []
if "new_medicine" not in st.session_state:
    st.session_state.new_medicine = ""
if "taken" not in st.session_state:
    st.session_state.taken = {}

# ------------------ PAGE NAVIGATION ------------------
def next_page():
    st.session_state.page += 1
def prev_page():
    st.session_state.page -= 1

# ------------------ GRADIENTS ------------------
gradients = [
    ("#c4f0e8", "#fcd6e7"),  # Welcome
    ("#f6d365", "#fda085"),  # Add Medicines
    ("#a8edea", "#fed6e3"),  # Tracker
    ("#d4fc79", "#96e6a1"),  # Wellness
    ("#84fab0", "#8fd3f4"),  # Quotes
    ("#fbc2eb", "#a6c1ee"),  # Summary
    ("#c9e8dd", "#fbd3e9")   # Thank You
]

# ------------------ PAGE 0: WELCOME ------------------
if st.session_state.page == 0:
    set_bg(gradients[0])
    st.markdown("<h1 style='text-align:center;'>🌸 Welcome to Medisia 🌸</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Your daily dose of health, care, and calmness 💖</p>", unsafe_allow_html=True)

    st.session_state.name = st.text_input("Enter your name:")

    # Centered Next Button (fixed alignment)
    st.markdown("<div style='text-align:center; margin-top:20px;'>", unsafe_allow_html=True)
    if st.button("Next ➡️"):
        if st.session_state.name.strip() == "":
            st.warning("Please enter your name before continuing 💬")
        else:
            next_page()
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ PAGE 1: ADD MEDICINES ------------------
elif st.session_state.page == 1:
    set_bg(gradients[1])
    st.header(f"💊 Hi {st.session_state.name}, add your medicines below:")

    new_med = st.text_input("Medicine name:", value=st.session_state.new_medicine, key="med_input")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("➕ Add Medicine", key="add_med"):
            med = new_med.strip()
            if med:
                if med not in st.session_state.medicines:
                    st.session_state.medicines.append(med)
                    st.session_state.taken[med] = None
                    st.session_state.new_medicine = ""
                    st.success(f"✅ {med} added successfully!")
                else:
                    st.warning("⚠️ This medicine is already added.")
            else:
                st.warning("Please enter a valid medicine name!")

    with col2:
        if st.button("⬅️ Back", key="add_back"):
            prev_page()
    with col3:
        if st.button("Next ➡️", key="add_next"):
            next_page()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("➕ Add More Medicines"):
        st.info("You can type and add more medicines above 💊")

    if st.session_state.medicines:
        st.subheader("💖 Your Medicine List:")
        for med in st.session_state.medicines:
            st.markdown(f"- {med}")

# ------------------ PAGE 2: MEDICINE CHECK ------------------
elif st.session_state.page == 2:
    set_bg(gradients[2])
    st.header("🩺 Medicine Tracker")
    st.write("Mark whether you've taken your medicines today:")

    if not st.session_state.medicines:
        st.warning("No medicines added yet! Please go back and add them.")
    else:
        for med in st.session_state.medicines:
            choice = st.radio(
                f"Have you taken **{med}**?",
                ["Yes ✅", "No ❌"],
                index=0 if st.session_state.taken.get(med) == "Yes ✅" else 1 if st.session_state.taken.get(med) == "No ❌" else 1,
                key=f"radio_{med}"
            )
            st.session_state.taken[med] = choice

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("⬅️ Back"):
            prev_page()
    with col3:
        if st.button("Next ➡️"):
            next_page()

# ------------------ PAGE 3: WELLNESS PAGE ------------------
elif st.session_state.page == 3:
    set_bg(gradients[3])
    st.header("🌿 Wellness Reminder 🌿")

    wellness_tips = [
        "💧 Stay hydrated – drink at least 8 glasses of water today.",
        "🚶‍♀️ Take a short walk and stretch your body.",
        "🧘 Breathe deeply – inhale calmness, exhale stress.",
        "🍎 Eat something healthy for your body and mind.",
        "😴 Take short breaks and rest your eyes from screens."
    ]
    st.subheader("Here are your wellness reminders:")
    for tip in wellness_tips:
        st.markdown(f"- {tip}")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Back"):
            prev_page()
    with col2:
        if st.button("Next ➡️"):
            next_page()

# ------------------ PAGE 4: MOTIVATIONAL QUOTES ------------------
elif st.session_state.page == 4:
    set_bg(gradients[4])
    st.header("💫 Motivational Quotes 💫")

    # Darker text for better readability
    st.markdown("""
        <style>
        blockquote {
            color: #222 !important;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    quotes = [
        "🌈 'Every day may not be good, but there's something good in every day.'",
        "💪 'Small steps every day lead to big changes.'",
        "🌸 'Healing takes time, and that’s perfectly okay.'",
        "☀️ 'You are stronger than you think and braver than you feel.'",
        "💖 'Take your medicine, take your rest, take care of you.'"
    ]
    for q in random.sample(quotes, 3):
        st.markdown(f"<blockquote>{q}</blockquote>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Back"):
            prev_page()
    with col2:
        if st.button("Next ➡️"):
            next_page()

# ------------------ PAGE 5: SUMMARY ------------------
elif st.session_state.page == 5:
    set_bg(gradients[5])
    st.header("📋 Summary of Your Day")

    if st.session_state.medicines:
        taken_meds = [m for m, t in st.session_state.taken.items() if t == "Yes ✅"]
        not_taken = [m for m, t in st.session_state.taken.items() if t == "No ❌"]

        st.subheader("✅ Medicines Taken:")
        if taken_meds:
            for med in taken_meds:
                st.markdown(f"- {med}")
        else:
            st.write("None yet!")

        st.subheader("❌ Medicines Not Taken:")
        if not_taken:
            for med in not_taken:
                st.markdown(f"- {med}")
        else:
            st.write("You’ve taken all your medicines! 🌟")
    else:
        st.write("No medicines added today.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Back"):
            prev_page()
    with col2:
        if st.button("Next ➡️"):
            next_page()

# ------------------ PAGE 6: THANK YOU ------------------
elif st.session_state.page == 6:
    set_bg(gradients[6])
    st.markdown("<h1 style='text-align:center;'>🌷 Thank You for Using Medisia 🌷</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Stay healthy, happy, and hydrated 💧💖</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>See you tomorrow!</p>", unsafe_allow_html=True)
    if st.button("🔄 Restart"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.page = 0


