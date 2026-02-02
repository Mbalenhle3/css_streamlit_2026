import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Researcher Profile | Mbalenhle Shandu",
    layout="wide"
)



st.sidebar.title("Miss Mbalenhle P Shandu")
st.sidebar.write("Software engineering")
st.sidebar.write("University of Zululand")

section = st.sidebar.radio(
    "Navigation",
    ["About Me", "Skills & Tools", "Projects", "Contact"]
)

# -----------------------------
# About Me
# -----------------------------
if section == "About Me":
    st.title("About Me")

    col1, col2, col3 = st.columns(3)
    col1.metric("Academic Level", "Honours")
    col2.metric("Research Area", "NLP")
    col3.metric("Focus Language", "isiZulu")

    st.markdown("""
        My academic journey began with a strong foundation in **software engineering**, where I
        developed several applications during my undergraduate studies. Through this experience,
        I gained practical skills in problem-solving, system development, and building real-world
        applications.
        
        Over time, my interests evolved towards **Data Science and Machine Learning**, where I now
        focus on applying data-driven and NLP techniques to solve real-world problems in education
        and language technology.
        
        """)


    st.markdown("""
    ### Research Interests
    - Natural Language Processing (NLP)
    - Sentiment Analysis
    - Low-resource African Languages
    - Multilingual Systems
    - Educational Technology
    """)

# -----------------------------
# Skills & Tools
# -----------------------------
elif section == "Skills & Tools":
    st.title("Skills & Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Skills")
        st.markdown("""
        - Data Analysis
        - Natural Language Processing (NLP)
        - Machine Learning
        - Text Preprocessing
        - Chatbot Development
        - Research & Academic Writing
        """)

    with col2:
        st.subheader("Tools & Technologies")
        st.markdown("""
        - Python
        - Pandas & NumPy
        - Streamlit
        - Scikit-learn
        - Jupyter Notebook
        - Git & GitHub
        """)

# -----------------------------
# Projects
# -----------------------------
elif section == "Projects":
    st.title("Research & Development Projects")

    with st.expander("Multilingual Student Support Chatbot"):
        st.markdown("""
        **Description:**  
        A chatbot developed to assist first-year University of Zululand students with
        queries related to university life and adapting to higher education.

        **Key Features:**
        - Responds in the student’s preferred language
        - Improves accessibility and inclusivity
        - Designed specifically for first-year students
        """)

    with st.expander("Unizulu gym booking system"):
        st.markdown("""
        **Description:**  
        The gym booking system was developed to replace the manual booking system which was time consuming.

        **Impact:**
        - AReduced paperwork
        - Reduced administrative errors
        - Improved efficiency of booking.
        """)

    with st.expander("Emotion Detection from isiZulu Text (Honours Research)"):
        st.markdown("""
        **Description:**  
        An honours research project focused on sentiment analysis from isiZulu text using
        Natural Language Processing techniques.

        **Focus Areas:**
        - Text preprocessing for isiZulu
        - Sentiment analysis
        - Challenges in low-resource languages

        **Future Direction:**
        - Focusing on sentiment analysis on my Honours level
        """)

# -----------------------------
# Contact
# -----------------------------
elif section == "Contact":
    st.title("Contact Information")

    st.markdown("""
    **Name:** Miss Mbalenhle Precide Shandu
    **Institution:** University of Zululand  
    **Field:** Software engineering 

    **Email:**mbalenhleshandu2@gmail.com  
    **Phone / WhatsApp:** 0634338613
    """)

    st.markdown("""
    You may contact me for academic discussions, research collaboration,
    or postgraduate-related inquiries.
    """)
