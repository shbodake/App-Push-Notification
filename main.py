import os

from src.config import GRAPH_PATH, ANALYSIS_PATH, REPORT_PATH
from src.data_loader import load_data
from src.data_cleaning import clean_data, save_cleaned_data
from src.data_transformation import transform_data
from src.analysis import generate_analysis, save_business_insights
from src.visualization import create_visualization
from src.report import create_report

def main():
    print("Loading data...")
    df = load_data()
    print(f"Raw rows: {len(df)}")

    print("Cleaning data...")
    df = clean_data(df)
    print(f"Cleaned rows: {len(df)}")
    save_cleaned_data(df)

    print("Transforming data...")
    df = transform_data(df)

    print("Generating analysis...")
    analysis = generate_analysis(df)

    print("Saving business insights...")
    save_business_insights(analysis, ANALYSIS_PATH)

    print("Creating visualizations...")
    create_visualization(df, GRAPH_PATH)

    print("Creating PDF report...")
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    create_report(analysis, REPORT_PATH)

    print("\nApp Push Notification Analysis Completed Successfully!")
    print(f"Processed data: {os.path.abspath('data/processed/push_notification_cleaned.csv')}")
    print(f"Insights: {ANALYSIS_PATH}")
    print(f"Graphs: {GRAPH_PATH}")
    print(f"Report: {REPORT_PATH}")

if __name__ == "__main__":
    main()
