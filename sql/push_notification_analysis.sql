-- MySQL-compatible analysis queries
-- Table name: push_notifications

-- 1. Overall KPIs
SELECT
    COUNT(*) AS total_notifications_sent,
    SUM(Delivered) AS total_delivered,
    ROUND(SUM(Delivered) * 100.0 / NULLIF(COUNT(*), 0), 2) AS delivery_rate,
    SUM(Opened) AS total_opened,
    ROUND(SUM(Opened) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS open_rate,
    SUM(Clicked) AS total_clicked,
    ROUND(SUM(Clicked) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS ctr,
    SUM(Converted) AS total_conversions,
    ROUND(SUM(Converted) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS conversion_rate,
    ROUND(SUM(Order_Value), 2) AS total_revenue
FROM push_notifications;

-- 2. Campaign performance
WITH campaign_metrics AS (
    SELECT
        Campaign_Name,
        COUNT(*) AS sent,
        SUM(Delivered) AS delivered,
        SUM(Opened) AS opened,
        SUM(Clicked) AS clicked,
        SUM(Converted) AS conversions,
        SUM(Order_Value) AS revenue
    FROM push_notifications
    GROUP BY Campaign_Name
)
SELECT
    Campaign_Name,
    sent,
    delivered,
    ROUND(delivered * 100.0 / NULLIF(sent, 0), 2) AS delivery_rate,
    ROUND(opened * 100.0 / NULLIF(delivered, 0), 2) AS open_rate,
    ROUND(clicked * 100.0 / NULLIF(delivered, 0), 2) AS ctr,
    ROUND(conversions * 100.0 / NULLIF(delivered, 0), 2) AS conversion_rate,
    ROUND(revenue, 2) AS revenue
FROM campaign_metrics
ORDER BY revenue DESC;

-- 3. Platform performance
SELECT
    Platform,
    COUNT(*) AS sent,
    SUM(Delivered) AS delivered,
    SUM(Opened) AS opened,
    ROUND(SUM(Opened) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS open_rate,
    SUM(Clicked) AS clicked,
    ROUND(SUM(Clicked) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS ctr
FROM push_notifications
GROUP BY Platform
ORDER BY open_rate DESC;

-- 4. Customer segment performance
SELECT
    Customer_Segment,
    COUNT(*) AS sent,
    SUM(Opened) AS opened,
    ROUND(SUM(Opened) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS open_rate,
    SUM(Converted) AS conversions,
    ROUND(SUM(Order_Value), 2) AS revenue
FROM push_notifications
GROUP BY Customer_Segment
ORDER BY revenue DESC;

-- 5. Notification type performance
SELECT
    Notification_Type,
    COUNT(*) AS sent,
    SUM(Delivered) AS delivered,
    SUM(Opened) AS opened,
    ROUND(SUM(Opened) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS open_rate,
    SUM(Converted) AS conversions,
    ROUND(SUM(Order_Value), 2) AS revenue
FROM push_notifications
GROUP BY Notification_Type
ORDER BY revenue DESC;

-- 6. Hourly performance
SELECT
    HOUR(STR_TO_DATE(Sent_Time, '%H:%i')) AS send_hour,
    COUNT(*) AS sent,
    SUM(Delivered) AS delivered,
    SUM(Opened) AS opened,
    ROUND(SUM(Opened) * 100.0 / NULLIF(SUM(Delivered), 0), 2) AS open_rate,
    SUM(Converted) AS conversions
FROM push_notifications
GROUP BY send_hour
ORDER BY send_hour;
