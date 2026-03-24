"""Resume formatting and file generation utilities."""

from pathlib import Path


SECTION_WIDTH = 60


def parse_comma_separated(raw_value: str) -> list[str]:
    """Return cleaned list items from comma-separated text."""
    items = [item.strip() for item in raw_value.split(",")]
    return [item for item in items if item]


def _format_section(title: str, items: list[str]) -> str:
    """Format one resume section with a title and bullet points."""
    divider = "-" * SECTION_WIDTH
    lines = [title.upper(), divider]

    if items:
        lines.extend(f"• {item}" for item in items)
    else:
        lines.append("• Not provided")

    return "\n".join(lines)


def build_resume_text(
    *,
    name: str,
    skills: list[str],
    education: list[str],
    projects: list[str],
) -> str:
    """Build a clean plain-text resume from user input."""
    name_line = name.strip().upper()
    name_underline = "=" * max(len(name_line), 8)

    sections = [
        _format_section("Skills", skills),
        _format_section("Education", education),
        _format_section("Projects", projects),
    ]

    return "\n\n".join([name_line, name_underline, *sections]) + "\n"


def save_resume_txt(content: str, file_path: Path) -> None:
    """Save resume content to a UTF-8 text file."""
    file_path.write_text(content, encoding="utf-8")


def save_resume_pdf(content: str, file_path: Path) -> bool:
    """Save resume as PDF if reportlab is available.

    Returns True when a PDF is created, otherwise False.
    """
    try:
        from reportlab.lib.pagesizes import LETTER
        from reportlab.pdfgen import canvas
    except ImportError:
        return False

    pdf = canvas.Canvas(str(file_path), pagesize=LETTER)
    width, height = LETTER

    left_margin = 50
    y = height - 50

    for line in content.splitlines():
        pdf.drawString(left_margin, y, line)
        y -= 16

        if y < 50:
            pdf.showPage()
            y = height - 50

    pdf.save()
    return True
