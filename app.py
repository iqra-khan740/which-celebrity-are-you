import streamlit as st
from io import BytesIO

st.set_page_config(
    page_title="Which Bollywood Celebrity Are You?",
    page_icon="🎬",
    layout="wide"
)

dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=True)
def apply_theme(dark_mode):
    if dark_mode:
        st.markdown("""
            <style>
            html, body, [data-testid="stAppViewContainer"] {
                background-color: #000000;
                color: #00FF00;
            }
            h1, h2, h3, h4, h5, h6, p, label, div, span {
                color: #00FF00 !important;
            }
            .stButton>button, .stDownloadButton>button {
                background-color: #003300;
                color: #00FF00;
                border-radius: 8px;
                font-weight: bold;
            }
            .stSelectbox > div > div,
            .stSelectbox > div > div > div,
            .stRadio label, .stSelectbox label {
                background-color: #000000;
                color: #00FF00 !important;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            html, body, [data-testid="stAppViewContainer"] {
                background-color: #FFFFFF;
                color: #000000;
            }
            h1, h2, h3, h4, h5, h6, p, label, div, span {
                color: #000000 !important;
            }
            .stButton>button, .stDownloadButton>button {
                background-color: #DDDDDD;
                color: #000000;
                border-radius: 8px;
                font-weight: bold;
            }
            </style>
        """, unsafe_allow_html=True)

apply_theme(dark_mode)

st.markdown("<h1 style='text-align: center;'>🎥 Which Bollywood Celebrity Are You?</h1><hr>", unsafe_allow_html=True)

all_celebrities = ["Mahira Khan", "Hania Amir", "Shehzhad Khan", "Shehzhad Roy", "Wahaj Ali"]
selected_celebrities = st.multiselect("Choose the celebrities to include in the quiz:", all_celebrities, default=all_celebrities)

if len(selected_celebrities) < 2:
    st.warning("Please select at least 2 celebrities to continue the quiz.")
    st.stop()

with st.form("quiz_form"):
    st.subheader("Answer these 5 questions honestly:")
    q1 = st.selectbox("🌈 What's your ideal weekend like?", [
        "Partying with friends", "Reading a book", "Exploring new places", "Working out"])
    q2 = st.selectbox("🎥 Pick a favorite Bollywood genre:", ["Action", "Drama", "Comedy"])
    q3 = st.selectbox("👗 Your fashion style is:", ["Classic & Elegant", "Trendy & Bold", "Casual & Sporty"])
    q4 = st.selectbox("💪 What's your biggest strength?", ["Confidence", "Charm", "Discipline", "Creativity"])
    q5 = st.selectbox("🎨 Pick a color that vibes with you:", ["Red", "Black", "Blue", "Pink"])
    gender = st.selectbox("👤 What's your gender?", ["Male", "Female"])
    submitted = st.form_submit_button("Reveal My Celebrity Twin 🌟")
if submitted:
    male_celebs = ["Shehzhad Khan", "Shehzhad Roy", "Wahaj Ali"]
    female_celebs = ["Mahira Khan", "Hania Amir"]
    gender_celebrities = male_celebs if gender == "Male" else female_celebs

    final_celebrities = [c for c in selected_celebrities if c in gender_celebrities]

    if len(final_celebrities) < 1:
        st.error("No matching celebrities for your gender. Please choose others.")
        st.stop()

    scores = {celeb: 0 for celeb in final_celebrities}

    if q1 == "Reading a book":
        if "Mahira Khan" in scores: scores["Mahira Khan"] += 1
    if q1 == "Exploring new places":
        if "Hania Amir" in scores: scores["Hania Amir"] += 1
    if q1 == "Partying with friends":
        if "Wahaj Ali" in scores: scores["Wahaj Ali"] += 1
    if q1 == "Working out":
        if "Shehzhad Roy" in scores: scores["Shehzhad Roy"] += 1

    if q2 == "Action":
        if "Shehzhad Khan" in scores: scores["Shehzhad Khan"] += 1
    if q2 == "Drama":
        if "Mahira Khan" in scores: scores["Mahira Khan"] += 1
    if q2 == "Comedy":
        if "Hania Amir" in scores: scores["Hania Amir"] += 1

    if q3 == "Classic & Elegant":
        if "Mahira Khan" in scores: scores["Mahira Khan"] += 1
    if q3 == "Trendy & Bold":
        if "Hania Amir" in scores: scores["Hania Amir"] += 1
    if q3 == "Casual & Sporty":
        if "Wahaj Ali" in scores: scores["Wahaj Ali"] += 1

    if q4 == "Confidence":
        if "Wahaj Ali" in scores: scores["Wahaj Ali"] += 1
    if q4 == "Charm":
        if "Hania Amir" in scores: scores["Hania Amir"] += 1
    if q4 == "Discipline":
        if "Shehzhad Khan" in scores: scores["Shehzhad Khan"] += 1
    if q4 == "Creativity":
        if "Shehzhad Roy" in scores: scores["Shehzhad Roy"] += 1

    if q5 == "Red":
        if "Mahira Khan" in scores: scores["Mahira Khan"] += 1
    if q5 == "Black":
        if "Shehzhad Roy" in scores: scores["Shehzhad Roy"] += 1
    if q5 == "Blue":
        if "Hania Amir" in scores: scores["Hania Amir"] += 1
    if q5 == "Pink":
        if "Wahaj Ali" in scores: scores["Wahaj Ali"] += 1

    winner = max(scores, key=scores.get)
    st.success(f"🎉 You are most like: *{winner}*!")

    celebrity_images = {
        "Mahira Khan": "uploaded_image/Mahira khan.png",
        "Hania Amir": "uploaded_image/Hania Amir.jpg",
        "Shehzhad Khan": "uploaded_image/Shehzhad Khan.jpg",
        "Shehzhad Roy": "uploaded_image/Shehzhad Roy.PNG",
        "Wahaj Ali": "uploaded_image/Wahaj Ali.jpg"
    }

    if winner in celebrity_images:
        st.image(celebrity_images[winner], caption=winner, use_container_width=True)
    else:
        st.warning("No image available for the selected celebrity.")

    st.balloons()

    result_text = f"You are... {winner}"
    buffer = BytesIO()
    buffer.write(result_text.encode())
    buffer.seek(0)
    st.download_button("📥 Download Result as Text", buffer, file_name="my_celebrity_result.txt", mime="text/plain")

    if st.button("🔄 Retake Quiz"):
        st.experimental_rerun()

st.markdown("""
    <hr>
    <div style='text-align:center; font-size: 0.9rem;'>
    Built with ❤ using Streamlit by Iqra Khan
    </div>
""", unsafe_allow_html=True)