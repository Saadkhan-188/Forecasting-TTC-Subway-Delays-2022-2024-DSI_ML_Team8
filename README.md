# 🚇 TTC Subway Delay Data Analysis – DSI\_ML\_Team8

We’re exploring **three years** of Toronto’s TTC subway delay logs (2022–2024) to uncover patterns, build predictive models, and offer real-world recommendations — helping transit agencies gain foresight to take preventative operational measures against recurring delays and commuters plan smarter.

📁 [Dataset Source (Open Data Toronto)](https://open.toronto.ca/dataset/ttc-subway-delay-data/)

---

## Table of Contents

* [Problem Context](#problem-context)
* [Learning Outcomes](#learning-outcomes)
* [Dataset Summary](#dataset-summary)
* [Industry Context](#industry-context)
* [Value Proposition](#value-proposition)
* [Tools & Libraries](#tools--libraries)
* [Getting Started](#getting-started)
* [Schedule and Project Plan](#schedule-and-project-plan)
* [Team Members](#team-members)
* [Analytical Plan](#analytical-plan)
* [Known Risks](#known-risks)
* [Folder Structure](#folder-structure)
* [Project Facilitators](#project-facilitators)
* [Other Resources](#other-resources)

---

## Problem Context

Toronto commuters frequently express frustration with unpredictable TTC subway delays — citing long wait times, vague announcements, and inconsistent communication. These complaints surface across Reddit threads, Twitter posts, local news outlets, and formal transit surveys. A 2024 Reddit analysis reported over **23,000 logged subway delays** in a single year ([source](https://www.reddit.com/r/toronto/comments/10b3otc/ttc_delay_data_analysis_2023/)), while Line 1 alone serves over **625,000 daily riders** ([Wikipedia](https://en.wikipedia.org/wiki/Line_1_Yonge%E2%80%93University)). Councillors and passengers alike have called for better coordination and predictive support during rush hours ([CBC](https://www.cbc.ca/news/canada/toronto/ttc-delay-frustration-riders-councillors-1.7139906)).

This project addresses that pain point by analyzing three years of TTC delay data (2022–2024) to uncover delay patterns and build both classification and regression models — predicting delay severity and duration with the goal of enabling faster operator response and better rider information systems, and surface insights that could inform both TTC operations and trip planning for riders.

---

## Learning Outcomes

By the end of this sprint, we aim to:

1. Apply technical skills across EDA, regression, classification modeling, and Git collaboration
2. Build a portfolio-ready, reproducible data science project
3. Work collaboratively using GitHub, Notion, and Slack
4. Communicate results clearly through a README, visualizations, and a final presentation

---

## Dataset Summary

* **Dataset**: [TTC Subway Delay Data](https://open.toronto.ca/dataset/ttc-subway-delay-data/)
* **Publisher**: Toronto Transit Commission
* **Years Covered**: 2022–2024 (\~50,000 rows)
* **Last Refreshed**: June 30, 2025
* **Contents**: Monthly delay logs across subway lines, including time, location, duration, and delay cause
* **Objective**: Generate a reproducible machine learning pipeline for delay trend analysis and prediction

---

## Industry Context

Urban transit systems around the world are adopting predictive analytics to improve reliability. TTC, serving millions in Toronto, logs frequent subway delays. By using historical delay data, this project explores how machine learning can enable smarter scheduling, early warnings, and better-informed operational decisions.

---

## Value Proposition

* Help TTC operators anticipate and reduce severe delays using pattern recognition
* Equip riders and route planners with earlier, more accurate delay predictions
* Provide a generalizable ML pipeline that could support other transit systems worldwide
* Demonstrate how open government datasets can power transparent, community-benefiting ML use cases anticipate and reduce severe delays using pattern recognition
* Equip riders and route planners with earlier, more accurate delay predictions
* Provide a generalizable ML pipeline that could support other transit systems worldwide

---

## Tools & Libraries

This project is built entirely in **Python**, using a combination of core libraries and open-source tools:

We use:

* `pandas`, `numpy`, `matplotlib`, `seaborn`
* `scikit-learn` and `xgboost` for modeling
* `SHAP` (in progress) for model explainability
* GitHub for version control
* Slack, Notion, Trello for team coordination

---

## Getting Started

This is a 10-day team sprint running from **July 17 to July 26, 2025**. All work is tracked on GitHub and Trello with async check-ins.

---

## Schedule and Project Plan

| Date       | Phase                     | Key Goals                                               | Owner(s)      |
| ---------- | ------------------------- | ------------------------------------------------------- | ------------- |
| July 17    | Kickoff & Planning        | Finalize dataset, roles, create repo and README         | Everyone      |
| July 18–19 | EDA & Feature Engineering | Clean data, engineer time/line features                 | Saad, Sahil   |
| July 21    | Modeling (2024 only)      | Train XGBoost + Random Forest on cleaned 2024 data      | Sneha, Suchi  |
| July 22    | SHAP + Regression         | Faiz: SHAP (w/ Sneha), Suchi: regression on `Min Delay` | Faiz, Suchi   |
| July 23    | Clean All Years           | Merge cleaned 2022 (Sahil), 2023 (Saad), 2024 (Sneha)   | Team          |
| July 24    | Model All Years           | Retrain models using full 2022–2024 dataset             | Sneha, Suchi  |
| July 25    | README & Polishing        | Finalize charts, summaries, push repo                   | Val, Everyone |
| July 26    | Final Presentation        | Present findings + submit final repo                    | Everyone      |

---

## Team Members

| Name                    | GitHub Handle                                    | Email                                                     | Contributions                           | Reflection Video |
| ----------------------- | ------------------------------------------------ | --------------------------------------------------------- | --------------------------------------- | ---------------- |
| Valerie Poon            | [@val-poon](https://github.com/val-poon)         | [valerieyfp@gmail.com](mailto:valerieyfp@gmail.com)       | PM, reporting, folder structure setup, documentation  | *TBD*            |
| Sahil Modi              | [@smodi23](https://github.com/smodi23)           | [sahilmodi237@gmail.com](mailto:sahilmodi237@gmail.com)   | 2022 data cleaning, EDA                 | *TBD*            |
| Saad Khan               | [@Saadkhan-188](https://github.com/Saadkhan-188) | [saadkhan188@gmail.com](mailto:saadkhan188@gmail.com)     | 2023 data cleaning, EDA                 | *TBD*            |
| Sneha Gupta             | [@reachsneha02](https://github.com/reachsneha02) | [reachsneha02@gmail.com](mailto:reachsneha02@gmail.com)   | 2024 model training, visualizations     | *TBD*            |
| Sucharitha Sundararaman | [@suchi-dev-ai](https://github.com/suchi-dev-ai) | [suchiraman22@gmail.com](mailto:suchiraman22@gmail.com)   | Regression modeling                     | *TBD*            |
| Faiz Shaikh             | [@FaizS11](https://github.com/FaizS11)           | [faizkshaikh11@gmail.com](mailto:faizkshaikh11@gmail.com) | SHAP + model explainability             | *TBD*            |

---

## Analytical Plan

We use three years of historical TTC subway delay data (2022–2024) to:

1. Clean and normalize noisy inputs (station names, line names, delay codes)
2. Engineer new features including `Min Gap`, `Hour`, and `Code Frequency`
3. Train classification models (XGBoost, Random Forest) to predict delay severity (`Delay_Class`)
4. Train regression models to predict delay length in minutes (`Min Delay`)
5. Evaluate performance using accuracy, macro-averaged F1 score (classification), and MAE/RMSE (regression)
6. Use SHAP for explainability to understand which features most influence predictions

---

## Known Risks

* **Data Imbalance**: Long delays represent <1% of samples — mitigated by classification tuning and SMOTE (TBD)
* **Messy Labels**: Inconsistent `Line` and `Code` fields required extensive mapping
* **Model Interpretability**: SHAP integration pending due to library complexity
* **Missing Context**: Some delays may reflect multi-modal issues (e.g. bus–subway interface), which are not modeled

---

## Folder Structure

```
DSI_ML_Team8/
data/
│   raw/         # Unmodified source data
│   processed/   # Cleaned and engineered datasets
│   external/    # External reference files
notebooks/       # Jupyter notebooks for EDA and modeling
models/          # Serialized models and performance metrics
visuals/         # Charts and figures for reporting and slides
reports/         # Final presentations, summaries, and documentation
src/             # Python scripts and feature engineering tools
.gitignore
README.md
```

---

## Project Facilitators

| Role             | Name              | Email                                                                       |
| ---------------- | ----------------- | --------------------------------------------------------------------------- |
| Tech Facilitator | Phil Van-Lane     | [phil.vanlane@mail.utoronto.ca](mailto:phil.vanlane@mail.utoronto.ca)       |
| Learning Support | Aditya Kulkarni   | [aditya.kulkarni@mail.utoronto.ca](mailto:aditya.kulkarni@mail.utoronto.ca) |
| Learning Support | Ernani Fantinatti | [ernanif@fantinatti.com](mailto:ernanif@fantinatti.com)                     |
| Learning Support | Laura MacKew      | [lauramackew@gmail.com](mailto:lauramackew@gmail.com)                       |

---

## Other Resources

* [Team Trello (Kanban & Docs)](https://trello.com/invite/b/68784cb94b65902aba3eaf1b/ATTI02762885d9b118c31ccbfa7dacd1992b7739A217/🚇-our-1-week-ttc-delay-ml-mission)
* [Slack Channel – DSI Certificate Program](https://uoft-dsi-certificates.slack.com/archives/C096UPGDKA4)
