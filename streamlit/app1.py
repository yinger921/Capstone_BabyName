import streamlit as st
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load your data
file_path = '/Users/yingzhou/Downloads/Capstone_Babyname/notebooks/data.csv'

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path, index_col=0)

data= data.sort_values(by=['Name', 'Year']) 

# Function to plot name metrics over time with year filter
def plot_name_trend_filtered(data, names, metric, gender, title, ylabel, start_year, end_year):
    # Filter data for the specified year range
    filtered_data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]
    
    plt.figure(figsize=(14, 10))

    for name in names:
        name_data = filtered_data[(filtered_data['Name'] == name) & (filtered_data['Gender'] == gender)]
        plt.plot(name_data['Year'], name_data[metric], marker='o', label=name)

    plt.title(f'{title} Over Time ({gender}) from {start_year} to {end_year}', fontsize=20)
    plt.xlabel('Year', fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    plt.legend(title='Name', fontsize=18)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

# Streamlit app
st.title("Baby Name Trends")

# User inputs
names_input = st.text_input("Enter names (comma-separated):", "Bill, Elon")
start_year_input = st.number_input("Enter start year:", min_value=1880, max_value=2023)
end_year_input = st.number_input("Enter end year:", min_value=1881, max_value=2023)
gender_input = st.selectbox("Select gender:", options=['M', 'F'])

# Process input
names_to_plot = [name.strip() for name in names_input.split(',')]

# Define the year range for the plot
start_year = start_year_input 
end_year = end_year_input

# Plotting
if st.button("Show Trend"):
    plot_name_trend_filtered(
       data,
        names_to_plot,
        'Gender_Name_Ratio',  
        gender_input,
        'Gender Name Permille Ratio',
        'Permille Ratio',
        start_year,
        end_year
    )

    
    
    
# Load the saved logistic regression model
def load_model():
    return joblib.load('../models/logistic_model.pkl')

log_reg_model = load_model()


# Load the saved preprocessor model
def preprocessor_model():
    return joblib.load('../models/preprocessor.pkl')

preprocessor_model = preprocessor_model()


# Streamlit app title
st.title("Baby Name Prediction")

# Function to get user input
def user_input_features():
    Year = st.slider("Year", 1880, 2024, 2020)
    Is_Famous = st.selectbox("Is the Name Famous? (1 = Yes, 0 = No)", [0, 1])
    Gender_Binary = st.selectbox("Gender (1 = Male, 0 = Female)", [0, 1])
    Rolling_Average_Gender_Ratio_5_Years = st.number_input("Rolling Average Gender Ratio (5 Years)", min_value=0.0, max_value=1000.0, value=0.5)
    Vowel_Count = st.slider("Number of Vowels", 0, 10, 3)
    Ends_With_Specified_Letters = st.selectbox("Ends with Specified Letters (1 = Yes, 0 = No)", [0, 1])

    data = {
        'Year': Year - 1880,
        'Is_Famous': Is_Famous,
        'Gender_Binary': Gender_Binary,
        'Rolling_Average_Gender_Ratio_5_Years': Rolling_Average_Gender_Ratio_5_Years,
        'Vowel_Count': Vowel_Count,
        'Ends_With_Specified_Letters': Ends_With_Specified_Letters
    }
    features = pd.DataFrame([data])
    return features

# Get user input
input_df = user_input_features()

# Apply the preprocessor
input_transformed = preprocessor_model.transform(input_df)


# Make predictions
prediction = log_reg_model.predict(input_transformed)[0]
probability = log_reg_model.predict_proba(input_transformed)[0][1]

# Display results
st.subheader("Prediction Results")
if prediction == 1:
    st.write(f"The name is predicted to be **in** the Top 100.")
else:
    st.write(f"The name is predicted to be **not in** the Top 100.")

st.write(f"Probability of being in the Top 100: **{probability:.3f}**")

