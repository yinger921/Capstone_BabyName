## Future Baby Names Prediction: Leveraging Famous Influences with Machine Learning
=========================

### Project Summary

#### Background
The project focuses on analyzing baby name trends in the United States, identifying the factors influencing these trends, and understanding their broader cultural, societal, and historical implications. Naming a child is a significant cultural act influenced by various factors, including gender ratios, cultural shifts, media influence, and historical events. By exploring these naming patterns, the project aims to reveal insights into how personal names reflect cultural narratives and societal values.

#### Data Insights
This project leverages historical baby name data to uncover patterns and predict future trends. It explores the impact of gender ratios, cultural phenomena, media influence, and historical events on the popularity of names. By developing predictive models and creating interactive visualizations, the project can provide valuable insights for parents, marketers, sociologists, and policymakers, aiding in decision-making and understanding cultural trends.

#### Key takeaways
Names like "Elizabeth" have shown consistent popularity, demonstrating timeless appeal.

Male names exhibit more rapid changes in popularity compared to female names, which suggests differing cycles of name popularity influenced by various social and cultural factors.

Prominent figures and media, such as Elon Musk and Game of Thrones, significantly impact baby name trends.

The analysis of gender ratios, national ratios, and name counts provides different perspectives on naming trends and their practical applications, such as targeted marketing and understanding cultural significance.

### Demo

#### Data Visualizations:
Visualizations include trend lines showing the popularity of specific names over time, gender ratio analysis across different states, and the impact of cultural phenomena on name popularity.

#### Interactive App:\
A web-based app (using streamlit or a similar platform) will serve as an interactive demo. This app will allow users to explore naming trends by state, year, gender, and other demographics. 

Key features of the app include:

Filtering and Exploration: Users can filter data by state, gender, and time period to see how baby name popularity changes across different regions and over time.

Trend Analysis: Visualizations showing trends in name popularity, the impact of famous personalities on naming choices, and the influence of media events.

Predictive Features: The app will include predictive models that forecast future baby name trends based on historical data and current influencing factors.


### Methodology
... High-level diagrams of entire process:

... Data Processing Steps:

Data Cleaning: Handling missing values, correcting errors, and standardizing data formats.

Data Aggregation: Grouping data by year, gender, state, and name for trend analysis.

Feature Engineering: Creating new features such as gender ratios and national popularity ratios.

... Modeling Directions:

Time Series Analysis: To forecast future name trends based on historical data.

Regression Models: To understand the relationship between external factors (e.g., economic indicators, media events) and name popularity.

... Prototyping Directions:

Interactive Visualizations: Building dashboards for users to explore data.

Predictive Models: Developing models to forecast future trends.

Web-based Apps: Creating a user-friendly interface for real-time interaction with the data.


### Organization

#### Repository 


* `model`
    - `joblib` dump of final model(s)
* `streamlit`
    - contains python file to demo the app

* `notebooks`
    - contains all model notebooks involved in the project and data

* `docs`
    - contains final report, presentations which summarize the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda.yml`
    - Conda environment specification

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

#### Dataset

... [Google Drive links to datasets and pickled models](https://drive.google.com/drive/folders/1grMuoCSioozmk6MBnLWtH8v2by4OBfEA Date in google drive)

### Credits

... Include any personal learning

This project deepened understanding of how cultural, social, and media factors influence naming trends. Insights into predictive modeling and visualization techniques were also gained.
