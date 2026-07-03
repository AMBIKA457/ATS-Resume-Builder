from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(name, resume_text):

    filename = "resume.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(name, styles["Title"])
    )

    story.append(Spacer(1, 20))

    for line in resume_text.split("\n"):
        if line.strip():
            story.append(
                Paragraph(line, styles["BodyText"])
            )
            story.append(Spacer(1, 5))

    doc.build(story)

    return filename