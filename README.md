# Forecasting TTC Subway Delays (2022–2024)

## Table of Contents

- [Problem Context](#problem-context)
- [Financial Impact](#financial-impact)
- [Objective](#objective)
- [Scope](#scope)
- [Sprint Timeline](#sprint-timeline)
- [Business Problem](#business-problem)
- [Dataset Source](#dataset-source)
- [Folder Structure](#folder-structure)
- [Methodology](#methodology)
  - [Data Cleaning](#data-cleaning)
  - [Feature Engineering](#feature-engineering-in-progress)
  - [Modeling](#modeling)
- [Key Signals (Preliminary)](#key-signals-preliminary)
- [Risks & Limitations](#risks--limitations)
- [Team & Contributions](#team--contributions)
- [Next Steps](#next-steps)
- [Acknowledgments](#acknowledgments)


## Problem Context

> “Sorry, I’m running late — the TTC’s delayed again.”

For many Toronto commuters, subway delays are a frustratingly common experience. Riders face long wait times, vague announcements, and limited insight into when service will resume. These frustrations regularly surface on Reddit, X (formerly Twitter), TTC board meetings, and city council reports.

In 2023 alone, the TTC logged over **23,000 subway delays** ([TTC Service Summary, 2022–2023](https://www.ttc.ca/-/media/Project/TTC/DevProto/Documents/Home/Transparency-and-accountability/Service-Summary_2022-11-20.pdf)) 

This impacts more than **625,000 daily riders on Line 1** ([TTC Subway Ridership, 2023–2024](https://cdn.ttc.ca/-/media/Project/TTC/DevProto/Documents/Home/Transparency-and-accountability/Subway-Ridership-20232024.pdf))

## Financial Impact

Toronto’s subway delays aren’t just an inconvenience—they’re costly.

A 2023 analysis by *City Hall Watcher* reported an average of **5,903 subway delay minutes per month**, up from **3,853 minutes** in 2019—a **53% increase** in service disruptions ([City Hall Watcher, 2023](https://toronto.cityhallwatcher.com/p/chw257)).

While TTC doesn’t publish a per-minute cost of delays, we can extrapolate from international studies and Canadian context:

| Estimate Source | Metric | Delay Cost Assumption | Monthly Cost | Annual Cost |
|------------------|--------|------------------------|--------------|-------------|
| NYC Comptroller (2017) | Major delay cost (USD) | $50–$100/minute | ~$295,000+ | ~$3.5M+ CAD |
| Modeled for TTC | 5,903 delay mins × $50 CAD/min | Conservative | ~$295,150 CAD | ~$3.54M CAD |

(Source: [ITS Canada Transit Delay Study](https://www.itscanada.ca/files/ITS%20Student%20Competition_Alaa%20Itani.pdf))

To put this in context, the TTC’s 2025 operating budget is **$2.38 billion CAD**, with only **26% covered by fares**—the rest subsidized by public funds ([Global News, 2024](https://globalnews.ca/news/10702607/canada-public-transit-funding-shortfall/)).

### Why This Matters

Our project aims to forecast delay trends and uncover contributing factors using TTC’s real-world data. This can help:

- Reduce unplanned service costs  
- Support operational planning  
- Improve rider satisfaction and public accountability  
- Justify proactive infrastructure investment


City councillors, transit users, and TTC board members continue to call for **data-informed strategies** to improve service reliability, transparency, and rider trust.


## Objective

Build a forecasting tool that helps TTC operations and commuters anticipate:

- Whether a controllable delay is likely to occur  
- How long that delay might last  
- Where and when the delay is most likely to happen  

This tool supports:

- Rush-hour service planning  
- Real-time alert prioritization  
- Data-informed communication with riders

This tool is intended to be a **reproducible, reusable foundation** for future delay mitigation planning.

## Scope

- **Focus**: Controllable delays only (e.g., operational issues like infrastructure, staffing)
- **Excludes**: External causes that cannot be addressed by TTC operations, bound and vehicle no. 
- **Subway Lines in Scope**:
  - Line 1 – Yonge–University  
  - Line 2 – Bloor–Danforth  
  - Line 4 – Sheppard  
  - *Note: Line 3 (Scarborough RT) was decommissioned in 2023 and excluded due to incomplete data*

## Sprint Timeline

| Date          | Milestone                                      |
|---------------|------------------------------------------------|
| July 17, 2025 | Project kickoff, scope alignment               |
| July 18–20    | Initial data cleaning and EDA                  |
| July 20–24    | Modeling (classification + regression)         |
| July 23       | Extended data cleaning + feature engineering   |
| July 24–25    | SHAP explainability + final visualizations     |
| July 26, 2025 | Final 5-minute POC walkthrough presentation    |

## Business Problem

How can TTC better forecast controllable subway delays to reduce rider uncertainty?

- Over 23,000 delays occurred in 2023 alone  
- Line 1 sees over 625,000 daily riders — yet alerts remain reactive and vague  
- Delays during peak hours create bottlenecks, stress, and missed commitments  

A well-scoped machine learning tool could help the TTC proactively mitigate delays, optimize dispatching, and improve the rider experience.

## Dataset Source

**Open Data Toronto – [Subway Delay Records](https://open.toronto.ca/dataset/ttc-subway-delay-data/)**

## Folder Structure

```
DSI_ML_Team8/
├── data/
│   ├── raw/                              # Original CSVs (2014–2025) from Open Data Toronto, including delay reason codes
│   └── processed/
│       └── ttc_delay_data_merged.csv         # Cleaned and merged dataset with decoded delay reasons (2022–2024)
├── notebooks/                           # EDA, modeling, SHAP analysis
├── outputs/                             # Visualizations and final report artifacts
├── report/                              # Final slides and summary documents
└── README.md
```

## Methodology

### Data Cleaning

- Removed null, canceled, and unknown entries  
- Filtered for controllable delays only  
- Joined reason code definitions with main dataset  

### Feature Engineering (in progress)

- Extracted `hour`, `day_of_week`, and grouped `code` categories  
- Created `code_freq` (frequency of delay reason per station/hour)  
- Converted categorical features to numeric encodings  

### Modeling

#### Binary Classification  
- **Goal**: Forecast whether a controllable delay will occur  
- **Algorithms**: Logistic Regression, Random Forest, XGBoost  
- **Outcome**: XGBoost shows strong precision/recall using `hour`, `station`, `day_of_week`, and `code`  

#### Regression  
- **Goal**: Forecast duration of delay (in minutes)  
- **Algorithms**: Linear Regression, Decision Tree, XGBoost  
- **Outcome**: XGBoost yields best results; delay duration shows some linearity  

#### Multi-Class Classification  
- **Goal**: Forecast top 5 recurring delay reasons (`code`)  
- **Algorithms**: Decision Tree, Random Forest (in progress)

## Key Signals (Preliminary)

- Predictive features with highest influence:  
  - `hour`  
  - `station`  
  - `day_of_week`  
  - `code` (mapped via lookup table)  
- XGBoost is the top-performing model in both classification and regression

## Risks & Limitations

- **Short sprint window (10 days)**: Limited time restricted deeper hyperparameter tuning and model generalization.
- **Data quality constraints**: Training was limited to 2022–2024 data due to time constraints, which may reduce model accuracy from underexposure to historical patterns.
- **Scope exclusions**: External events (e.g., weather, emergency services, medical incidents) were excluded, despite their real-world impact on delays.
- **Not production-ready**: Current prototype is not integrated with real-time systems or live data pipelines.

These risks highlight areas for future exploration and refinement.


## Team & Contributions

| Name                     | GitHub                                     | Email                        | Contributions                                    | Reflection Video |
|--------------------------|--------------------------------------------|------------------------------|--------------------------------------------------|------------------|
| Valerie Poon             | [@val-poon](https://github.com/val-poon)   | valerieyfp@gmail.com         | PM, reporting, folder setup, documentation       | TBD              |
| Sahil Modi               | [@smodi23](https://github.com/smodi23)     | sahilmodi237@gmail.com       | 2022–2024 data wrangling, EDA                    | TBD              |
| Saad Khan                | [@Saadkhan-188](https://github.com/Saadkhan-188) | saadkhan188@gmail.com  | Business framing, data visualization             | TBD              |
| Sneha Gupta              | [@reachsneha02](https://github.com/reachsneha02) | reachsneha02@gmail.com | Classification models, experimentation           | TBD              |
| Sucharitha Sundararaman | [@suchi-dev-ai](https://github.com/suchi-dev-ai) | suchiraman22@gmail.com | Regression modeling                              | TBD              |
| Faiz Shaikh              | [@FaizS11](https://github.com/FaizS11)     | faizkshaikh11@gmail.com      | SHAP analysis, data visualization (in progress)  | TBD              |

## Next Steps

- Complete SHAP model explainability and finalize visualizations  
- Finalize classification for top delay reason codes  
- Deliver stakeholder-ready walkthrough slides and POC  

## Acknowledgments

Special thanks to the UofT DSI instructional team and sprint facilitators for their guidance throughout this project.
