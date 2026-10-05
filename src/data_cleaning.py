import os
import pandas as pd
from src.config import PROCESSED_DATA_PATH

def clean_data(df):
    df = df.copy()
    df = df.drop_duplicates()

    text_columns = [
        "Notification_ID", "Campaign_ID", "Campaign_Name",
        "Customer_ID", "Platform", "Device_Type",
        "Customer_Segment", "Notification_Type",
        "Notification_Status"
    ]

    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

    df["Campaign_Date"] = pd.to_datetime(
        df["Campaign_Date"], errors="coerce"
    )

    df["Sent_Time"] = pd.to_datetime(
        df["Sent_Time"], format="%H:%M", errors="coerce"
    ).dt.time

    numeric_columns = [
        "Delivered", "Opened", "Clicked", "Converted",
        "Order_Value", "Unsubscribe"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in ["Delivered", "Opened", "Clicked", "Converted", "Unsubscribe"]:
        df[col] = df[col].fillna(0).astype(int)

    df["Order_Value"] = df["Order_Value"].fillna(0)

    df = df.dropna(subset=["Campaign_Date", "Sent_Time"])

    for col in ["Delivered", "Opened", "Clicked", "Converted", "Unsubscribe"]:
        df = df[df[col].isin([0, 1])]

    df = df.reset_index(drop=True)
    return df

def save_cleaned_data(df):
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Cleaned data saved to: {PROCESSED_DATA_PATH}")
