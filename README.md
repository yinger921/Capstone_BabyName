# Future Baby Names Prediction: Leveraging Famous Influences with Machine Learning

## Project Summary

### Background
The Future Baby Names Prediction project leverages historical baby name data from the United States to uncover trends and predict future naming patterns. The cultural act of naming a child is influenced by various factors such as gender ratios, media influences, and historical events. This project aims to provide insights into how names mirror cultural and societal shifts.

### Data Insights
Using historical data, the project identifies key patterns and influences on baby name trends. It uncovers the role of gender, media, and historical events in shaping name popularity. The predictive models and interactive visualizations serve as tools for parents, marketers, sociologists, and policymakers to understand these trends better.

**Key Takeaways**:
- Timeless names like "Elizabeth" maintain consistent popularity across decades.
- Male names tend to fluctuate in popularity more rapidly than female names, potentially reflecting different cultural cycles.
- Influences such as media figures and pop culture (e.g., Elon Musk, Game of Thrones) can significantly sway naming trends.
- Gender and state demographics offer useful perspectives for targeted marketing and sociological analysis.

### Project Demo

#### Data Visualizations
The project offers several interactive visualizations:
- **Trend Lines**: Tracking the popularity of specific names over time.
- **Gender Ratio Analysis**: Explore the differences in name trends by gender across various states.
- **Cultural Impact**: See how major media events or figures have influenced baby names.

#### Interactive Web Application
An interactive web app (developed with Streamlit) allows users to explore these naming trends across different parameters. 

**Features**:
- **Filtering & Exploration**: Filter by state, gender, time period, and see how trends vary regionally and temporally.
- **Trend Analysis**: Visualize trends in name popularity and explore the impact of celebrities and cultural moments.
- **Predictive Capabilities**: Forecast future name trends based on historical data and contemporary influences.

### Methodology

#### Data Processing
The project's methodology includes the following steps:
1. **Data Cleaning**: Handle missing values, correct inconsistencies, and standardize formats.
2. **Data Aggregation**: Group data by year, gender, state, and name for better trend analysis.
3. **Feature Engineering**: Create features like gender ratios and national popularity scores for deeper analysis.

#### Modeling Approach
1. **Time Series Models**: Predict future baby name trends using historical data.
2. **Regression Models**: Assess the impact of factors such as economic indicators and media events on name popularity.
3. **Clustering & Decision Trees**: Cluster popular names and analyze their characteristics using decision trees.

#### Prototyping
- **Interactive Visualizations**: Developed dashboards and visual tools for users to explore data.
- **Predictive Models**: Built models that forecast name trends based on various cultural influences.
- **Web-based Application**: Implemented a user-friendly web interface for real-time exploration and interaction.

### Repository Organization

The repository is structured as follows:

- **model/**: Includes the trained machine learning models in `joblib` format.
- **streamlit/**: Contains the Streamlit app code for the interactive demo.
- **notebooks/**: Jupyter notebooks used during the development and experimentation phases.
- **docs/**: Reports and presentations summarizing the project.
- **references/**: Academic papers, tutorials, and resources consulted during the project.
- **src/**: Data information.
- **datasets/**: If applicable, smaller datasets used for testing.
- **.gitignore**: Configuration for ignored files.
- **conda.yml**: Conda environment specification for setting up dependencies.
- **README.md**: This document.
- **LICENSE**: The project’s license.

### Dataset Information

The datasets used in this project, as well as the trained models, can be accessed via the following [Google Drive folder](https://drive.google.com/drive/folders/1grMuoCSioozmk6MBnLWtH8v2by4OBfEA).

### Credits & Learning

This project significantly deepened my understanding of the influence of culture, media, and societal changes on naming trends. It also enhanced my skills in predictive modeling and data visualization, particularly using Python, Streamlit, and machine learning tools.

