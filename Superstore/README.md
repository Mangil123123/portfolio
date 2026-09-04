# 📊 Superstore Sales Analysis Dashboard

![Superstore Sales](Images/Superstore.png)

## 🇺🇸 About the Project

A minimalist Power BI dashboard designed to analyze sales dynamics and structure for a retail network. The project focuses on data integrity, clean visualization, and actionable business insights.

### 🎯 Business Task

**Context:** A retail company needs a transparent tool to track key sales metrics without visual noise. Standard reports are often overloaded with details, hindering quick decision-making.

**Objective:** Create a unified monitoring window that answers the following questions:
- What is the total revenue and average order value?
- Which product categories generate the most income?
- How do sales trends change over the years?
- Which customer segment is the primary driver?
- How are sales distributed across regions?

**Business Value:** Reducing report analysis time through an intuitive interface and focus on top categories allows for faster identification of trends and anomalies.

## 🛠️ Tech Stack

- Power BI Desktop
- DAX (Data Analysis Expressions)
- Power Query (Data Recovery & Transformation)
- CSV (Data Source)

## What I Did

### 1. Data Preparation
- **Recovered the dataset** after a critical error: accidentally deleted 70% of rows during initial cleaning (Total Sales dropped from 2.26M to 600K).
- Solved the "broken dates" issue (`Order Date` as text) without data loss using a DAX hack:
```dax
Year = RIGHT('train'[Order Date], 4)
```

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

**Year (Calculated Column)**
```dax
Year = RIGHT('train'[Order Date], 4)
```

### 3. Visualization
- **KPI Cards** — Total Sales, Avg Order Value, Total Orders with embedded SVG icons.
- **Bar Chart** — Sales by Sub-Category.
- **Donut Chart** — Distribution by Customer Segment.
- **Line Chart** — Sales Trend by Year.
- **Map** — US Sales Geography.

### 4. Design
- **Strict Minimalism:** Background `#E5E5EA`, Cards `#FFFFFF`, Border Radius 12px.
- Removed all unnecessary elements: X/Y axes, gridlines, borders.
- **Color Scheme:** Blue, White, Gray. No rainbow palettes.
- Icons integrated directly into KPI cards via Image visualization.

![Superstore Sales](Images/Superstore.gif)

## Skills Applied

- Emergency data recovery and ETL error handling
- Writing DAX measures (DISTINCTCOUNT, DIVIDE, RIGHT, SUM)
- Conditional Formatting (Rules) for custom color schemes
- UI/UX Dashboard Design
- Visual Optimization

## 📈 Key Insights

- **Dynamics:** Stable sales growth since 2016.
- **Category Leaders:** Phones (328K) and Chairs (323K) generate ~30% of total revenue.
- **Segmentation:** Consumer is the leader (50.76%), Corporate takes second place (30.44%).
- **Geography:** California and New York are key markets; central states require attention.

## 💡 Recommendations

1. **Marketing:** Boost promotion in the Corporate segment (30% growth potential).
2. **Assortment:** Focus on Phones and Chairs as sales drivers.
3. **Analysis:** Conduct deep-dive analysis of central states (gray zone on map) to uncover hidden demand.

## 📂 Dataset

Educational project based on the public Superstore dataset, adapted for real-world retail analysis tasks.

**Source:** [Superstore Sales Dataset on Kaggle](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)

**File:** [📥Download .pbix File](https://raw.githubusercontent.com/Mangil123123/portfolio/main/Superstore/Files/Superstore.pbix) (Final report; requires free Power BI Desktop to view)

**Time Spent:** 4 days
