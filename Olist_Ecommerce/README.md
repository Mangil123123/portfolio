# 🛒 Brazilian E-Commerce Analytics Dashboard (Olist, Power BI)
##### [← Back to portfolio](../README.md) | [Переключить на русский](README_RU.md)

![Olist E-Commerce Dashboard](Images/Olist_Ecommerce.png)

## 🇺🇸 About

Power BI dashboard for analyzing the performance of the Brazilian marketplace Olist: revenue trends, top categories, order geography, delivery quality and customer reviews.

### 🎯 Business objective

**Context:** Olist is a marketplace for electronics and home goods. Data covers September 2016 – September 2018 (≈99K orders, ≈112K items).
**Task:** Build a single monitoring window answering:
- How does revenue grow by month and quarter?
- Which product categories drive the most revenue?
- Which Brazilian states lead in orders?
- How reliable is delivery (lead time, on-time rate)?
- How do customers rate their purchases?

**Business value:** Revealing seasonality, top categories and geographic leaders helps optimize logistics, marketing budget and assortment.

## 🛠️ Tools

- Power BI Desktop
- DAX (measures, iterators, Calendar table)
- Power Query (cleaning, Replace Values, Capitalize Each Word)
- CSV (6 files of the Olist dataset)

## What I did

### 1. Data preparation
- Loaded 6 CSV files: `olist_customers_dataset`, `olist_order_items_dataset`, `olist_order_reviews_dataset`, `olist_orders_dataset`, `olist_products_dataset`, `product_category_name_translation` (geolocation / payments / sellers not used).
- Power Query cleaning: replaced `_` with space in category names → `Capitalize Each Word` (`health_beauty` → `Health Beauty`).
- Null handling: `null` categories mapped to `Other` via a DAX calculated column `Product Category` (`IF(ISBLANK(...), "Other", ...)`), so no orders are lost in calculations and `(Blank)` is removed from the slicer.
- Created calculated column `Date.OrderPurchase` (type Date) for a correct relationship with Calendar.
- Star-schema relationships:
  - `Calendar[Date]` → `orders[Date.OrderPurchase]` (1:*)
  - `orders[order_id]` → `order_items[order_id]` (1:*)
  - `orders[order_id]` → `order_reviews[order_id]` (1:*)
  - `orders[customer_id]` → `customers[customer_id]` (*:1)
  - `order_items[product_id]` → `products[product_id]` (*:1)
  - `products[product_category_name]` → `translations[product_category_name]` (*:1)

### 2. Calendar table
```dax
Calendar = CALENDAR(MIN('olist_orders_dataset'[order_purchase_timestamp]), MAX('olist_orders_dataset'[order_purchase_timestamp]))
```
Columns: `Year`, `Month`, `Quarter`, `MonthKey`, `MonthNumber`. `Month` is sorted by `MonthKey`, not by month number (the latter repeats every year and breaks chronology — the source of the "sawtooth" on the chart before the fix).

### 3. DAX measures (table `_Metrics`)

**Total Revenue**
```dax
Total Revenue = SUM('olist_order_items_dataset'[price])
```

**Total Orders**
```dax
Total Orders = DISTINCTCOUNT('olist_orders_dataset'[order_id])
```

**Avg Order Value**
```dax
Avg Order Value = AVERAGEX(DISTINCT('olist_orders_dataset'[order_id]), CALCULATE(SUM('olist_order_items_dataset'[price])))
```

**Avg Review Score**
```dax
Avg Review Score = AVERAGE('olist_order_reviews_dataset'[review_score])
```

**On-time Delivery Rate**
```dax
On-time Delivery Rate = 
DIVIDE(
    CALCULATE(
        COUNTROWS('olist_orders_dataset'),
        'olist_orders_dataset'[order_delivered_customer_date] <= 'olist_orders_dataset'[order_estimated_delivery_date]
    ),
    CALCULATE(
        COUNTROWS('olist_orders_dataset'),
        NOT ISBLANK('olist_orders_dataset'[order_delivered_customer_date])
    ),
    0
)
```

**Avg Delivery Days**
```dax
Avg Delivery Days = 
AVERAGEX(
    FILTER(
        'olist_orders_dataset',
        NOT ISBLANK('olist_orders_dataset'[order_delivered_customer_date])
    ),
    DATEDIFF(
        'olist_orders_dataset'[order_purchase_timestamp],
        'olist_orders_dataset'[order_delivered_customer_date],
        DAY
    )
)
```

**Total Freight**
```dax
Total Freight = SUM('olist_order_items_dataset'[freight_value])
```

**Total Items**
```dax
Total Items = COUNTROWS('olist_order_items_dataset')
```
> The Olist dataset has no `quantity` field: each `order_items` row is a single product line, so item count is the number of rows, not the sum of `order_item_id` (which is a position index inside an order).

### 4. Visualization
- **KPI cards** (6) — Total Revenue, Total Orders, Avg Order Value, Avg Review Score, On-time Delivery Rate, Avg Delivery Days with png icons.
- **Line chart** — revenue by month (`Calendar[Month]` × `Total Revenue`), visible range Jan 2017 – Aug 2018 (2016 excluded due to data gaps, Sep 2018 incomplete; local visual-level filter).
- **Bar chart (horizontal)** — revenue by category (`Product Category` × `Total Revenue`), top-10.
- **Matrix** — `Top 10 Categories` (`Product Category` × `Total Revenue`, `Total Orders`, `Avg Review Score`).
- **Map (bubble)** — revenue by state (`Customer state` × `Total Revenue`).
- **Slicers** (4, Dropdown) — Year, Product Category, Customer state, Order Status.
- Data labels enabled on bar charts for instant reading.

### 5. Design
- Page background `#FAFAFA`, cards `#FFFFFF` with 30px rounded corners.
- Accent color `#118DFF`, icons embedded inside KPI cards.
- Canvas header in two lines: “Welcome to” (small) + product name (large).
- All visual and slicer titles in English.

![Olist_Ecommerce](Images/Olist_Ecommerce.gif)

## Skills applied

- Power Query work (replace values, Capitalize Each Word, data types)
- DAX measures (`AVERAGEX, AVERAGE, CALCULATE, DIVIDE, COUNTROWS, FILTER, DATEDIFF, DISTINCT, DISTINCTCOUNT, SUM, ISBLANK`)
- Calendar table and time intelligence
- Dashboard UI design

## 📈 Key insights

- **Revenue:** R$ 1.36 billion over the period, ≈99K orders, ≈112K items.
- **Average order value:** R$ ≈13,800. Olist is a marketplace for electronics and home goods (top: Health Beauty, Watches Gifts, Computers Accessories), so the basket is larger than grocery e-commerce; the metric reflects average revenue per order, including multi-item carts.
- **Rating:** Avg Review Score 4.09/5 — high customer satisfaction.
- **Delivery:** On-time Delivery Rate ≈95%, average lead time ≈12 days.
- **Top categories:** Health Beauty (R$ 126M), Watches Gifts (R$ 121M), Bed Bath Table (R$ 104M), Sports Leisure (R$ 99M), Computers Accessories (R$ 91M).
- **Seasonality:** revenue growth 2017 → 2018, Q4 peaks (Black Friday in November, Christmas season in December).
- **Geography:** Southeast states (São Paulo, Rio de Janeiro, Minas Gerais) lead in orders.

## 💡 Recommendations

1. **Assortment:** strengthen the top-5 categories — they drive most of the revenue.
2. **Logistics:** investigate the ≈5% late deliveries by state and category.
3. **Seasonality:** prepare stock and marketing for Q4 — historically the peak period.
4. **Geography:** expand beyond the Southeast.

## 📂 Dataset

Learning project on the public Brazilian E-Commerce by Olist dataset, adapted to real e-commerce analysis tasks.

**Source:** [Brazilian E-Commerce Public Dataset by Olist on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Period:** September 2016 – September 2018. 2016 is a store-launch year with uneven data (October contains a batch of historical orders, November–December a dip), and September 2018 is incomplete. The revenue trend chart shows the representative window January 2017 – August 2018; the remaining metrics (KPIs, categories, states) are computed on the full base.

**Currency:** all amounts in the dataset are in Brazilian reais (BRL). The dashboard and this README use the `R$` symbol; conversion to USD was deliberately omitted to avoid introducing exchange-rate error for 2017–2018.

**Volume:** 6 CSV files; ≈99K orders, ≈112K items; lookup tables — products, customers, order_reviews, translations.

**File:** [📥 Download .pbix file](https://github.com/Mangil123123/portfolio/releases/download/v1.0/brazilian.e_commerce.pbix) (final report; free Power BI Desktop required to view)

**Time spent:** 6 days


## 🗂️ Other Projects

| | | |
|---|---|---|
| <a href="../Telco_Churn/README.md"><img src="../Telco_Churn/Images/Churn_Dashboard.png" width="300" alt="Telco Churn"></a> | <a href="../Superstore/README.md"><img src="../Superstore/Images/Superstore.png" width="300" alt="Superstore"></a> | <a href="../Airbnb_NYC/README.md"><img src="../Airbnb_NYC/images/Airbnb_NYC.png" width="300" alt="Airbnb"></a> |
| **Telco Churn** | **Superstore** | **Airbnb NYC** |
| Telecom churn analysis | Retail sales analytics | Short-term rental market |

| | | |
|---|---|---|
| <a href="../HR_Employee_Attrition/README.md"><img src="../HR_Employee_Attrition/images/HR_dashboard.png" width="300" alt="HR"></a> | <a href="../AdventureWorks_Sales_Dashboard/README.md"><img src="../AdventureWorks_Sales_Dashboard/images/AdventureWorks_Sales_Dashboard.png" width="300" alt="AdventureWorks"></a> | <a href="../Netflix_analysis/README.md"><img src="../Netflix_analysis/images/Netflix_dashboard3.png" width="300" alt="Netflix"></a> |
| **HR Analytics** | **AdventureWorks Sales** | **Netflix Analysis** |
| Employee attrition | Bike retail sales analysis | Netflix content analysis |

[← Back to portfolio](../README.md)
