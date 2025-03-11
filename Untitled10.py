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
        .sidebar .sidebar-content {
            background-color: #1E3A8A !important; /* Dark blue sidebar */
            color: white !important;
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

# Apply Custom CSS\add_custom_css()

# Mock Database (In-memory for simplicity)
users = {}

# Navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to", ["Homepage", "Sign Up", "Dashboard", "Budgeting", "Savings & Goals", "Investments", "Debt Management"])

# Homepage
def homepage():
    st.title("Welcome to Your Financial Journey")
    st.subheader("See how much you can save in just 2 minutes!")
    st.write("Join 500,000+ Indians improving their financial future!")
    
    st.markdown("## About Us")
    st.write("We are committed to helping individuals make informed financial decisions through behavioral science-driven strategies.")
    
    st.markdown("## Pricing")
    st.write("Affordable pricing plans tailored to suit different financial needs.")
    
    st.markdown("## Offerings")
    st.write("- Smart Budgeting Tools\n- Investment Guidance\n- Debt Management Solutions\n- Savings Goal Tracking")
    
    st.markdown("## Customer Testimonials")
    st.write("'This platform transformed my financial habits! - Raj, Mumbai'")
    
    st.markdown("## Blogs & Resources")
    st.write("Read expert financial advice and stay updated on money management trends.")
    
    st.markdown("## Contact Us")
    st.write("Email: support@finwebsite.com | Phone: +91-1234567890")
    
    st.markdown("## Sign Up / Login")
    if st.button("Sign Up / Login"):
        st.experimental_set_query_params(page="Sign Up")

# Signup Page
def signup():
    st.title("Sign Up")
    email = st.text_input("Enter your email:")
    goal = st.selectbox("What’s your financial goal?", ["Save more", "Invest wisely", "Reduce debt"])
    if st.button("Get Started"):
        users[email] = {'goal': goal, 'savings': 0, 'expenses': {}}
        st.experimental_set_query_params(page="Dashboard", email=email)

# Dashboard
def dashboard():
    email = st.experimental_get_query_params().get("email", [""])[0]
    user = users.get(email, {})
    st.title("Your Financial Dashboard")
    st.subheader(f"Financial Goal: {user.get('goal', 'Not Set')}")
    st.metric("Total Savings", f"₹{user.get('savings', 0)}")

# Budgeting Page
def budgeting():
    st.title("Budgeting & Expense Tracking")
    email = st.experimental_get_query_params().get("email", [""])[0]
    user = users.get(email, {})
    st.subheader("Add Expenses")
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Add Expense"):
        user['expenses'][category] = user['expenses'].get(category, 0) + amount
        st.success("Expense Added!")

# Savings & Goals Page
def savings_goals():
    st.title("Savings & Goal Setting")
    email = st.experimental_get_query_params().get("email", [""])[0]
    user = users.get(email, {})
    st.subheader("Set Savings Goals")
    savings_amount = st.number_input("Savings Amount", min_value=0.0)
    if st.button("Save Money"):
        user['savings'] += savings_amount
        st.success("Savings Updated!")

# Investments Page
def investments():
    st.title("Investments & Wealth Management")
    st.write("Smart investment suggestions based on your risk profile coming soon!")

# Debt Management Page
def debt_management():
    st.title("Debt & Credit Management")
    st.write("Track your loans, credit scores, and repayments here.")

# Page Routing
if page == "Homepage":
    homepage()
elif page == "Sign Up":
    signup()
elif page == "Dashboard":
    dashboard()
elif page == "Budgeting":
    budgeting()
elif page == "Savings & Goals":
    savings_goals()
elif page == "Investments":
    investments()
elif page == "Debt Management":
    debt_management()
