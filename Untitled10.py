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
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Apply Custom CSS
add_custom_css()

def homepage():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Pricing", "Blogs & Resources", "Customer Testimonials", "Contact Us"])
    
    # Sign Up / Login Button on Top Right Corner
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    col1, col2 = st.columns([8, 2])
    with col2:
        if st.button("Sign Up / Login", key="login_button"):
            st.session_state["show_signup"] = True
            st.rerun()
    
    if page == "Home":
        st.title("Welcome to Your Financial Journey")
        
        # Enlarged Banner Image with Hook Quote
        st.markdown("""
        <div class="banner-container">
            <img src="https://t3.ftcdn.net/jpg/07/78/11/08/360_F_778110813_nGqTda2YeQ3IE85xss0YzUGWOozNwC3d.jpg" width="100%">
            <div class="banner-text">See how much you can save in just 2 minutes!</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### <div class='section-heading'>Join 500,000+ Indians improving their financial future!</div>", unsafe_allow_html=True)
        
        st.markdown("## <div class='section-heading'>About Us</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>We are committed to helping individuals make informed financial decisions through behavioral science-driven strategies.</div>", unsafe_allow_html=True)
    
    elif page == "Pricing":
        st.markdown("## <div class='section-heading'>Pricing</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Choose the plan that fits your financial goals the best.</div>", unsafe_allow_html=True)
    
    elif page == "Blogs & Resources":
        st.markdown("## <div class='section-heading'>Blogs & Resources</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Explore our latest insights on saving and investing.</div>", unsafe_allow_html=True)
    
    elif page == "Customer Testimonials":
        st.markdown("## <div class='section-heading'>Customer Testimonials</div>", unsafe_allow_html=True)
        st.markdown("<div class='justified-text'>Read stories from real users who transformed their financial future.</div>", unsafe_allow_html=True)
    
    elif page == "Contact Us":
        st.markdown("## <div class='section-heading'>Contact Us</div>", unsafe_allow_html=True)
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submit = st.form_submit_button("Send Inquiry")
            if submit:
                st.success("Thank you for reaching out! We'll get back to you soon.")
    
    # Sign Up / Login Form
    if st.session_state.get("show_signup", False):
        with st.form("signup_form"):
            st.title("Sign Up / Login")
            email = st.text_input("Enter your email:")
            goal = st.selectbox("What’s your financial goal?", ["Save more", "Invest wisely", "Reduce debt"])
            submit = st.form_submit_button("Get Started")
            if submit:
                st.session_state.logged_in = True
                st.session_state.show_signup = False
                st.success("Login successful! Redirecting to dashboard...")
                st.switch_page("dashboard")

    # Redirect to Dashboard if logged in
    if st.session_state.get("logged_in", False):
        st.switch_page("dashboard")

homepage()
