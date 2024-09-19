import streamlit as st

# Function for login
def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "doctor" and password == "12345":  # Add real authentication
            st.session_state["logged_in"] = True
            st.experimental_rerun()  # Refresh to load chat area

# Function to display animated doctor picture
def animated_doctor():
    st.markdown(
        """
        <style>
        @keyframes fadeOut {
            0% {opacity: 1;}
            100% {opacity: 0;}
        }
        .doctor-img {
            position: absolute;
            top: 50px;
            right: 50px;
            width: 150px;
            animation: fadeOut 2s forwards;  /* Reduced animation duration to 2 seconds */
        }
        </style>
        <img class="doctor-img" src="https://github.com/satya102304/NeuroDiagnose-Engine/blob/main/hidoc.png" alt="Doctor">
        """, unsafe_allow_html=True
    )

# Chat UI after login
def chat_ui():
    st.title("Healthcare Chatbot")
    animated_doctor()  # Call the function to show the animated doctor

    # Chatbox input
    user_input = st.text_input("Ask a question:")
    if st.button("Send"):
        st.write(f"Response: {user_input}")  # Placeholder for chatbot response logic

if "logged_in" in st.session_state and st.session_state["logged_in"]:
    chat_ui()
else:
    st.title("Healthcare Chatbot Login")
    login()
