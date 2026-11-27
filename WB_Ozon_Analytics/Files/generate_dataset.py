# -*- coding: utf-8 -*-
"""Генератор демо-датасета WB/Ozon: выручка, комиссии, возвраты, прибыль по SKU."""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
OUT = Path(r"C:\Users\Rodki\OneDrive\Документы\github\portfolio-main\WB_Ozon_Analytics\Files")
OUT.mkdir(parents=True, exist_ok=True)

# ---------- 1. Товары ----------
CATS = {
    "Одежда": dict(comm=0.20, ret=0.30, logi=55, stor=(40, 90)),
    "Электроника": dict(comm=0.12, ret=0.05, logi=120, stor=(80, 200)),
    "Дом и кухня": dict(comm=0.17, ret=0.10, logi=90, stor=(60, 160)),
    "Красота": dict(comm=0.18, ret=0.08, logi=45, stor=(30, 70)),
    "Дети": dict(comm=0.17, ret=0.12, logi=70, stor=(40, 100)),
    "Спорт": dict(comm=0.15, ret=0.09, logi=85, stor=(50, 130)),
}
PRODUCTS = [
    ('Одежда', 'Футболка хлопковая базовая', 'Basics', 380, 1290),
    ('Одежда', 'Худи оверсайз с начесом', 'Basics', 1150, 3490),
    ('Одежда', 'Джинсы прямые мужские', 'Denverse', 1450, 3990),
    ('Одежда', 'Платье миди плиссе', 'Lunelle', 980, 2790),
    ('Одежда', 'Куртка демисезонная', 'Denverse', 2600, 6990),
    ('Одежа', 'Носки тонкие 5 пар', 'Basics', 90, 390),
    ('Одежда', 'Свитер вязной', 'Lunelle', 1250, 3290),
    ('Одежда', 'Спортивные леггинсы', 'FitLine', 420, 1490),
    ('Одежда', 'Рубашка льняная', 'Lunelle', 780, 2190),
    ('Одежда', 'Пуховик зимний', 'Arctic Line', 3900, 10990),
    ('Одежда', 'Пиджак классический', 'Denverse', 2100, 5490),
    ('Одежда', 'Комплект термобелья', 'Arctic Line', 350, 1190),
    ('Электроника', 'Наушники TWS', 'SoundPro', 1450, 4490),
    ('Электроника', 'Портативная колонка', 'SoundPro', 1900, 5490),
    ('Электроника', 'Умные часы AMOLED', 'ChronoX', 2400, 7990),
    ('Электроника', 'Powerbank 20000 mAh', 'VoltEdge', 620, 2190),
    ('Электроника', 'Механическая клавиатура', 'KeyForge', 2300, 6490),
    ('Электроника', 'Веб-камера Full HD', 'OptiView', 780, 2490),
    ('Электроника', 'USB-хаб 4 порта', 'VoltEdge', 240, 990),
    ('Электроника', 'Электрическая зубная щетка', 'SmileTech', 890, 2990),
    ('Дом и кухня', 'Кастрюля 3 л с крышкой', 'HomeChef', 590, 1990),
    ('Дом и кухня', 'Сковорода антипригарная 24 см', 'HomeChef', 420, 1590),
    ('Дом и кухня', 'Набор ножей 5 предметов', 'BladePro', 980, 2990),
    ('Дом и кухня', 'Электрический чайник', 'HomeChef', 890, 2790),
    ('Дом и кухня', 'Постельное белье комплект', 'SoftHome', 1250, 3690),
    ('Дом и кухня', 'Аромадиффузор ультразвуковой', 'ZenHome', 340, 1290),
    ('Дом и кухня', 'Плед флисовый', 'SoftHome', 380, 1390),
    ('Дом и кухня', 'Органайзер для хранения', 'ZenHome', 290, 1090),
    ('Красота', 'Крем для лица увлажняющий', 'PureSkin', 210, 890),
    ('Красота', 'Сыворотка с витамином C', 'PureSkin', 380, 1390),
    ('Красота', 'Шампунь восстанавливающий 400 мл', 'HairLab', 260, 990),
    ('Красота', 'Набор кистей для макияжа', 'BrushArt', 340, 1290),
    ('Красота', 'Патчи под глаза', 'PureSkin', 90, 490),
    ('Красота', 'Термозащитный спрей', 'HairLab', 180, 790),
    ('Дети', 'Конструктор 120 деталей', 'KidBuild', 590, 1990),
    ('Дети', 'Мягкая игрушка 40 см', 'KidHug', 260, 990),
    ('Дети', 'Набор для творчества', 'KidBuild', 220, 890),
    ('Дети', 'Детская зубная паста', 'KidSmile', 90, 390),
    ('Дети', 'Распашонки 3 шт', 'KidHug', 280, 1090),
    ('Спорт', 'Коврик для йоги 6 мм', 'FitLine', 420, 1490),
    ('Спорт', 'Гантели разборные 2x5 кг', 'IronGrip', 1350, 3990),
    ('Спорт', 'Фитнес-резинки набор', 'FitLine', 190, 790),
    ('Спорт', 'Скоростной скакалку', 'FitLine', 130, 590),
    ('Спорт', 'Бутылка спортивная 750 мл', 'HydraSport', 160, 690),
]
COST_MULT = {"Одежда": 1.9, "Электроника": 1.7, "Дом и кухня": 1.85,
             "Красота": 1.85, "Дети": 1.8, "Спорт": 1.75}
# Ошибка закупки: себестоимость 68-78% цены — структурно убыточные SKU
DUD = {10, 18, 23, 41}
cost_map = {}
for i, (c, n, b, cp, pr) in enumerate(PRODUCTS):
    cost_map[f"SKU-{i+1:03d}"] = int(pr * rng.uniform(0.68, 0.78)) if i in DUD else int(cp * COST_MULT.get(c, 1.5))
products = pd.DataFrame(
    [(f"SKU-{i+1:03d}", n, c, b, cost_map[f"SKU-{i+1:03d}"], pr) for i, (c, n, b, cp, pr) in enumerate(PRODUCTS)],
    columns=["sku", "product_name", "category", "brand", "cost_price_rub", "price_rub"],
)

# ---------- 2. Месячные продажи ----------
months = pd.period_range("2024-10", "2025-09", freq="M")
season = {1: 0.55, 2: 0.62, 3: 1.15, 4: 0.95, 5: 0.90, 6: 0.85,
          7: 0.88, 8: 0.95, 9: 0.98, 10: 1.05, 11: 1.55, 12: 1.80}
rows = []
for idx, p in products.iterrows():
    cat_name = "Одежда" if p.category == "Одежа" else p.category  # «грязная» категория, чин в PQ
    cat = CATS[cat_name]
    base = rng.integers(120, 900)                      # базовый спрос
    if p.category == "Одежа":                          # опечатка-дубль в данных (как в жизни)
        base = rng.integers(150, 700)
    ads_base = rng.integers(25000, 60000)
    star = idx in (0, 12, 27)                          # звезды
    loser = idx in (5, 10, 18, 41)                     # проблемные SKU
    for m in months:
        s = season[m.month]
        if p.category == "Спорт" and m.month in (5, 6):
            s *= 1.25
        orders = int(base * s * rng.uniform(0.85, 1.15))
        buyouts = int(orders * rng.uniform(0.94, 0.99))
        rev_rate = cat["ret"] * rng.uniform(0.8, 1.2)
        if loser or idx in DUD:
            rev_rate *= 1.5                              # у проблемных SKU ещё и возвраты
        returns = int(orders * rev_rate)
        revenue = buyouts * p.price_rub
        commission = round(revenue * cat["comm"] * rng.uniform(0.97, 1.03))
        logistics = buyouts * int(cat["logi"] * rng.uniform(0.9, 1.1))
        storage = int(rng.uniform(*cat["stor"]) * 30)
        ads = int(ads_base * (0.6 + s) * rng.uniform(0.8, 1.2))
        if loser or idx in DUD:
            ads *= 4.0                                   # рекламные звезды сжигают маржу
        if star:
            ads = int(ads * 0.8)
        cogs = buyouts * p.cost_price_rub
        ret_cost = returns * (cat["logi"] + p.price_rub * 0.02)
        profit = revenue - commission - logistics - storage - ads - cogs - ret_cost
        rows.append([str(m), p.sku, orders, buyouts, returns,
                     revenue, commission, logistics, storage, ads,
                     int(ret_cost), cogs, int(profit)])
sales = pd.DataFrame(rows, columns=[
    "month", "sku", "orders_units", "buyouts_units", "returns_units", "revenue_rub",
    "commission_rub", "logistics_rub", "storage_rub", "ads_rub",
    "returns_cost_rub", "cogs_rub", "profit_rub"])

# ---------- 3. Причины возвратов ----------
reasons = {
    "Одежда": [("Не подошёл размер", 0.52), ("Передумал", 0.22), ("Не то качество", 0.14), ("Брак / дефект", 0.07), ("Ошибка посадки", 0.05)],
    "Электроника": [("Брак / дефект", 0.38), ("Не соответствует описанию", 0.27), ("Передумал", 0.19), ("Не подошёл размер", 0.06), ("Повреждена упаковка", 0.10)],
    "Дом и кухня": [("Не соответствует описанию", 0.34), ("Брак / дефект", 0.26), ("Передумал", 0.20), ("Повреждена упаковка", 0.12), ("Не подошёл размер", 0.08)],
    "Красота": [("Аллергия / реакция", 0.31), ("Не подошёл эффект", 0.28), ("Брак / дефект", 0.22), ("Передумал", 0.13), ("Повреждена упаковка", 0.06)],
    "Дети": [("Не подошёл возраст", 0.36), ("Брак / дефект", 0.24), ("Передумал", 0.22), ("Не соответствует описанию", 0.12), ("Повреждена упаковка", 0.06)],
    "Спорт": [("Не подошёл размер", 0.33), ("Не то качество", 0.25), ("Брак / дефект", 0.20), ("Передумал", 0.14), ("Повреждена упаковка", 0.08)],
}
rrows = []
for m in months:
    month_rows = sales[sales["month"] == str(m)]
    for cat_name, mixes in reasons.items():
        cat_skus = set(products[products.category == cat_name].sku)
        if cat_name == "Одежда":
            # «Одежа» — опечатка в выгрузке; после чистки в PQ эти SKU тоже Одежда
            cat_skus |= set(products[products.category == "Одежа"].sku)
        total_ret = int(month_rows.loc[month_rows["sku"].isin(cat_skus), "returns_units"].sum())
        weights = [(reason, share * rng.uniform(0.9, 1.1)) for reason, share in mixes]
        w_sum = sum(w for _, w in weights)
        rows_cat = [(reason, total_ret * w / w_sum) for reason, w in weights]
        ints = [int(round(v)) for _, v in rows_cat]
        residual = total_ret - sum(ints)          # контроль: причины сходятся в итог месяца
        ints[ints.index(max(ints))] += residual
        for (reason, _), v in zip(rows_cat, ints):
            rrows.append([str(m), cat_name, reason, v])
returns_df = pd.DataFrame(rrows, columns=["month", "category", "reason", "returns_units"])

# валидация: причины возвратов сходятся с returns_units из sales
assert returns_df["returns_units"].sum() == sales["returns_units"].sum(), "returns mismatch"

# ---------- 4. Сохранение ----------
products.to_csv(OUT / "products.csv", index=False, encoding="utf-8-sig")
sales[["ads_rub", "returns_cost_rub"]] = sales[["ads_rub", "returns_cost_rub"]].round().astype(int)
sales.to_csv(OUT / "sales_monthly.csv", index=False, encoding="utf-8-sig")
returns_df.to_csv(OUT / "returns_reasons.csv", index=False, encoding="utf-8-sig")
print(f"products.csv        {len(products)} строк")
print(f"sales_monthly.csv   {len(sales)} строк")
print(f"returns_reasons.csv {len(returns_df)} строк")

# ---------- 5. Валидация и инсайты ----------
rev = sales["revenue_rub"].sum()
prof = sales["profit_rub"].sum()
print(f"\nВыручка (выкупы): {rev:,.0f} ₽")
print(f"Прибыль:          {prof:,.0f} ₽   (маржа {prof/rev*100:.1f}%)")
by_cat = sales.merge(products[["sku", "category", "product_name"]], on="sku").groupby("category").agg(
    revenue=("revenue_rub", "sum"), profit=("profit_rub", "sum"))
by_cat["margin_%"] = (by_cat["profit"] / by_cat["revenue"] * 100).round(1)
print("\nПо категориям:")
print(by_cat.sort_values("revenue", ascending=False).to_string())
sku_prof = sales.merge(products[["sku", "product_name", "category"]], on="sku").groupby(
    ["sku", "product_name", "category"]).agg(revenue=("revenue_rub", "sum"), profit=("profit_rub", "sum"))
loss = sku_prof[sku_prof["profit"] < 0]
print(f"\nУбыточных SKU: {len(loss)} из {len(sku_prof)}")
print(sku_prof.sort_values("profit").head(6).to_string())
mon = sales.groupby("month").agg(revenue=("revenue_rub", "sum"), profit=("profit_rub", "sum"))
mon["margin_%"] = (mon["profit"] / mon["revenue"] * 100).round(1)
print("\nПо месяцам:")
print(mon.to_string())
ret_tot = sales["returns_units"].sum()
print(f"\nВозвратов: {ret_tot:,} шт ({ret_tot / sales['buyouts_units'].sum() * 100:.1f}% от выкупов)")
neg_months = (sales["profit_rub"] < 0).sum()
print(f"Убыточных месяцев (sku-месяцев): {neg_months} из {len(sales)} ({neg_months/len(sales)*100:.0f}%)")
loss_month = sales[sales["profit_rub"] < 0].merge(products[["sku", "product_name"]], on="sku")
print("\nУбыточные sku-месяцы:")
print(loss_month.groupby(["sku", "product_name"])["profit_rub"].agg(["count", "sum"]).to_string())
top = sku_prof.sort_values("profit", ascending=False).head(3)
print("\nТоп-3 SKU по прибыли:")
print(top.to_string())
