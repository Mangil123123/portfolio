# portfolio

# 🎬 Netflix Content Analysis Dashboard

![Netflix Dashboard](images/Netflix_dashboard3.png)

## 🇬🇧 About the Project (English)

An interactive dashboard for analyzing the Netflix content library: distribution by type, country, and year-over-year trends.

## 🎯 Business Task

Task: Conduct descriptive analytics of the Netflix content library to identify structural characteristics and trends:

- What is the library structure by content type (Movies/TV Shows)?
- How is content distributed by country of production?
- How has the volume of added content changed over the years?
- What patterns can be identified based on the available metadata?

Limitations: The analysis does not include content performance evaluation (views, retention, ROI), as this data is not available in the public dataset.

Business Value: Understanding the structure and dynamics of the library is the first step toward forming hypotheses about content strategy.

### 🛠️ Tools
- Power BI Desktop
- DAX (Data Analysis Expressions)
- Power Query (data cleaning)
- CSV (data source)

## What I Did

### 1. Data Preparation
- Imported the Netflix dataset (~8,796 records) from a CSV file
- Cleaned data in Power Query: removed blank values, errors, duplicates; split certain columns/rows, etc.

### 2. Creating DAX Measures
- Total Content — total number of titles:
```
Total Content = 
DISTINCTCOUNT('netflix_titles'[show_id])
```
- Total Movies — number of movies:
```
Total Movies = 
CALCULATE(
    DISTINCTCOUNT('netflix_titles'[show_id]),
    'netflix_titles'[Type] = "Movie"
)
```
- Total TV Shows — number of TV shows:
```
Total TV Shows = 
CALCULATE(
    DISTINCTCOUNT('netflix_titles'[show_id]),
    'netflix_titles'[Type] = "TV Show"
)
```
- Movies % — percentage of movies:
```
Movies % = 
DIVIDE(
    [Total Movies],
    [Total Content],
    0
)
```
- TV Shows % — percentage of TV shows:
```
TV Shows % = 
DIVIDE(
    [Total TV Shows],
    [Total Content],
    0
)
```
- YoY Growth — year-over-year content growth:
```
YoY Growth =
CALCULATE(
[Total Content],
SAMEPERIODLASTYEAR(netflix_titles[date_added]))
```

### 3. Data Visualization
- KPI cards — key metrics at the top of the dashboard
- Bar chart — top 10 countries by content volume (used visual filter for top 10)
- Line chart — content addition dynamics by year (2008–2020; used "less than or equal to" filter for 2020, as data dropped sharply after 2020)

### 4. Design & UX
- Placed KPIs at the top for quick overview
- Set colors based on Netflix brand design
- Added titles and labels to all charts
- Translated interface to English for international portfolio
- Added inner shadows for a modern look, rounded corners

### 5. Analysis
- Identified US dominance in content production
- Discovered sharp library growth starting from 2014
- Determined peak content addition in 2018–2019
- Analyzed movie-to-TV show ratio (70/30)

## Skills Applied
- Power Query (cleaning, transformation, merging data, etc.)
- Writing DAX measures (CALCULATE, DIVIDE, SAMEPERIODLASTYEAR, DISTINCTCOUNT)
- Dashboard visual design
- Business analytics and insight discovery
- Working with CSV data

### 📈 Key Insights
- Total content: 7,966 titles
- Ratio: 69.7% Movies vs. 30.3% TV Shows
- Country leader: USA leads (3,500+), India is 2nd (1,000+), UK is 3rd (800+)
- Growth trend: Content library grew 4–5x over 5 years (2014–2019)
- Catalog refresh: 90% of content was added after 2014

### 📂 Dataset
This is an educational project using a public dataset, but I framed the task as if it were assigned by a real business.

Time spent: 2 days  
Source: [Netflix Movies and TV Shows on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
