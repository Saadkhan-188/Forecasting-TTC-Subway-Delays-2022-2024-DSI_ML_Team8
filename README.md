# TTC Subway Delay Forecasting & Prevention

## Contents

* [Overview](#overview)
* [Learning Outcomes](#learning-outcomes)
* [Getting Started](#getting-started)

  * [Key Contacts](#key-contacts)
  * [Module Delivery & Expectations](#module-delivery--expectations)
  * [Schedule](#schedule)
* [Instructions (How to Work on the Project)](#instructions-how-to-work-on-the-project)

  * [How to Pick a Dataset](#how-to-pick-a-dataset)
  * [Reviewing Your Dataset](#reviewing-your-dataset)
  * [Folder Structure & Repo Setup](#folder-structure--repo-setup)
  * [Tips for Working as a Team](#tips-for-working-as-a-team)
* [Submitting Your Project](#submitting-your-project)

  * [Submission & Evaluation](#submission--evaluation)
  * [Project Showcase](#project-showcase)
  * [How to Present Your Work](#how-to-present-your-work)
* [Getting Help](#getting-help)

  * [Troubleshooting & FAQs](#troubleshooting--faqs)
  * [Additional Resources](#additional-resources)
* [Other Resources](#other-resources)

## Overview

The TTC subway system experiences frequent service disruptions, yet there is no accessible tool to forecast or prevent them. Our team used historical TTC subway delay data (2014–2025) to analyze trends, model future risk, and recommend preventative operational strategies.

This project answers:

* When and where do subway delays most frequently occur?
* Can we predict days with unusually high numbers of delays?
* What patterns in incident type, location, and time can inform preventative action?

## Learning Outcomes

By the end of this module, our team was able to:

1. Apply multiple data science techniques including regression, classification, time-based analysis, and feature engineering.
2. Build a portfolio-ready machine learning pipeline using real operational data.
3. Develop clean, modular code and structured notebooks with interpretable insights.
4. Communicate complex findings through reproducible reports, visualizations, and a stakeholder-facing README.
5. Collaborate effectively using GitHub branches, pull requests, and team role clarity.

## Getting Started

### Key Contacts

**Team:**

* **Val Poon** – Project Manager, Documentation
* **Sucharita Sundaraman** – Modeling, Reporting
* **Sneha Gupta** – Modeling, Reporting
* **Sahil Modi** – Data Cleaning, EDA
* **Saad Khan** – Data Cleaning, EDA

**Support:**

* [DSI Instructional Team](https://mail.utoronto.ca)

### Module Delivery & Expectations

This project spans 2 weeks. Week 1 focused on data wrangling, EDA, and feature engineering. Week 2 focused on modeling, recommendations, and final presentation prep. Each team member submitted code, contributed to analysis, and recorded a reflection video.

### Schedule

| Day     | Milestone                                           |
| ------- | --------------------------------------------------- |
| Day 1–2 | Team kickoff, dataset selected, roles assigned      |
| Day 3–5 | EDA, data cleaning, merged dataset created          |
| Day 6–7 | Modeling (logistic regression), feature engineering |
| Day 8–9 | Final visualizations, README, and slides            |
| Day 10  | Presentation + video submissions                    |

## Instructions (How to Work on the Project)

### How to Pick a Dataset

We selected the [TTC Subway Delay dataset](https://open.toronto.ca/dataset/ttc-subway-delay-data/) because it is:

* Public and well-documented
* Time-series based
* Relevant to Toronto residents and city operations

### Reviewing Your Dataset

* Key variables include: date, time, station, delay cause, delay duration, and line.
* We identified relationships between time-of-day, location, and frequency.
* Delay types (codes) were mapped using an auxiliary Excel file.

### Folder Structure & Repo Setup

```
📦 ttc-subway-delay-project
├── data/
│   ├── raw/                # Original Excel/CSV files
│   ├── processed/          # Cleaned, merged CSV
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   └── 02_model_logistic_regression.ipynb
├── models/                 # Trained model files (optional)
├── reports/
│   └── figures/            # Visualizations for slides
├── src/                    # Helper scripts
├── team/                   # Reflection videos
├── README.md
└── .gitignore
```

## Submitting Your Project

### Submission & Evaluation

We followed best practices with GitHub commits, branches, and pull requests. Our repo contains:

* Cleaned dataset with over 150,000 entries
* Notebook with EDA, charts, and time-based aggregation
* Logistic regression model with precision, recall, and feature importance
* Team reflection videos

### Project Showcase

Our final presentation included:

* Key business problem
* Stakeholder persona (TTC operations team)
* Reproducible findings (charts, metrics)
* ML model predicting high-delay days
* Recommendations for preventative measures (station, cause, peak hour-based)

## Getting Help

We referenced:

* Slack help channels
* GitHub Copilot & ChatGPT for syntax and logic checks
* Public transit documentation (Toronto Open Data portal)

## Other Resources

* [Open TTC Dataset](https://open.toronto.ca/dataset/ttc-subway-delay-data/)
* [Scikit-learn documentation](https://scikit-learn.org/)
* [Seaborn API](https://seaborn.pydata.org/api.html)
* [DSI Git & teamwork resources](https://github.com/uoft-dsi)

---

This README reflects the lived collaboration and problem-solving of our team. We're proud of what we built, and we hope others can build on it too.
