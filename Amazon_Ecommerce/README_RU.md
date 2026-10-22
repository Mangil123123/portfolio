
# 🛍️ Дашборд анализа e-commerce Amazon (Power BI)
##### [← Назад к портфолио](../README_RU.md) | [Switch to English](README.md)

![Amazon E-Commerce Dashboard](Images/Amazon_Ecommerce.png)

## 🇷🇺 О проекте

Дашборд в Power BI для анализа потребительского поведения на Amazon: динамика выручки, топ категорий и товаров, демография покупателей и география доставок.

### 🎯 Бизнес-задача

**Контекст:** Amazon — крупнейший маркетплейс. Данные охватывают период 2018–2022 гг. (≈2M транзакций, ≈5K уникальных пользователей).
**Задача:** Создать единое окно мониторинга, отвечающее на вопросы:
- Как меняется выручка и количество транзакций по годам?
- Какие товары и категории приносят максимальный доход?
- Какая демографическая группа (возраст) является основной целевой аудиторией?
- Как распределяются продажи по штатам США?

**Бизнес-ценность:** Понимание сезонности (пики в Черную пятницу и Prime Day), выявление самых маржинальных товаров и портрета типичного покупателя для настройки таргетированной рекламы.

## 🛠️ Инструменты

- Power BI Desktop
- DAX (меры, итераторы SUMX, контекст фильтра)
- Power Query (очистка пропусков, перевод центов в доллары)
- CSV (3 файла датасета Amazon)

## Что я сделал

### 1. Подготовка данных (Power Query)
- Загрузил 3 файла: `amazon-purchases.csv`, `survey.csv` (демография), `fields.csv` (словарь).
- **Обработка цен:** Исходные цены хранились в центах (например, 13999 = $139.99). Создан вычисляемый столбец с делением на 100 и установлен тип `Decimal Number`.
- **Обработка пропусков:** Пустые категории и штаты заполнены как `Other` и `Digital / no state`, чтобы не терять транзакции.
- **Оптимизация:** Текстовая колонка `Title` (названия товаров) удалена из таблицы фактов и вынесена в отдельный справочник `Dim_Product` для снижения веса `.pbix` файла.
- Связи в модели (star schema):
  - `Calendar[Date]` → `amazon-purchases[Date.OrderPurchase]` (1:*)
  - `Dim_Product[ASIN]` → `amazon-purchases[ASIN]` (1:*)
  - `survey[RespondentID]` → `amazon-purchases[RespondentID]` (1:*)

### 2. Календарная таблица
```dax
Calendar = CALENDAR(DATE(2018,1,1), DATE(2022,12,31))
```
Столбцы: `Year`, `Month`, `MonthKey`, `Quarter`. Сортировка `Month` выполнена по `MonthKey` для корректного хронологического отображения на графиках.

### 3. DAX-меры (таблица `_Measures`)

**Total Revenue**
```dax
Total Revenue = SUMX('amazon-purchases', 'amazon-purchases'[PriceUsd] * 'amazon-purchases'[Quantity])
```
**Total Items**
```dax
Total Items = SUM('amazon-purchases'[Quantity])
```
**Total Transactions**
```dax
Total Transactions = COUNTROWS('amazon-purchases')
```
**Unique Customers**
```dax
Unique Customers = DISTINCTCOUNT('amazon-purchases'[RespondentID])
```
**Avg Transaction Value**
```dax
Avg Transaction Value = DIVIDE([Total Revenue], [Total Transactions])
```
**Revenue per Customer**
```dax
Revenue per Customer = DIVIDE([Total Revenue], [Unique Customers])
```
**Max Price**
```dax
Max Price = MAX('amazon-purchases'[PriceUsd])
```

### 4. Визуализация
- **KPI-карточки** (6) — Total Revenue, Total Items, Total Transactions, Unique Customers, Avg Transaction Value, Revenue per Customer с иконками.
- **Line Chart** — динамика выручки по датам, отображает сезонные пики.
- **Bar Chart** — топ-10 категорий и топ-10 товаров по выручке (подарочные карты и пустые названия исключены для чистоты аналитики).
- **Donut Chart** — распределение выручки по возрастным группам.
- **Map** — распределение выручки по штатам доставки.
- **Slicer** — фильтрация по годам (2018–2022).

### 5. Дизайн
- Фон `#FAFAFA`, карточки `#E6E6E6` с закруглёнными углами, темно-синие акценты.
- Единый шрифт (Segoe UI), скрытые оси и сетки на графиках для чистоты.
- Заголовок канваса: «Amazon E-Commerce Dashboard».

![Amazon_Ecommerce](Images/Amazon_Ecommerce.gif)

## 📈 Ключевые инсайты

- **Выручка:** $376M за период, ≈2M транзакций от 5K клиентов.
- **Средний чек:** $203. Высокий показатель обусловлен тем, что в исходном датасете количество единиц товара (`Quantity`) зафиксировано как 10 для каждой транзакции.
- **Сезонность:** Четкие пики в ноябре-декабре (Черная пятница, Рождество) и в июле (Prime Day).
- **Топ категории:** Книги, Зоотовары, БАДы.
- **Топ товары:** PlayStation 5, Amazon Reload, Fire TV Stick, Apple AirPods.
- **Демография:** Основную выручку (32%) приносят клиенты в возрасте 25–34 лет.
- **География:** Лидеры — Калифорния, Техас и Нью-Йорк.

## 💡 Рекомендации

1. **Ассортимент:** Сфокусировать маркетинговый бюджет на топ-категориях (Книги, Зоотовары, Техника).
2. **Сезонность:** Наращивать складские запасы и запускать рекламные кампании за 2-3 недели до июля и ноября.
3. **Демография:** Настроить таргетинг на аудиторию 25–34 лет — это самая платежеспособная группа в выборке.

## 📂 Датасет

**Источник:** [Amazon Open E-Commerce 1.0 (Nature Scientific Data)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YGLYDY)


**Файл:** [📥 Скачать .pbix файл](https://github.com/Mangil123123/portfolio/releases/download/v1.00/amazon.pbix) (требуется Power BI Desktop)

## 🗂️ Другие проекты

| | | |
|---|---|---|
| <a href="../Olist_Ecommerce/README_RU.md"><img src="../Olist_Ecommerce/Images/Olist_Ecommerce.png" width="300" alt="Olist"></a> | <a href="../Telco_Churn/README_RU.md"><img src="../Telco_Churn/Images/Churn_Dashboard.png" width="300" alt="Telco Churn"></a> | <a href="../Superstore/README_RU.md"><img src="../Superstore/Images/Superstore.png" width="300" alt="Superstore"></a> |
| **Olist E-Commerce** | **Telco Churn** | **Superstore** |
| Бразильский e-commerce | Отток клиентов телеком | Ритейл-аналитика |

| | | |
|---|---|---|
| <a href="../Airbnb_NYC/README_RU.md"><img src="../Airbnb_NYC/images/Airbnb_NYC.png" width="300" alt="Airbnb"></a> | <a href="../HR_Employee_Attrition/README_RU.md"><img src="../HR_Employee_Attrition/images/HR_dashboard.png" width="300" alt="HR"></a> | <a href="../AdventureWorks_Sales_Dashboard/README_RU.md"><img src="../AdventureWorks_Sales_Dashboard/images/AdventureWorks_Sales_Dashboard.png" width="300" alt="AdventureWorks"></a> |
| **Airbnb NYC** | **HR Analytics** | **AdventureWorks Sales** |
| Рынок аренды | Текучесть персонала | Анализ продаж |

| |
|---|
| <a href="../Netflix_analysis/README_RU.md"><img src="../Netflix_analysis/images/Netflix_dashboard3.png" width="260" alt="Netflix"></a> |
| **Netflix Analysis** |
| Анализ контента Netflix |

[← Назад к портфолио](../README_RU.md)
