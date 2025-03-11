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
            background-color: #f0f8ff !important; /* Light blue background */
            color: #1E3A8A !important; /* Dark blue text */
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: white;
        }
        .css-1d391kg, .stButton>button {
            background-color: #1E3A8A !important;
            color: white !important;
            border-radius: 5px;
        }
        .css-1d391kg:hover, .stButton>button:hover {
            background-color: #3B82F6 !important;
        }
        .banner-container {
            position: relative;
            text-align: center;
            margin-bottom: 20px;
        }
        .banner-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.5);
            color: white;
            padding: 20px;
            border-radius: 10px;
            font-size: 24px;
            font-weight: bold;
        }
        .justified-text {
            text-align: justify;
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
    
    st.markdown("### **Join 500,000+ Indians improving their financial future!**")
    
    st.markdown("## **About Us**")
    st.markdown("<div class='justified-text'>We are committed to helping individuals make informed financial decisions through behavioral science-driven strategies.</div>", unsafe_allow_html=True)
    
    # Left-Side Navigation Menu
    with st.sidebar:
        st.title("Navigation")
        menu = st.radio("Go to", ["Pricing", "Offerings", "Customer Testimonials", "Blogs & Resources", "Contact Us"])
    
    if menu == "Pricing":
        st.markdown("## **Pricing**")
        st.markdown("<div class='justified-text'>Affordable pricing plans tailored to suit different financial needs.</div>", unsafe_allow_html=True)
    elif menu == "Offerings":
        st.markdown("## **Offerings**")
        st.markdown("<div class='justified-text'>- Smart Budgeting Tools\n- Investment Guidance\n- Debt Management Solutions\n- Savings Goal Tracking</div>", unsafe_allow_html=True)
    elif menu == "Customer Testimonials":
        st.markdown("## **Customer Testimonials**")
        st.markdown("<div class='justified-text'>'This platform transformed my financial habits! - Raj, Mumbai'</div>", unsafe_allow_html=True)
    elif menu == "Blogs & Resources":
        st.markdown("## **Blogs & Resources**")
        st.markdown("<div class='justified-text'>Read expert financial advice and stay updated on money management trends.</div>", unsafe_allow_html=True)
    elif menu == "Contact Us":
        st.markdown("## **Contact Us**")
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
