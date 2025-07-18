# 🚇 TTC Subway Delay Data Analysis – DSI_ML_Team8

Analyzing transit delay trends from Toronto’s TTC Subway Delay dataset to uncover actionable insights, build a predictive model, and explore strategies for improving urban mobility.

📁 [Dataset Source (Open Data Toronto)](https://open.toronto.ca/dataset/ttc-subway-delay-data/)

---

## Table of Contents

- [Overview](#overview)
- [Learning Outcomes](#learning-outcomes)
- [Project Overview](#project-overview)
- [Tools & Libraries](#tools--libraries)
- [Getting Started](#getting-started)
- [Schedule and Project Plan](#schedule-and-project-plan)
- [Team Members](#team-members)
- [Folder Structure](#folder-structure)
- [Project Facilitators](#project-facilitators)
- [Other Resources](#other-resources)

---

## Overview

This project explores the [TTC Subway Delay Data](https://open.toronto.ca/dataset/ttc-subway-delay-data/) provided by the Toronto Transit Commission. By applying machine learning techniques and visual analytics, our team will identify patterns and potential predictive signals for subway delays, focusing on time-based features and operational categories.

---

## Learning Outcomes

By the end of this sprint, we aim to:

1. Apply technical skills across EDA, regression, time series modeling, and Git collaboration  
2. Build a portfolio-ready, reproducible data science project  
3. Work collaboratively using GitHub, Notion, and Slack  
4. Communicate results clearly through a README, visualizations, and a final presentation

---

## Project Overview

- **Dataset**: [TTC Subway Delay Data](https://open.toronto.ca/dataset/ttc-subway-delay-data/)
- **Publisher**: Toronto Transit Commission  
- **Last Refreshed**: June 30, 2025  
- **Description**: Monthly delay logs across TTC subway lines including time, location, delay cause, duration, and other metadata  
- **Goal**: Identify delay trends, engineer time-based features, and evaluate predictive models for delay classification or duration estimation

---

## Tools & Libraries

We expect to use:

- [`pandas`](https://pandas.pydata.org/) for data manipulation  
- [`numpy`](https://numpy.org/) for numerical operations  
- [`scikit-learn`](https://scikit-learn.org/) for modeling  
- [`matplotlib`](https://matplotlib.org/) and [`seaborn`](https://seaborn.pydata.org/) for visualization  
- [`Prophet`](https://facebook.github.io/prophet/) or [`statsmodels`](https://www.statsmodels.org/stable/index.html) for time series (TBD)  
- [`SHAP`](https://shap.readthedocs.io/en/latest/) for explainability (optional)  
- [GitHub](https://github.com/) for version control  
- [Slack](https://slack.com/) for async communication  
- [Notion](https://www.notion.so/DSI-ML-Team-8-233898e03e6b80b5af9cd0be21df8599) for documentation & Kanban  

Reflection videos will be linked in this README.

---

## Getting Started

This is a 10-day team sprint running from **July 17 to July 26, 2025**. All work will be documented in GitHub, with daily async check-ins on Slack and Notion.

---

## Schedule and Project Plan

| Date       | Phase                   | Key Goals                                                       | Owner(s)                                                                                                                                   |
|------------|-------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| July 17    | Kickoff & Planning      | Finalize dataset, roles, create repo, draft README               | Everyone, [@val-poon](https://github.com/val-poon)                                                                                   |
| July 18–19 | EDA & Feature Engineering | Complete EDA, preprocess, create time-based features             | [@Saadkhan-188](https://github.com/Saadkhan-188), [@smodi23](https://github.com/smodi23)                                                   |
| July 21    | Modeling                | Train & evaluate logistic regression baseline                    | [@reachsneha02](https://github.com/reachsneha02), [@suchi-dev-ai](https://github.com/suchi-dev-ai)                                        |
| July 22    | Visualizations & Recs  | Build charts, identify key trends, draft insights                | [@reachsneha02](https://github.com/reachsneha02), [@suchi-dev-ai](https://github.com/suchi-dev-ai)                                        |
| July 23    | README + Reporting     | Finalize README, visual assets, and insight write-up/ slide deck             | [@val-poon](https://github.com/val-poon)                                                                                            |
| July 24    | Slides + Reflection Videos | Record 3–5 min videos + upload             | Everyone                                                                                                                                   |
| July 25    | Final Touches          | Polish notebooks, test reproducibility, push final GitHub repo   | Everyone                                                                                                                                   |
| July 26    | Final Presentation     | Present findings to cohort                                       | Everyone                                                                                                                                   |



---

## Team Members

| Name                    | GitHub Handle     | Email                        | Role               | Reflection Video |
|-------------------------|------------------|------------------------------|--------------------|------------------|
| Valerie Poon            | @val-poon         | valerieyfp@gmail.com         | PM, Reporting      | _TBD_            |
| Saad Khan               | @saadkhan-dsi     | saadkhan188@gmail.com        | Analyst            | _TBD_            |
| Sahil Modi              | @sahilmodi-ml     | sahilmodi237@gmail.com       | Analyst            | _TBD_            |
| Sneha Gupta             | @sneha-gupta-ml   | reachsneha02@gmail.com       | Modeling           | _TBD_            |
| Sucharitha Sundararaman| @sucharitha-s     | Suchiraman22@gmail.com       | Modeling           | _TBD_            |
| Faiz Shaikh             | _TBD_             | _TBD_                        | TBD (away)         | _TBD_            |

---

## Folder Structure

```
DSI_ML_Team8/
├── data/
│   ├── raw/         # Unmodified source data
│   ├── processed/   # Cleaned and engineered datasets
│   └── external/    # External reference files
├── notebooks/       # Jupyter notebooks for EDA and modeling
├── models/          # Serialized models and performance metrics
├── visuals/         # Charts and figures for reporting and slides
├── reports/         # Final presentations, summaries, and documentation
├── src/             # Python scripts and feature engineering tools
├── .gitignore
└── README.md
```


---

## Project Facilitators

| Role                 | Name              | Email                              |
|----------------------|-------------------|-------------------------------------|
| Tech Facilitator     | Phil Van-Lane     | phil.vanlane@mail.utoronto.ca      |
| Learning Support     | Aditya Kulkarni   | aditya.kulkarni@mail.utoronto.ca   |
| Learning Support     | Ernani Fantinatti | ernanif@fantinatti.com             |
| Learning Support     | Laura MacKew      | lauramackew@gmail.com              |

---

## Other Resources

- [Team Notion Workspace (Kanban & Docs)](https://www.notion.so/DSI-ML-Team-8-233898e03e6b80b5af9cd0be21df8599)
- [Slack Channel – DSI Certificate Program](https://uoft-dsi-certificates.slack.com/archives/C096UPGDKA4)

---

