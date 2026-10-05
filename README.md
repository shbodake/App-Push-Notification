# App Push Notification Campaign Analysis

## Project Objective
Analyze app push notification campaign performance across delivery, engagement,
click-through, conversion, revenue, platform, customer segment, notification type,
and send hour.

## Important
The 50,000-row dataset in this project is **synthetic portfolio data**. It is designed
to resemble realistic app push notification campaign data and must not be presented
as actual Netcore customer/company data.

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- SQL / MySQL
- Power BI
- ReportLab

## Dataset
50,000 notification records from January to June 2026.

Columns:
Notification_ID, Campaign_ID, Campaign_Name, Customer_ID, Campaign_Date,
Platform, Device_Type, Customer_Segment, Notification_Type, Sent_Time,
Notification_Status, Delivered, Opened, Clicked, Converted, Order_Value, Unsubscribe

## Run
From the project root:

```bash
pip install -r requirements.txt
python main.py
```

## Expected output
- Cleaned CSV in `data/processed/`
- 9 PNG charts in `outputs/graphs/`
- Business insights in `outputs/analysis/`
- PDF report in `outputs/reports/`

## Portfolio / Resume
Use this as a portfolio project separately from actual Netcore work.

Suggested resume title:
**App Push Notification Campaign Analysis | Python, SQL, Power BI**

Suggested bullets:
- Analyzed synthetic app push notification data to evaluate delivery, engagement,
  CTR, conversion, and revenue KPIs.
- Cleaned and transformed 50K notification records using Python and Pandas.
- Used SQL aggregations and CTEs to analyze campaign, platform, segment, and
  notification-type performance.
- Built a Power BI dashboard to monitor campaign KPIs and identify engagement trends.
