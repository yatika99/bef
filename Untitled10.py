#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Mock Database (In-memory for simplicity)
users = {}

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Sign Up", "Dashboard", "Budgeting", "Savings & Goals", "Investments", "Debt Management"])

# Homepage
def homepage():
    st.title("Welcome to Your Financial Journey")
    st.subheader("See how much you can save in just 2 minutes!")
    st.write("Join 500,000+ Indians improving their financial future!")
    if st.button("Start Your Financial Journey"):
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

