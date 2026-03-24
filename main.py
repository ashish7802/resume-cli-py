"""CLI entry point for resume-generator-cli.

This module collects user input and delegates resume generation to generator.py.
"""

from pathlib import Path

from generator import build_resume_text, parse_comma_separated, save_resume_pdf, save_resume_txt

OUTPUT_DIR = Path("output")


def prompt_list(field_name: str) -> list[str]:
    """Prompt for a comma-separated list and return cleaned items."""
    raw = input(f"Enter {field_name} (comma-separated): ").strip()
    return parse_comma_separated(raw)


def main() -> None:
    """Collect inputs and generate resume files."""
    print("=== Resume Generator CLI ===")

    name = input("Enter your full name: ").strip()
    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter your full name: ").strip()

    skills = prompt_list("skills")
    education = prompt_list("education")
    projects = prompt_list("projects")

    resume_text = build_resume_text(
        name=name,
        skills=skills,
        education=education,
        projects=projects,
    )

    OUTPUT_DIR.mkdir(exist_ok=True)

    txt_path = OUTPUT_DIR / "resume.txt"
    save_resume_txt(resume_text, txt_path)
    print(f"\nResume saved: {txt_path}")

    create_pdf = input("Do you also want a PDF version? (y/n): ").strip().lower()
    if create_pdf == "y":
        pdf_path = OUTPUT_DIR / "resume.pdf"
        created = save_resume_pdf(resume_text, pdf_path)
        if created:
            print(f"Resume saved: {pdf_path}")
        else:
            print("PDF generation skipped. Install 'reportlab' to enable PDF output.")

    print("\nDone! Your resume has been generated.")


if __name__ == "__main__":
    main()
