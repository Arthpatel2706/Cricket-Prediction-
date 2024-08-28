import streamlit as st
import pre_app
import app

def set_page_config():
    st.set_page_config(page_title="IPL Predictor", page_icon="🏏", layout="wide")

def apply_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #ffffff;
    }
    
    .medium-font {
        font-size: 18px !important;
        color: #ffffff;
    }
    
    .custom-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 20px;
        backdrop-filter: blur(10px);
    }
    
    .custom-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 5px;
        border: none;
    }
    
    .custom-button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

def show_home_page():
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>Welcome to IPL Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<p class='medium-font' style='text-align: center;'>Choose your prediction type</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class='custom-box'>
                <h3 style='text-align: center; color: #ffffff;'>🏏 Score Prediction</h3>
                <p style='text-align: center; color: #ffffff;'>Predict the first inning score of an IPL match</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button('Score Prediction', key='score_pred', help='Click to predict match scores'):
            st.session_state.page = 'score_prediction'
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class='custom-box'>
                <h3 style='text-align: center; color: #ffffff;'>🏆 Win Prediction</h3>
                <p style='text-align: center; color: #ffffff;'>Predict the winning probability of teams</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button('Win Prediction', key='win_pred', help='Click to predict match winners'):
            st.session_state.page = 'win_prediction'
            st.rerun()

def main():
    set_page_config()
    apply_custom_css()

    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    # Sidebar for navigation
    with st.sidebar:
        st.markdown("<h2 style='text-align: left; color: #000000;'>Navigation</h2>", unsafe_allow_html=True)
        if st.button('🏠 Home', key='home', help='Go to Home'):
            st.session_state.page = 'home'
            st.rerun()

    # Display the selected page
    if st.session_state.page == 'home':
        show_home_page()
    elif st.session_state.page == 'score_prediction':
        pre_app.main()
    elif st.session_state.page == 'win_prediction':
        app.main()

if __name__ == "__main__":
    main()