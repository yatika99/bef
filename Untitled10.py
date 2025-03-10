#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Mock Database (In-memory for simplicity)
users = {}

# Homepage
def homepage():
    st.title("Welcome to Your Financial Journey")
    st.subheader("See how much you can save in just 2 minutes!")
    if st.button("Start Your Financial Journey"):
        st.session_state.page = "signup"

# Signup Page
def signup():
    st.title("Sign Up")
    email = st.text_input("Enter your email:")
    goal = st.selectbox("What’s your financial goal?", ["Save more", "Invest wisely", "Reduce debt"])
    if st.button("Get Started"):
        users[email] = {'goal': goal, 'savings': 0, 'expenses': {}}
        st.session_state.page = "dashboard"
        st.session_state.email = email

# Dashboard
def dashboard():
    email = st.session_state.email
    user = users.get(email, {})
    st.title("Your Financial Dashboard")
    st.subheader(f"Financial Goal: {user.get('goal', 'Not Set')}")
    st.metric("Total Savings", f"₹{user.get('savings', 0)}")
    
    st.subheader("Add Expenses")
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0)
    if st.button("Add Expense"):
        user['expenses'][category] = user['expenses'].get(category, 0) + amount
        st.success("Expense Added!")
    
    st.subheader("Add Savings")
    savings_amount = st.number_input("Savings Amount", min_value=0.0)
    if st.button("Save Money"):
        user['savings'] += savings_amount
        st.success("Savings Updated!")

# Streamlit Navigation
if 'page' not in st.session_state:
    st.session_state.page = "homepage"
if 'email' not in st.session_state:
    st.session_state.email = ""

if st.session_state.page == "homepage":
    homepage()
elif st.session_state.page == "signup":
    signup()
elif st.session_state.page == "dashboard":
    dashboard()


