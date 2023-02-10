import streamlit as st
import webbrowser
from PIL import Image

icon = Image.open('hospital.png') 

st.set_page_config(
	page_title = 'PredictoMed Login',
	page_icon = icon,
	layout = 'centered', #wide
	initial_sidebar_state = 'auto', #collapsed, expanded
	menu_items={
		'Get Help': 'https://streamlit.io',
		'Report a bug': 'https://github.com/anchalsingh1708',
		'About':'About your application: **Fit Me Up**'
	}
	)




def redirect(_url):
    link = ''
    st.markdown(link, unsafe_allow_html=True)
# Create an empty container
placeholder = st.empty()

actual_email = "anchal"
actual_password = "123"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    webbrowser.open('https://predictomed.streamlit.app/')
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass


