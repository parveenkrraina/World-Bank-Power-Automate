from pathlib import Path
import argparse
import re
import markdown
from xhtml2pdf import pisa


def _strip_front_matter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)


def _link_callback(uri: str, base_path: Path) -> str:
    if uri.startswith(("http://", "https://", "data:")):
        return uri

    candidate = Path(uri)
    if not candidate.is_absolute():
        candidate = (base_path / candidate).resolve()

    return str(candidate)


def convert_markdown_to_pdf(markdown_path: Path, pdf_path: Path) -> None:
    text = _strip_front_matter(markdown_path.read_text(encoding="utf-8"))
    html_body = markdown.markdown(text, extensions=["extra", "sane_lists", "toc"])
    html = f"""
    <html>
    <head>
        <meta charset=\"utf-8\" />
        <style>
            body {{ font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.4; }}
            h1, h2, h3 {{ color: #1f2937; }}
            code {{ background: #f3f4f6; padding: 1px 3px; }}
            pre {{ background: #f3f4f6; padding: 8px; white-space: pre-wrap; }}
            table {{ border-collapse: collapse; width: 100%; margin: 8px 0; }}
            th, td {{ border: 1px solid #d1d5db; padding: 6px; text-align: left; }}
            img {{ max-width: 100%; height: auto; }}
            blockquote {{ border-left: 3px solid #9ca3af; margin: 0; padding-left: 10px; color: #374151; }}
        </style>
    </head>
    <body>{html_body}</body>
    </html>
    """

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with pdf_path.open("wb") as output_file:
        result = pisa.CreatePDF(
            src=html,
            dest=output_file,
            link_callback=lambda uri, _: _link_callback(uri, markdown_path.parent),
        )
    if result.err:
        raise RuntimeError("PDF generation failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF")
    parser.add_argument("input", type=Path, help="Path to markdown file")
    parser.add_argument("output", type=Path, help="Path to output PDF")
    args = parser.parse_args()

    convert_markdown_to_pdf(args.input, args.output)
    print(f"Created: {args.output}")
