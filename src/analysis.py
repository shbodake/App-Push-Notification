def safe_rate(numerator, denominator):
    if denominator == 0:
        return 0
    return round((numerator / denominator) * 100, 2)

def generate_analysis(df):
    analysis = {}

    sent = len(df)
    delivered = int(df["Delivered"].sum())
    opened = int(df["Opened"].sum())
    clicked = int(df["Clicked"].sum())
    converted = int(df["Converted"].sum())
    revenue = float(df["Order_Value"].sum())

    analysis["Total Notifications Sent"] = sent
    analysis["Total Delivered"] = delivered
    analysis["Delivery Rate"] = safe_rate(delivered, sent)
    analysis["Total Opened"] = opened
    analysis["Open Rate"] = safe_rate(opened, delivered)
    analysis["Total Clicked"] = clicked
    analysis["CTR"] = safe_rate(clicked, delivered)
    analysis["Total Conversions"] = converted
    analysis["Conversion Rate"] = safe_rate(converted, delivered)
    analysis["Total Revenue"] = round(revenue, 2)
    analysis["Average Order Value"] = round(
        revenue / converted, 2
    ) if converted else 0

    campaign_revenue = (
        df.groupby("Campaign_Name")["Order_Value"]
        .sum()
        .sort_values(ascending=False)
    )
    analysis["Highest Revenue Campaign"] = campaign_revenue.index[0]

    segment_open = (
        df.groupby("Customer_Segment")["Opened"]
        .mean()
        .sort_values(ascending=False)
    )
    analysis["Highest Engagement Segment"] = segment_open.index[0]

    return analysis

def save_business_insights(analysis, file_path):
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("PUSH NOTIFICATION CAMPAIGN ANALYSIS\n")
        file.write("=" * 45 + "\n\n")

        for key, value in analysis.items():
            file.write(f"{key}: {value}\n")
