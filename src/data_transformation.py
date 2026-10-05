def transform_data(df):
    df = df.copy()

    df["Hour"] = df["Sent_Time"].apply(lambda x: x.hour)
    df["Day_Name"] = df["Campaign_Date"].dt.day_name()
    df["Month"] = df["Campaign_Date"].dt.month
    df["Month_Name"] = df["Campaign_Date"].dt.month_name()

    return df
