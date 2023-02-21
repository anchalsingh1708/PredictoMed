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

    #import base64
import pickle
import streamlit as st
#import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import pandas as pd
#from sklearn.linear_model import LogisticRegression
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
#import pickle
#from pathlib import Path
from PIL import Image




#import streamlit_authenticator as stauth

# loading the saved models
#from PIL import Image

icon = Image.open('hospital.png') 





diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

calories_model = pickle.load(open('calories_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('PredictoMed',
                          
                          ['Home page',
                           'Diabetes Prediction',
                           'Calories Burnt Prediction',
                           'Parkinsons Prediction'],
                          #icons=['house','activity','person'],
			   icons=['house','activity','heart','person'],
                          menu_icon="command",
                          default_index=0)




hide_streamlit_style = """
            <style>
            
           footer {
           	
           	visibility: hidden;
           	
           	}
           footer:after {
           	content:'@anchal'; 
           	visibility: visible;
           	display: block;
           	position: relative;
           	#background-color: red;
           	padding: 5px;
           	top: 2px;
           }
           
            </style>
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#MainMenu {visibility: hidden;}




#Home Page design
if (selected == 'Home page'):
    header=st.container()
    def set_background_image(image_path):
        from PIL import Image
        #st.write("Welcome to PredictoMed that predicts the likelihood of heart disease, diabetes, and Parkinson's disease based on symptoms.")
        st.markdown("<p style='font-family: Comic Sans MS; font-size: 20px;'>Welcome to PredictoMed that predicts the likelihood of Diabetes, and Parkinson's disease.</p>", unsafe_allow_html=True)
        image = Image.open(image_path)
        st.image(image, width=700,use_column_width=True)
    
    set_background_image("predictomed home.jpg")
#The use_column_width=True argument makes the image span the entire width of the page
# and the clamp=True argument makes sure that the aspect ratio of the image is maintained  
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
   
# Load the diabetes dataset
    df = pd.read_csv("diabetes.csv")

# Create a title and header
    st.header("Exploring Diabetes Dataset")
    #img = Image.open("E:\PILLAI COLLEGE\MLPROJECT\diabetes.jpg")
    #st.image(img, width=400)
    st.write("Diabetes is a chronic condition in which the body is unable to produce or effectively use insulin, a hormone that regulates blood sugar levels. This leads to elevated levels of glucose in the blood, which can cause damage to various organs and tissues over time.")
    

# Show the first 5 rows of the dataset
    st.write(df.head())

# Create a selectbox to choose which column to plot
    column = st.selectbox("Select a column", df.columns)

# Plot a bar chart of the selected column
    st.bar_chart(df[column])

    st.title('Diabetes Prediction')
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        if not Pregnancies or not Glucose or not BloodPressure or not SkinThickness or not Insulin or not BMI or not DiabetesPedigreeFunction or not Age:
            st.write("Please enter a value for all input fields")
        else:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
            
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        
        st.success(diab_diagnosis)
    




# Heart Disease Prediction Page
if (selected == 'Calories Burnt Prediction'):
    
    # page title
    st.title('Calories Burnt Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.text_input('Gender')
        
    with col2:
        age = st.text_input('Age')
        
    with col3:
        height = st.text_input('Height')
        
    with col1:
        Duration = st.text_input('Duration')
        
    with col2:
        Heart_Rate = st.text_input('Heart_Rate')
        
    with col3:
        Body_Temp = st.text_input('Body_Temp')
        
    
        
     
     
    # code for Prediction
    Calories_d = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        calories_prediction = calories_model.predict([[gender,age,height,Duration,Heart_Rate,Body_Temp]])                          
        
        Calories_d=calories_prediction
        
    st.success(Calories_d)

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
   
    # Load the Parkinson's dataset
    df = pd.read_csv("parkinsons.csv")

# Create a title and header
    st.title("Parkinson's Analysis")
    st.header("Exploring Parkinson's Data")

# Show the first 5 rows of the dataset
    st.write(df.head())



# Show summary statistics for the numerical columns
    st.write(df.describe())

# Create a selectbox to choose which column to plot
    #column = st.selectbox("Select a column", df.columns)

# Plot a bar chart of the selected column
    #st.bar_chart(df[column])
    
    st.title("Parkinson's Disease Prediction")
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
   
        
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        if not fo or not fhi or not flo or not Jitter_percent or not Jitter_Abs or not RAP or not PPQ or not DDP or not Shimmer or not Shimmer_dB or not APQ3 or not APQ5 or not APQ or not DDA or not NHR or not HNR or not RPDE or not DFA or not spread1 or not spread2 or not D2 or not PPE :
            st.write("Please enter a value for all input fields")
        else:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
              
        st.success(parkinsons_diagnosis)
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass


