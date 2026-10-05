import os
import matplotlib.pyplot as plt

def _save_bar(series, title, ylabel, path, rotation=0):
    plt.figure(figsize=(10, 5))
    series.plot(kind="bar")
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel("")
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()

def create_visualization(df, graph_path):
    os.makedirs(graph_path, exist_ok=True)

    campaign = df.groupby("Campaign_Name").agg(
        Sent=("Notification_ID", "count"),
        Delivered=("Delivered", "sum"),
        Opened=("Opened", "sum"),
        Clicked=("Clicked", "sum"),
        Converted=("Converted", "sum"),
        Revenue=("Order_Value", "sum")
    )

    _save_bar(
        campaign["Delivered"] / campaign["Sent"] * 100,
        "Campaign Delivery Rate", "Delivery Rate (%)",
        os.path.join(graph_path, "campaign_delivery_rate.png"), 35
    )

    _save_bar(
        campaign["Opened"] / campaign["Delivered"] * 100,
        "Campaign Open Rate", "Open Rate (%)",
        os.path.join(graph_path, "campaign_open_rate.png"), 35
    )

    _save_bar(
        campaign["Clicked"] / campaign["Delivered"] * 100,
        "Campaign CTR", "CTR (%)",
        os.path.join(graph_path, "campaign_ctr.png"), 35
    )

    _save_bar(
        campaign["Converted"] / campaign["Delivered"] * 100,
        "Campaign Conversion Rate", "Conversion Rate (%)",
        os.path.join(graph_path, "campaign_conversion_rate.png"), 35
    )

    _save_bar(
        campaign["Revenue"].sort_values(ascending=False),
        "Campaign Revenue", "Revenue",
        os.path.join(graph_path, "campaign_revenue.png"), 35
    )

    platform = df.groupby("Platform").agg(
        Delivered=("Delivered", "sum"),
        Opened=("Opened", "sum"),
        Clicked=("Clicked", "sum"),
        Converted=("Converted", "sum")
    )
    platform["Open_Rate"] = platform["Opened"] / platform["Delivered"] * 100
    _save_bar(
        platform["Open_Rate"],
        "Platform Open Rate", "Open Rate (%)",
        os.path.join(graph_path, "platform_performance.png")
    )

    ntype = df.groupby("Notification_Type").agg(
        Delivered=("Delivered", "sum"),
        Opened=("Opened", "sum")
    )
    ntype["Open_Rate"] = ntype["Opened"] / ntype["Delivered"] * 100
    _save_bar(
        ntype["Open_Rate"].sort_values(ascending=False),
        "Notification Type Open Rate", "Open Rate (%)",
        os.path.join(graph_path, "notification_type_performance.png"), 30
    )

    segment = df.groupby("Customer_Segment").agg(
        Delivered=("Delivered", "sum"),
        Opened=("Opened", "sum")
    )
    segment["Open_Rate"] = segment["Opened"] / segment["Delivered"] * 100
    _save_bar(
        segment["Open_Rate"].sort_values(ascending=False),
        "Customer Segment Open Rate", "Open Rate (%)",
        os.path.join(graph_path, "customer_segment_performance.png"), 25
    )

    hourly = df.groupby("Hour").agg(
        Delivered=("Delivered", "sum"),
        Opened=("Opened", "sum")
    )
    hourly["Open_Rate"] = hourly["Opened"] / hourly["Delivered"] * 100
    _save_bar(
        hourly["Open_Rate"],
        "Hourly Notification Performance", "Open Rate (%)",
        os.path.join(graph_path, "hourly_performance.png")
    )
