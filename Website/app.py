import streamlit as st
import pickle
import pandas as pd

# Load model
pipe = pickle.load(open('GradientBoosting_for_Winning.pkl', 'rb'))

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

    .result-progress {
        font-size: 18px !important;
        font-weight: bold;
        color: #333333;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_css()  # Apply custom CSS for styling

    st.markdown("<h1 style='text-align: center; color: #333333;'>IPL Win Predictor 🏆</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<p class='big-font'>Batting Team</p>", unsafe_allow_html=True)
        batting_team = st.selectbox('', sorted(teams), key='batting')

    with col2:
        st.markdown("<p class='big-font'>Bowling Team</p>", unsafe_allow_html=True)
        bowling_team = st.selectbox('', sorted(teams), key='bowling')

    st.markdown("<p class='big-font'>Match Venue</p>", unsafe_allow_html=True)
    selected_city = st.selectbox('', sorted(cities), key='city')

    st.markdown("<p class='big-font'>First Innings Total</p>", unsafe_allow_html=True)
    first_innings_total = st.number_input('', min_value=0, step=1, key='first_innings_total')

    col3, col4, col5 = st.columns(3)

    with col3:
        st.markdown("<p class='big-font'>Current Score</p>", unsafe_allow_html=True)
        score = st.number_input('', min_value=0, step=1, key='score')

    with col4:
        st.markdown("<p class='big-font'>Overs Completed</p>", unsafe_allow_html=True)
        overs = st.number_input('', min_value=0.0, max_value=19.5, step=0.1, key='overs')

    with col5:
        st.markdown("<p class='big-font'>Wickets Fallen</p>", unsafe_allow_html=True)
        wickets = st.number_input('', min_value=0, max_value=9, step=1, key='wickets')

    if st.button('Predict Win Probability', key='predict', help='Click to predict win probability'):
        runs_left = first_innings_total - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
            'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets_left': [wickets_left],
            'first_innings_total': [first_innings_total], 'crr': [crr], 'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        batting_team_prob = result[0][1]
        bowling_team_prob = result[0][0]

        st.markdown(f"<p class='result'>Win Probability:</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='result'>{batting_team}: {batting_team_prob:.2%}</p>", unsafe_allow_html=True)
        st.progress(batting_team_prob)
        st.markdown(f"<p class='result'>{bowling_team}: {bowling_team_prob:.2%}</p>", unsafe_allow_html=True)
        st.progress(bowling_team_prob)

if __name__ == "__main__":
    main()
