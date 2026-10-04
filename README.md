# 🎬 Netflix Content Intelligence

An exploratory data analysis and interactive Streamlit dashboard for analyzing Netflix Movies and TV Shows.

The project explores Netflix's content library through data cleaning, feature engineering, statistical analysis, visualizations, and an interactive dashboard.

---

## 📌 Project Overview

Netflix has a large collection of Movies and TV Shows with different ratings, release years, genres, and content addition patterns.

This project performs Exploratory Data Analysis (EDA) to understand:

- Distribution of Movies and TV Shows
- Content ratings
- Release year patterns
- Content added to Netflix over time
- Relationship between content type and other variables
- Monthly and yearly content addition trends

An interactive Streamlit dashboard is also included to explore the dataset using filters and visualizations.

---

## 🗂️ Project Structure

```text
Netflix-Content-Intelligence/
│
├── dashboards/
│   └── app.py
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── netflix_eda.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```
## 📊 Dataset

The project uses the **Netflix Movies and TV Shows** dataset.

The dataset contains information such as:

- Show ID
- Content Type
- Title
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Genres
- Description

### Dataset Source

Kaggle:  
https://www.kaggle.com/padmapriyatr/netflix-titles

The dataset is also included in this repository at:

`data/netflix_titles.csv`

---

## 🔍 Exploratory Data Analysis

The EDA notebook follows these stages:

1. Import Libraries
2. Load Dataset
3. Dataset Overview
4. Missing Values Analysis
5. Duplicate Analysis
6. Data Cleaning
7. Feature Engineering
8. Univariate Analysis
9. Bivariate Analysis
10. Multivariate Analysis
11. Time-Based Analysis
12. Key Insights
13. Final Conclusion

---

## 📈 Dashboard

The project includes an interactive **Streamlit dashboard** with:

- Content Type Distribution
- Rating Distribution
- Release Year Analysis
- Content Added Over Time
- Top Genres
- Search by Title
- Content Type Filter
- Rating Filter
- Release Year Filter
- Title Details

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit

---

