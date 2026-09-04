# Titanic Survival Analysis — Project 1

## Overview
This project explores the Titanic passenger dataset to understand what factors were
associated with survival. It was my first end-to-end data analysis project, covering
data loading, cleaning, exploration, and visualization using Python and pandas.

## Tools Used
- Python
- pandas (data loading, cleaning, grouping)
- matplotlib (visualization)

## What I Did
1. Loaded the raw Titanic dataset (`train.csv`) using pandas
2. Checked the data's shape and column names
3. Identified missing values across columns using `isnull().sum()`
4. Calculated overall survival rate
5. Grouped survival rate by **gender** and by **passenger class**
6. Visualized both findings as bar charts

## Key Findings

**Survival by Gender**
- Female passengers: ~74% survived
- Male passengers: ~19% survived

Women were far more likely to survive than men — consistent with the historical
"women and children first" evacuation policy during the disaster.

**Survival by Passenger Class**
- 1st Class: ~63% survived
- 2nd Class: ~47% survived
- 3rd Class: ~24% survived

Passengers in higher (wealthier) travel classes had significantly better survival
odds, likely reflecting better access to lifeboats and higher decks.

**Combined (Gender + Class)**
Breaking survival down by both gender and class together showed the effect
compounds — for example, women in 1st class had the highest survival rates,
while men in 3rd class had the lowest.

## Charts
- `survival_by_gender.png` — Bar chart comparing survival rate by gender
- `survival_by_class.png` — Bar chart comparing survival rate by passenger class

## What I'd Explore Next
- Whether age played a role in survival (e.g., were children prioritized?)
- Whether traveling with family (siblings/spouses/parents/children aboard)
affected survival odds
- Building a simple prediction model using scikit-learn

## About Me
This project is part of my transition into data analytics, building on a
background in Business Intelligence tools (Tableau, Power BI) and an MBA
in Data Science.
