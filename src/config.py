import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(
    BASE_DIR, "data", "raw", "push_notification_data.csv"
)

PROCESSED_DATA_PATH = os.path.join(
    BASE_DIR, "data", "processed", "push_notification_cleaned.csv"
)

GRAPH_PATH = os.path.join(BASE_DIR, "outputs", "graphs")

ANALYSIS_PATH = os.path.join(
    BASE_DIR, "outputs", "analysis", "business_insights.txt"
)

REPORT_PATH = os.path.join(
    BASE_DIR, "outputs", "reports",
    "Push_Notification_Analysis_Report.pdf"
)
