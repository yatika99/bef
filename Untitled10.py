#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import base64

# Custom Styling for Blue & White Theme with Watermark
def add_custom_css():
    custom_css = """
    <style>
        body {
            background-color: #f0f8ff !important; /* Light blue background */
            color: #1E3A8A !important; /* Dark blue text */
        }
        .stApp {
            background: url('https://www.transparenttextures.com/patterns/asfalt-dark.png');
            background-size: cover;
        }
        .css-1d391kg, .stButton>button {
            background-color: #1E3A8A !important;
            color: white !important;
            border-radius: 5px;
        }
        .css-1d391kg:hover, .stButton>button:hover {
            background-color: #3B82F6 !important;
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
    st.image("https://t3.ftcdn.net/jpg/07/78/11/08/360_F_778110813_nGqTda2YeQ3IE85xss0YzUGWOozNwC3d.jpg", use_column_width=True)
    st.subheader("See how much you can save in just 2 minutes!")
    st.write("Join 500,000+ Indians improving their financial future!")
    
    st.markdown("## About Us")
    st.write("We are committed to helping individuals make informed financial decisions through behavioral science-driven strategies.")
    
    # Left-Side Navigation Menu
    with st.sidebar:
        st.title("Navigation")
        menu = st.radio("Go to", ["Pricing", "Offerings", "Customer Testimonials", "Blogs & Resources", "Contact Us"])
    
    if menu == "Pricing":
        st.markdown("## Pricing")
        st.write("Affordable pricing plans tailored to suit different financial needs.")
    elif menu == "Offerings":
        st.markdown("## Offerings")
        st.write("- Smart Budgeting Tools\n- Investment Guidance\n- Debt Management Solutions\n- Savings Goal Tracking")
    elif menu == "Customer Testimonials":
        st.markdown("## Customer Testimonials")
        st.write("'This platform transformed my financial habits! - Raj, Mumbai'")
    elif menu == "Blogs & Resources":
        st.markdown("## Blogs & Resources")
        st.write("Read expert financial advice and stay updated on money management trends.")
    elif menu == "Contact Us":
        st.markdown("## Contact Us")
        st.write("Email: support@finwebsite.com | Phone: +91-1234567890")
    
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
