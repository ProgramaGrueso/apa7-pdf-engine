"""
Compiler module: renders HTML strings or files to PDF via headless Chromium/Chrome.
"""

import os
import shutil
import subprocess
import tempfile
from typing import Optional


def find_browser_executable() -> str:
    """Finds available Chromium, Google Chrome or Brave executable on the system."""
    for binary in ["chromium", "google-chrome-stable", "google-chrome", "brave", "chromium-browser"]:
        path = shutil.which(binary)
        if path:
            return path
    raise FileNotFoundError(
        "Could not find Chromium or Chrome executable in PATH. "
        "Please install chromium (e.g. sudo apt install chromium-browser / sudo pacman -S chromium)."
    )


def compile_html_to_pdf(html_content: str, output_pdf_path: str, browser_path: Optional[str] = None) -> str:
    """
    Compiles an APA 7 compliant HTML string into a PDF using headless Chromium.

    Args:
        html_content: Complete HTML document string.
        output_pdf_path: Path where the output PDF will be saved.
        browser_path: Optional path to chromium executable.

    Returns:
        Absolute path to the generated PDF.
    """
    if browser_path is None:
        browser_path = find_browser_executable()

    abs_output = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(abs_output) or ".", exist_ok=True)

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(html_content)
        tmp_html_path = tmp.name

    try:
        cmd = [
            browser_path,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={abs_output}",
            "--no-pdf-header-footer",
            tmp_html_path,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if not os.path.exists(abs_output) or os.path.getsize(abs_output) == 0:
            raise RuntimeError(f"PDF generation failed: {result.stderr}")
        return abs_output
    finally:
        if os.path.exists(tmp_html_path):
            os.remove(tmp_html_path)
