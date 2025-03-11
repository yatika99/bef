#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import base64
import streamlit.components.v1 as components

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
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #1565C0 !important;
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

def homepage():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Pricing", "Blogs & Resources", "Customer Testimonials", "Contact Us"])
    
    # Sign Up / Login Logic
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    if page == "Home":
        st.title("Welcome to Your Financial Journey")
        st.markdown("### Join 500,000+ Indians improving their financial future!")
        st.markdown("## About Us")
        st.markdown("We are committed to helping individuals make informed financial decisions through behavioral science-driven strategies.")
    
    elif page == "Pricing":
        st.markdown("## Pricing")
        st.markdown("Choose the plan that fits your financial goals the best.")
    
    elif page == "Blogs & Resources":
        st.markdown("## Blogs & Resources")
        st.markdown("Explore our latest insights on saving and investing.")
    
    elif page == "Customer Testimonials":
        st.markdown("## Customer Testimonials")
        st.markdown("Read stories from real users who transformed their financial future.")
    
    elif page == "Contact Us":
        st.markdown("## Contact Us")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submit = st.form_submit_button("Send Inquiry")
            if submit:
                st.success("Thank you for reaching out! We'll get back to you soon.")
    
    # Login/Signup and Redirect to Dashboard
    if not st.session_state["logged_in"]:
        with st.form("signup_form"):
            st.title("Sign Up / Login")
            email = st.text_input("Enter your email:")
            goal = st.selectbox("What’s your financial goal?", ["Save more", "Invest wisely", "Reduce debt"])
            submit = st.form_submit_button("Get Started")
            if submit:
                st.session_state.logged_in = True
                st.success("Login successful! Redirecting to dashboard...")
                st.experimental_rerun()
    else:
        dashboard()

def dashboard():
    st.sidebar.title("Dashboard Navigation")
    section = st.sidebar.radio("Go to", ["Dashboard", "Budget", "Savings", "Investments", "Debt Management", "Profile", "Settings"])
    
    st.title("Dashboard")
    st.subheader("Welcome, User!")
    
    if section == "Dashboard":
        st.metric(label="Financial Health Score", value="78/100", delta="Improve by increasing savings")
        st.markdown("## Segments")
        st.button("Budget")
        st.button("Savings")
        st.button("Investments")
        st.button("Debt Management")
    
    elif section == "Budget":
        st.markdown("## Budget Overview")
        st.markdown("Manage your expenses wisely.")
    
    elif section == "Savings":
        st.markdown("## Savings Plan")
        st.markdown("Track and grow your savings.")
    
    elif section == "Investments":
        st.markdown("## Investment Portfolio")
        st.markdown("Monitor and optimize your investments.")
    
    elif section == "Debt Management":
        st.markdown("## Debt Reduction Strategies")
        st.markdown("Plan how to reduce and manage debt effectively.")
    
    elif section == "Profile":
        st.markdown("## User Profile")
        st.markdown("Manage your personal information and preferences.")
    
    elif section == "Settings":
        st.markdown("## Settings")
        st.markdown("Customize your experience.")
        if st.button("Sign Out"):
            st.session_state.logged_in = False
            st.experimental_rerun()

homepage()
