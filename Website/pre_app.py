import streamlit as st
import pickle
import pandas as pd

# Load model
pipe = pickle.load(open('Hyperperameter_pipe.pkl', 'rb'))

# Constants
teams = ['Royal Challengers Bengaluru', 'Delhi Capitals', 'Mumbai Indians',
         'Punjab Kings', 'Kolkata Knight Riders', 'Sunrisers Hyderabad',
         'Chennai Super Kings', 'Rajasthan Royals', 'Gujarat Titans',
         'Lucknow Super Giants']

cities = ['Hyderabad', 'Bengaluru', 'Mumbai', 'Indore', 'Kolkata',
          'Bangalore', 'Delhi', 'Chandigarh', 'Chennai', 'Jaipur', 'Pune',
          'Visakhapatnam', 'Abu Dhabi', 'Ahmedabad', 'Sharjah', 'Dubai',
          'Navi Mumbai', 'Lucknow', 'Guwahati', 'Dharamsala', 'Mohali',
          'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
          'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
          'Cuttack', 'Nagpur', 'Raipur', 'Ranchi']

def apply_custom_css():
    st.markdown("""
    <style>
    .big-font {
        font-size: 16px !important;
        font-weight: bold;
        color: #333333;
        margin-bottom: 1px; /* Reduced bottom margin */
    }
    
    .medium-font {
        font-size: 14px !important;
        color: #333333;
        margin-bottom: 1px; /* Reduced bottom margin */
    }
    
    .custom-box {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 1px;
        padding: 1px;
        margin-bottom: 1px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    }

    .stSelectbox, .stNumberInput {
        margin-bottom: 1px; /* Adjust margin to control space below select boxes and number inputs */
    }
    
    .stButton>button {
        margin-top: 1px; /* Reduced top margin for button */
    }
    
    .result {
        font-size: 24px !important;
        font-weight: bold;
        color: #ffffff; /* Change this color to make it more prominent */
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_css()  # Apply custom CSS for spacing adjustments

    st.markdown("<h1 style='text-align: center; color: #333333;'>IPL Score Predictor 🏏</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='big-font'>Batting Team</p>", unsafe_allow_html=True)
        batting_team = st.selectbox('', sorted(teams), key='batting')

    with col2:
        st.markdown("<p class='big-font'>Bowling Team</p>", unsafe_allow_html=True)
        bowling_team = st.selectbox('', sorted(teams), key='bowling')

    st.markdown("<p class='big-font'>Match Venue</p>", unsafe_allow_html=True)
    city = st.selectbox('', sorted(cities), key='city')

    col3, col4, col5 = st.columns(3)

    with col3:
        st.markdown("<p class='big-font'>Current Score</p>", unsafe_allow_html=True)
        current_score = st.number_input('', min_value=0, max_value=500, step=1, key='score')

    with col4:
        st.markdown("<p class='big-font'>Overs Completed</p>", unsafe_allow_html=True)
        overs = st.number_input('', min_value=5.0, max_value=19.5, step=0.1, key='overs')

    with col5:
        st.markdown("<p class='big-font'>Wickets Fallen</p>", unsafe_allow_html=True)
        wickets = st.number_input('', min_value=0, max_value=9, step=1, key='wickets')

    st.markdown("<p class='big-font'>Runs scored in last 5 overs</p>", unsafe_allow_html=True)
    last_five = st.number_input('', min_value=0, max_value=100, step=1, key='last_five')

    if st.button('Predict Score', key='predict', help='Click to predict the score'):
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = current_score / overs

        input_df = pd.DataFrame({
            'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city,
            'current_score': [current_score], 'balls_left': [balls_left], 'wickets_left': [wickets_left],
            'crr': [crr], 'last_five': [last_five]
        })
        result = pipe.predict(input_df)
        st.markdown(f"<p class='result'>Predicted Score: {int(result[0])}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
