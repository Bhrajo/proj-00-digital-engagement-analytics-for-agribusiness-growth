# Digital Engagement Analytics for Agribusiness Growth

## Project Overview

This project empirically investigates how strategic social media marketing can drive measurable agribusiness growth in Ghana, particularly among farmers cultivating highly perishable crops.

The project uses advanced data analytics and machine learning to quantify the relationship between:

- Digital engagement
- Customer value
- Brand trust
- Purchasing behavior
- Agribusiness profitability

The core objective is to demonstrate whether social media can serve as a practical, data-driven solution to reduce middleman exploitation and empower Ghanaian farmers with direct market access in the digital space. In simple terms, can farmers rely on buyers online to mitigate the "monopsony" of buyers in traditional markets?

## Problem Statement

Vegetable and perishable crop farmers in Ghana face significant exploitation by middlemen due to:

- Short product shelf life
- Limited bargaining power
- Weak infrastructure
- Lack of direct consumer access

While social media presents a promising alternative, there has been a lack of quantifiable empirical evidence linking digital engagement to measurable agribusiness growth.
This project addresses that gap using statistical modeling and predictive analytics.

## Project Objectives

1. Quantify how engagement metrics drive:
   - Customer purchasing behavior
   - Brand trust
   - Customer loyalty
   - Business growth
2. Develop evidence-based digital marketing strategies to:
   - Increase profitability
   - Broaden market access
   - Reduce middleman exploitation.

If achieved, these objectives can significantly boost farmers' confidence in exploring digital market spaces.

## Dataset

- 2,548 raw records across 19 variables

### After Cleaning and Preprocessing

After rigorous cleaning, validation, and preprocessing, the final analytical dataset consisted of:

- 694 agribusiness customers
- Social media engagement metrics
- Trust scores
- Purchase behavior
- Platform usage patterns
- Customer demographics

All sensitive identifiers were anonymized in compliance with Ghana Data Protection Act and GDPR principles.

## Methodology

The project follows a structured analytical pipeline:

### 1️. Data Preprocessing & Validation

- Missing value imputation
- Outlier handling (Winsorization)
- Feature scaling
- Integrity validation

### 2️. Exploratory Data Analysis (EDA)

- Univariate and bivariate analysis
- Customer segmentation
- Composite engagement scoring
- Platform performance comparison

### 3️. Feature Engineering

- Loyalty Resilience Score
- Brand Relation Score
- Customer Value Metrics

### 4️. Predictive Modeling

Models used:

- Linear Regression
- Logistic Regression
- Random Forest
- XGBoost
- LightGBM

Hyperparameter tuning was performed for performance optimization.

### 5️. Model Evaluation

Model evaluation included:

- R²
- Accuracy
- ROC-AUC
- Confusion Matrix
- SHAP Explainability

---

## Key Findings

### 1. There is a Strong Link Between Engagement & Customer Value

The LightGBM model achieved: **R² = 0.836**

This demonstrates that digital engagement is a statistically significant driver of measurable financial outcomes.

### 2. Clear High-Value Customer Segment Identified

A distinct “High Value” segment was discovered:

- High engagement
- Nearly double purchase frequency
- Disproportionate revenue contribution.

15.1% of customers represent the highest growth & profitability potential.

### 3. Platform Specialization Identified

Each social media platform serves a different strategic function.

- **Instagram** → Sales conversion
- **Facebook** → Brand trust & loyalty
- **Twitter** → Awareness & engagement
- **LinkedIn** → Information gathering (low purchase conversion)

A one-size-fits-all strategy is inefficient.

To fully leverage digital opportunities for agribusiness growth, farmers and agribusiness operators must allocate resources toward comprehensive digital literacy initiatives.

### 4. Customer Churn is Predictable

The XGBoost churn classification model achieved near-perfect predictive performance, indicating strong separability between retained and at-risk customers.

Key predictors:

- Loyalty Resilience
- Brand Relation Score

Customer churn is not random — it is measurable and preventable.
Agribusiness marketers should prioritize strengthening these predictive factors through targeted engagement and retention strategies.

## Strategic Implications

### For Agribusiness Managers

- Allocate resources based on customer segmentation
- Prioritize high-growth & high-profit segments
- Track loyalty metrics as primary KPIs
- Invest in influencer marketing strategies to strengthen brand trust
- Future analytics initiatives, particularly sentiment analysis of social media interactions, are recommended to further refine engagement strategies.

### For Policymakers & NGOs

- Invest in digital literacy programs
- Support data-driven marketing training
- Strengthen digital infrastructure in rural areas

## Project Structure

```
Proj-00-digital-engagement-analytics-for-agribusiness-growth

|── data
  ── Cleaned_Agribusiness_Social_Media_Marketing.csv
  ── Engineered_Features.csv
  ── (processed datasets used for modeling)

|── notebooks
  ── Enhancing_Digital_Engagement_for_Agribusiness_Growth.ipynb
  ── Enhancing_Digital_Engagement_for_Agribusiness_Growth.html
  ── Enhancing_Digital_Engagement_for_Agribusiness_Growth.pdf

|── outputs
  |── 01-data-preprocessing-and-validation
   ── README.md
   ── (validation visualizations)
 
  |── 02-exploratory-data-analysis
   ── README.md
   ── (EDA visualizations)
 
  |── 03-modeling-and-predictions
   ── README.md
   ── (model performance & prediction visualizations)

|── environment.yml
 ── requirements.txt
 ── README.md
 ── LICENSE
 ── .gitignore

```

### Structure Overview

- **data/** – Contains cleaned and engineered datasets used in modeling and analysis.
- **notebooks/** – Contains the primary analytical notebook and exported versions for review.
- **outputs/** – Stores categorized visual results aligned with each stage of the analytical pipeline.
- **environment.yml** and **requirements.txt** – Ensure full reproducibility of the computational environment.
