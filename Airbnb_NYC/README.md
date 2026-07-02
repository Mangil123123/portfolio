# Portfolio

# 🏠 Airbnb NYC Market Analysis Dashboard

![Airbnb Dashboard](images/Airbnb_NYC.png)

## 🇺🇸 About the Project

Interactive Power BI dashboard for analyzing the short-term rental market in New York City.

## 🎯 Business Task

**Context:** Short-term rental investors need data to make decisions for maximum profitability. Wrong choice of district or property type can lead to losses instead of profit.

**Task:** Conduct market analysis to identify the best investment opportunities:
- Which districts have the most listings?
- What property types are most common?
- Which districts have the highest average prices?
- What is the occupancy rate across NYC?
- Which districts offer the best investment potential?

**Business Value:** Data-driven investment decisions can increase rental income by 20-40%.

## 🛠️ Tools
- Power BI Desktop
- DAX (Data Analysis Expressions)
- Power Query (data cleaning and transformation)
- CSV (data source)

## What I Did

### 1. Data Preparation
- Imported Airbnb Open Data dataset (~102,599 listings, NYC, 26 columns)
- Cleaned data in Power Query:
  - Fixed typos in district names ("brookln" → "Brooklyn", "manhatan" → "Manhattan")
  - Handled missing values ("Unknown" → filtered out from analysis)
  - Checked data types and removed errors

### 2. DAX Measures

**Total Listings**

Measure:
```dax
🏠 Total Listings = COUNTROWS('Airbnb_Open_Data')
```

**Average Price/Night**

Measure:
```dax
💵 Avg. Price/Night = AVERAGE('Airbnb_Open_Data'[price])
```

**Occupancy Rate**

Measure:
```dax
📈 Occupancy Rate = 
DIVIDE(
    365 - AVERAGE('Airbnb_Open_Data'[availability 365]),
    365
)
```

**Avg Reviews/Month**

Measure:
```dax
⭐ Avg. Reviews/Month = AVERAGE('Airbnb_Open_Data'[reviews per month])
```

### 3. Visualization
- **KPI cards** — key metrics at the top (Total Listings, Avg Price, Occupancy Rate, Avg Reviews)
- **Stacked bar chart** — listings by district with breakdown by room type
- **Bar chart** — average price by district
- **Donut chart** — room type distribution
- **Scatter plot** — price vs reviews correlation
- **Slicers** — interactive filters for districts and room types

### 4. Design
- Clean professional design with custom styling
- KPIs at the top for quick overview
- "Top-down" structure: from overall numbers to details
- Interactive filters (district, room type)
- Key insights section with actionable findings

## Skills Applied

- Working with Power Query (cleaning, transformation, handling missing data)
- Writing DAX measures (COUNTROWS, AVERAGE, DIVIDE, CALCULATE, FORMAT)
- Dashboard visual design and UX
- Business analytics and insight identification
- Working with large CSV datasets (100K+ rows, 26 columns)
- Data quality assessment and documentation

## 📈 Key Insights
- **Market Leader:** Manhattan — most listings (~27,000)
- **Property Mix:** 52.38% — entire home/apartment
- **Price Leader:** Staten Island — highest average price ($445) among districts
- **Occupancy:** average occupancy rate — 61%
- **Data Quality:** found and fixed typos in district names, filtered out "Unknown" category

## 💡 Recommendations
1. **For Investors:** Staten Island — for premium pricing, Manhattan — for volume
2. **Property Type:** focus on entire home/apt (52% of market)
3. **Data Quality:** always validate district names in Airbnb datasets
4. **Market Saturation:** Brooklyn — good balance between number of listings and competition

## 📂 Dataset
This is an educational project on a public dataset, but the task is formulated as if it were from a real business.

**Source:** [Airbnb Open Data on Kaggle](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata) (original: InsideAirbnb NYC)

**Time spent:** 4 days
