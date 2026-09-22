# 🏪 Superstore Sales Analysis Dashboard

![Superstore Sales](Images/Superstore.png)

## 🇺🇸 About the Project

Minimalist Power BI dashboard for analyzing sales dynamics and structure of a retail network.

### 🎯 Business Task

**Context:** A retail company needs to track key sales metrics.
**Task:** Create a unified monitoring window answering the following questions:
- What is the total revenue and average order value?
- Which product categories generate the main income?
- How do sales dynamics change by year?
- Which customer segment is the primary one?
- How are sales distributed by region?

**Business Value:** Reducing report analysis time through an intuitive interface and focus on top categories allows faster identification of trends and anomalies.

## 🛠️ Tools

- Power BI Desktop
- DAX
- Power Query (data recovery)
- CSV (data source)

## What I Did

### 1. Data Preparation
- Recovered the dataset after a critical error: during initial cleaning, 70% of rows were accidentally deleted (Total Sales dropped from 2.26M to 600K).
- Solved the broken dates issue without data loss risk.

### 2. DAX Measures

**Total Sales**
```dax
Total Sales = SUM('train'[Sales])
```

**Avg Order Value**
```dax
Avg Order Value = DIVIDE([Total Sales], [Total Orders])
```

**Total Orders**
```dax
Total Orders = DISTINCTCOUNT('train'[Order ID])
```

**Year**
```dax
Year = RIGHT('train'[Order Date], 4)
```

### 3. Visualization
- **KPI Cards** — Total Sales, Avg Order Value, Total Orders with embedded SVG icons.
- **Bar Chart** — Sales by Sub-Category.
- **Donut Chart** — Distribution by Segment.
- **Line Chart** — Sales Trend by Year.
- **Map** — US Sales Geography.

### 4. Design
- Strict minimalism: background `#E5E5EA`, cards `#FFFFFF`, border radius 12px.
- Removed all unnecessary elements: X/Y axes, gridlines, borders.
- Color scheme: blue, white, gray.
- Icons integrated into KPI cards via Image visualization.

![Superstore Sales](Images/Superstore.gif)

## 💡 Applied Skills

- Emergency data recovery and ETL error handling
- Writing DAX measures (DISTINCTCOUNT, DIVIDE, RIGHT, SUM)
- Conditional Formatting (Rules) for custom color schemes
- UI dashboard design
- Visual optimization

## 📈 Key Insights

- **Dynamics:** Stable sales growth since 2016.
- **Category Leaders:** Phones (328K) and Chairs (323K) generate ~30% of total revenue.
- **Segmentation:** Consumer is the leader (50.76%), Corporate takes second place (30.44%).
- **Geography:** California and New York are key markets; central states require attention.

## 💡 Recommendations

1. **For Marketing:** Boost promotion in the Corporate segment (30% growth potential).
2. **Assortment:** Focus on Phones and Chairs.
3. **Analysis:** Conduct deep-dive analysis of central states (gray zone on map) to uncover hidden demand.

##  Dataset

Educational project based on the public Superstore dataset, adapted for real-world retail analysis tasks.

**Source:** [Superstore Sales Dataset on Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)

**File:** [📥Download .pbix File](https://raw.githubusercontent.com/Mangil123123/portfolio/main/Superstore/Files/Superstore.pbix) (Final report; requires free Power BI Desktop to view)

**Time Spent:** 4 days
