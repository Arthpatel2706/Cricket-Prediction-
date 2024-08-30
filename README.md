# Cricket Analysis using EDA and Machine learning

This project aims to predict IPL match outcomes, including first-innings scores and match winners, using advanced machine learning models. The project involves data extraction, preprocessing, feature engineering, and model development, culminating in a user-friendly web application developed using Streamlit. The web app provides real-time predictions based on user input, offering valuable insights into IPL match dynamics.

**[Visit the Crickcast Website](https://crickcast.streamlit.app/)**

## Project Structure

### 1. IPL Data Folder
- **`IPL Data/`**: This folder contains all the raw and processed data used for building the predictive models.

### 2. Website Folder
- **`GradientBoosting_for_Winning.pkl`**: This is the trained Gradient Boosting model used for predicting match winners.
- **`Hyperperameter_pipe.pkl`**: This is the trained XGBoost model used for predicting first-innings scores.
- **`app.py`**: This script handles the "Winner Prediction" page on the website, where users can input match details and get predictions on the likely winner.
- **`main.py`**: This script is the homepage of the website, providing an entry point for users to navigate through the application.
- **`pre_app.py`**: This script manages the "Score Prediction" page on the website, where users can input match details and receive predictions on the expected first-innings score.

### 3. Jupyter Notebooks
- **`1.0 Common.ipynb`**: This notebook is the foundational file for both prediction tasks. It includes data extraction, data transformation, cleaning, exploratory data analysis (EDA), and common feature engineering steps.
- **`1.1 For Score Prediction.ipynb`**: This notebook is dedicated to building the machine learning model for score prediction. It includes task-specific feature engineering and model development.
- **`1.2 For Winner Prediction.ipynb`**: This notebook focuses on developing the machine learning model for predicting match winners. It includes task-specific feature engineering and model development.

### 4. Common Pickle File
- **`Common.pkl`**: This pickle file stores the processed data used in both the score prediction and winner prediction models, making it easier to load and use in the respective notebooks.

## How to Use

1. **Data Processing**: Start by exploring the `1.0 Common.ipynb` notebook to understand how the data was prepared for modeling.
2. **Model Development**: Use `1.1 For Score Prediction.ipynb` and `1.2 For Winner Prediction.ipynb` to see how the models were trained and evaluated for their respective tasks.
3. **Web Application**: The `Website` folder contains all necessary files to run the web application. Use `main.py` to launch the home page, and navigate to score and winner predictions via `pre_app.py` and `app.py` respectively.
