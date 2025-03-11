#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import base64

# Custom Styling for Blue & White Theme
def add_custom_css():
    custom_css = """
    <style>
        body {
            background-color: #E3F2FD !important; /* Light blue background */
            color: #0D47A1 !important; /* Dark blue text */
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background-color: white;
        }
        .stButton>button {
            background-color: #0D47A1 !important;
            color: white !important;
            border-radius: 5px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #1565C0 !important;
        }
        .banner-container {
            position: relative;
            text-align: center;
            margin-bottom: 30px;
        }
        .banner-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.6);
            color: white;
            padding: 20px;
            border-radius: 10px;
            font-size: 28px;
            font-weight: bold;
        }
        .justified-text {
            text-align: justify;
            font-size: 16px;
        }
        .section-heading {
            font-weight: bold;
            color: #0D47A1;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Apply Custom CSS
add_custom_css()

# Mock Database (In-memory for simplicity)
users = {}

# Homepage
def homepage():
    st.title("Welcome to Your Financial Journey")
    
    # Enlarged Banner Image with Hook Quote
    st.markdown("""
    <div class="banner-container">
        <img src="https://t3.ftcdn.net/jpg/07/78/11/08/360_F_778110813_nGqTda2YeQ3IE85xss0YzUGWOozNwC3d.jpg" width="100%">
        <div class="banner-text">See how much you can save in just 2 minutes!</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)  # Space between banner and next section
    st.markdown("### <div class='section-heading'>Join 500,000+ Indians improving their financial future!</div>", unsafe_allow_html=True)
    
    st.markdown("## <div class='section-heading'>About Us</div>", unsafe_allow_html=True)
    st.markdown("<div class='justified-text'>We are committed to helping individuals make informed financial decisions through behavioral science-driven strategies.</div>", unsafe_allow_html=True)
    
    # Left-Side Navigation Menu
    with st.sidebar:
        st.title("Navigation")
        menu = st.radio("Go to", ["Pricing", "Offerings", "Customer Testimonials", "Blogs & Resources", "Contact Us"])
    
    if menu == "Pricing":
        st.markdown("## <div class='section-heading'>Pricing</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Affordable pricing plans tailored to suit different financial needs.</div>", unsafe_allow_html=True)
    elif menu == "Offerings":
        st.markdown("## <div class='section-heading'>Offerings</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>- Smart Budgeting Tools<br>- Investment Guidance<br>- Debt Management Solutions<br>- Savings Goal Tracking</div>", unsafe_allow_html=True)
    elif menu == "Customer Testimonials":
        st.markdown("## <div class='section-heading'>Customer Testimonials</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>'This platform transformed my financial habits! - Raj, Mumbai'</div>", unsafe_allow_html=True)
    elif menu == "Blogs & Resources":
        st.markdown("## <div class='section-heading'>Blogs & Resources</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Read expert financial advice and stay updated on money management trends.</div>", unsafe_allow_html=True)
    elif menu == "Contact Us":
        st.markdown("## <div class='section-heading'>Contact Us</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Email: support@finwebsite.com | Phone: +91-1234567890</div>", unsafe_allow_html=True)
    
    # Sign Up Pop-up
    if st.button("Sign Up / Login"):
        st.session_state.show_signup = True
    
    if st.session_state.get("show_signup", False):
        with st.form("signup_form"):
            st.title("Sign Up")
            email = st.text_input("Enter your email:")
            goal = st.selectbox("What’s your financial goal?", ["Save more", "Invest wisely", "Reduce debt"])
            submit = st.form_submit_button("Get Started")
            if submit:
                users[email] = {'goal': goal, 'savings': 0, 'expenses': {}}
                st.session_state.logged_in = True
                st.session_state.show_signup = False
                st.success("Account created successfully!")

# Run Homepage
homepage()
