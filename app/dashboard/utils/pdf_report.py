import unicodedata
from io import BytesIO

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


class PDFReport:

    @staticmethod
    def generate(latest: dict):

        buffer = BytesIO()

        doc = SimpleDocTemplate(
            buffer,
            leftMargin=40,
            rightMargin=40,
            topMargin=40,
            bottomMargin=40,
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "TitleStyle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            textColor=HexColor("#1F4E79"),
            spaceAfter=18,
        )

        heading_style = ParagraphStyle(
            "HeadingStyle",
            parent=styles["Heading2"],
            textColor=HexColor("#1F4E79"),
            spaceBefore=12,
            spaceAfter=8,
        )

        body_style = ParagraphStyle(
            "BodyStyle",
            parent=styles["BodyText"],
            leading=20,
            spaceAfter=8,
        )

        footer_style = ParagraphStyle(
            "FooterStyle",
            parent=styles["Italic"],
            alignment=TA_CENTER,
            textColor=HexColor("#666666"),
        )

        story = []

        # =====================================================
        # Header
        # =====================================================

        story.append(
            Paragraph(
                "RetailPulse AI",
                title_style,
            )
        )

        story.append(
            Paragraph(
                "<b>AI Business Insights Report</b>",
                heading_style,
            )
        )

        story.append(
            HRFlowable(
                width="100%",
                thickness=1,
                color=HexColor("#CFCFCF"),
            )
        )

        story.append(Spacer(1, 18))

        # =====================================================
        # Report Information
        # =====================================================

        story.append(
            Paragraph(
                "<b>Question</b>",
                heading_style,
            )
        )

        story.append(
            Paragraph(
                latest["question"],
                body_style,
            )
        )

        story.append(
            Paragraph(
                f"<b>Model:</b> {latest['model']}",
                body_style,
            )
        )

        story.append(
            Paragraph(
                f"<b>Generated:</b> {latest['generated_at']}",
                body_style,
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            HRFlowable(
                width="100%",
                thickness=0.8,
                color=HexColor("#DDDDDD"),
            )
        )

        story.append(Spacer(1, 16))

        # =====================================================
        # Clean AI Response
        # =====================================================

        response = latest["response"]

        replacements = {
            "–": "-",
            "—": "-",
            "•": "-",
            "●": "-",
            "▪": "-",
            "■": "",
            "“": '"',
            "”": '"',
            "‘": "'",
            "’": "'",
        }

        for old, new in replacements.items():
            response = response.replace(old, new)

        response = unicodedata.normalize("NFKD", response)

        response = response.encode(
            "ascii",
            "ignore"
        ).decode("ascii")


        lines = response.splitlines()

        # =====================================================
        # Render Markdown
        # =====================================================

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # ## Heading
            if line.startswith("## "):

                story.append(
                    Paragraph(
                        f"<b>{line[3:]}</b>",
                        heading_style,
                    )
                )

                continue

            # **Heading**
            if (
                line.startswith("**")
                and line.endswith("**")
            ):

                title = line.replace("**", "")

                story.append(
                    Paragraph(
                        f"<b>{title}</b>",
                        heading_style,
                    )
                )

                continue

            # Numbered list
            if (
                len(line) > 2
                and line[0].isdigit()
                and line[1] == "."
            ):

                story.append(
                    Paragraph(
                        line,
                        body_style,
                    )
                )

                continue

            # Bullet list
            if line.startswith("- "):

                story.append(
                    Paragraph(
                        f"• {line[2:]}",
                        body_style,
                    )
                )

                continue

            # Normal paragraph
            story.append(
                Paragraph(
                    line,
                    body_style,
                )
            )

        story.append(Spacer(1, 24))

        story.append(
            HRFlowable(
                width="100%",
                thickness=0.8,
                color=HexColor("#DDDDDD"),
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            Paragraph(
                "Generated by RetailPulse AI",
                footer_style,
            )
        )

        story.append(
            Paragraph(
                "Confidential Business Analytics Report",
                footer_style,
            )
        )

        doc.build(story)

        pdf = buffer.getvalue()

        buffer.close()

        return pdf