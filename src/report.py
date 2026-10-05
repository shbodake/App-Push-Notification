from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_report(analysis, report_path):
    document = SimpleDocTemplate(report_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph(
            "App Push Notification Campaign Analysis",
            styles["Title"]
        )
    )
    story.append(Spacer(1, 20))
    story.append(Paragraph("Business Insights", styles["Heading2"]))
    story.append(Spacer(1, 10))

    for key, value in analysis.items():
        story.append(
            Paragraph(f"<b>{key}:</b> {value}", styles["Normal"])
        )
        story.append(Spacer(1, 8))

    document.build(story)
