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

## 🚀 Run the Project Locally

Step 1: Clone the Repository

     git clone https://github.com/kadintimitravinda/Netflix-Content-Intelligence.git

Step 2: Navigate to the Project Directory

     cd Netflix-Content-Intelligence

Step 3: Create a Virtual Environment

    python -m venv venv

Step 4: Activate the Virtual Environment

    .\venv\Scripts\Activate.ps1

Step 5: Install Required Dependencies

    pip install -r requirements.txt

Step 6: Run the Streamlit Dashboard

    streamlit run dashboards/app.py

The dashboard will open at:    http://localhost:8501

---

## 💡 Key Insights

The analysis provides insights into:

 - Netflix's distribution of Movies and TV Shows
 - Popular content ratings
 - Release-year distribution
 - Differences between Movies and TV Shows
 - Year-wise content additions
 - Monthly content addition patterns

---

## 👩‍💻 Author

Kadintimitravinda

AI & Data Science Student at
Vishnu Institute of Technology

GitHub:  https://github.com/kadintimitravinda

---
