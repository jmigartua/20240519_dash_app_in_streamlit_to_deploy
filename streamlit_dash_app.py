import streamlit as st
import threading
import time
import subprocess
import requests

# Function to start the Dash app
def start_dash():
    subprocess.Popen(["python", "dash_app.py"])

# Function to check if the Dash app is running
def check_dash():
    while True:
        try:
            response = requests.get("http://localhost:8050")
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)

# Start the Dash app in a separate thread
threading.Thread(target=start_dash).start()

# Check if the Dash app is running before embedding it
check_dash()

# Display the Dash app in an iframe within Streamlit
st.title("Dash App in Streamlit")
st.write("This is an example of embedding a Dash app within Streamlit.")

# Embed the Dash app using an iframe
st.markdown(
    """
    <iframe src="http://localhost:8050" width="100%" height="800" style="border:none;"></iframe>
    """,
    unsafe_allow_html=True
)
