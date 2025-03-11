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
        }
        .stButton>button:hover {
            background-color: #1565C0 !important;
        }
        .banner-container {
            position: relative;
            text-align: center;
            margin-bottom: 30px;
            background-color: #BBDEFB; /* Light blue background behind banner */
            padding: 20px;
            border-radius: 10px;
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
        .sidebar {
            background-color: #0D47A1 !important;
            color: white !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Apply Custom CSS
add_custom_css()

# Mock Database (In-memory for simplicity)
users = {}

def dashboard():
    st.title("User Dashboard")
    st.sidebar.title("Dashboard Navigation")
    dashboard_menu = st.sidebar.radio("Choose a section", ["My Investments", "Financial Tools", "Reports", "Settings", "Logout"])
    
    if dashboard_menu == "My Investments":
        st.markdown("## <div class='section-heading'>My Investments</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Track and manage your investments efficiently.</div>", unsafe_allow_html=True)
    elif dashboard_menu == "Financial Tools":
        st.markdown("## <div class='section-heading'>Financial Tools</div>", unsafe_allow_html=True)
        loan_amount = st.number_input("Loan Amount", min_value=1000, value=50000)
        interest_rate = st.number_input("Interest Rate (%)", min_value=1.0, value=7.5)
        tenure = st.slider("Tenure (in years)", 1, 30, 10)
        emi = (loan_amount * (interest_rate/1200) * ((1 + interest_rate/1200) ** (tenure * 12))) / (((1 + interest_rate/1200) ** (tenure * 12)) - 1)
        st.write(f"Your monthly EMI: ₹{emi:.2f}")
    elif dashboard_menu == "Reports":
        st.markdown("## <div class='section-heading'>Reports</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>View your financial reports and insights.</div>", unsafe_allow_html=True)
    elif dashboard_menu == "Settings":
        st.markdown("## <div class='section-heading'>Settings</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Manage your account preferences.</div>", unsafe_allow_html=True)
    elif dashboard_menu == "Logout":
        st.session_state.logged_in = False
        st.rerun()

# Homepage
def homepage():
    st.title("Welcome to Your Financial Journey")
    
    if st.session_state.get("logged_in", False):
        dashboard()
        return
    
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
    
    # Sign Up / Login
    if st.button("Sign Up / Login"):
        st.session_state.show_signup = True
    
    if st.session_state.get("show_signup", False):
        with st.form("signup_form"):
            st.title("Sign Up / Login")
            email = st.text_input("Enter your email:")
            goal = st.selectbox("What’s your financial goal?", ["Save more", "Invest wisely", "Reduce debt"])
            submit = st.form_submit_button("Get Started")
            if submit:
                users[email] = {'goal': goal, 'savings': 0, 'expenses': {}}
                st.session_state.logged_in = True
                st.session_state.show_signup = False
                st.success("Login successful! Redirecting to dashboard...")
                st.rerun()

# Run Homepage
homepage()
