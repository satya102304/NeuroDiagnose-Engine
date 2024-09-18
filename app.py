import streamlit as st
import time

# Sample login function
def login(username, password):
    # For demonstration purposes, accept any username and password
    if username and password:
        return True
    return False

# Create a login page
def login_page():
    st.title("Healthcare Chatbot Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
            st.experimental_rerun()  # Refresh to move to the next step
        else:
            st.error("Invalid credentials")

# Show the animated doctor greeting
def show_greeting():
    # Custom CSS for animation
    st.markdown("""
        <style>
        .doctor-image {
            animation: fadeIn 3s ease forwards;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Doctor image with the animated "Hi" message
    st.image("doctor_image.png", caption="Dr. Health", use_column_width=True, class_="doctor-image")
    st.markdown("<h3 style='text-align: center;'>Hi! How can I assist you today?</h3>", unsafe_allow_html=True)
    
    time.sleep(3)  # Pause for effect before moving to the chatbot
    st.session_state.greeted = True

# Create the chatbot interface
def chatbot_interface():
    st.title("Healthcare Chatbot")
    user_input = st.text_input("Ask me anything about your health!")
    if user_input:
        st.write(f"You asked: {user_input}")
        # Here, you would integrate your chatbot's response logic
        st.write("Chatbot response goes here.")

# Main app logic
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'greeted' not in st.session_state:
    st.session_state.greeted = False

# Step-by-step process
if not st.session_state.logged_in:
    login_page()
elif not st.session_state.greeted:
    show_greeting()
else:
    chatbot_interface()
