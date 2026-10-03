"""
apa7-pdf-engine
~~~~~~~~~~~~~~~

Strict, publication-grade APA 7 PDF report generator powered by Headless Chromium.
"""

from .compiler import compile_html_to_pdf, find_browser_executable
from .template import build_apa7_document

__version__ = "0.1.0"
__all__ = ["compile_html_to_pdf", "build_apa7_document", "find_browser_executable"]
