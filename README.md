# 📄 apa7-pdf-engine

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Chromium](https://img.shields.io/badge/Engine-Headless_Chromium-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.chromium.org)
[![APA Style](https://img.shields.io/badge/Format-APA_7th_Edition-008080?style=for-the-badge)](https://apastyle.apa.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<p align="center">
  <strong>Strict, publication-grade APA 7th Edition PDF report generator powered by Headless Chromium. Pure CSS/HTML print engine without ReportLab boilerplate or WeasyPrint page-break bugs.</strong>
</p>

</div>

---

## 📌 Problem

Programmatically generating academic or professional statistical reports in Python typically requires:
- **ReportLab**: Rigid, verbose coordinate-based canvas code with manual page wrap calculations.
- **WeasyPrint / wkhtmltopdf**: Frequently break complex multi-column scientific tables, hanging indents, and running headers across pages.
- **Word / DOCX Automation**: Requires external office suites and lacks reproducible CLI automation.

## 💡 The Solution

`apa7-pdf-engine` pairs semantic HTML generation with exact **APA 7th Edition CSS print rules** rendered via **Headless Chromium** (`--print-to-pdf --no-pdf-header-footer`):
- **1-inch (2.54 cm) margins** on letter paper.
- **Times New Roman 12 pt** with double line spacing (`line-height: 2.0`).
- **First-line paragraph indentation** (0.5 in).
- **Strict APA Table borders**: Clean top border, header separator, and bottom border (zero vertical grid lines).
- **References page**: Automatic hanging indent (0.5 in) with page breaks.
- **Running Head**: Standardized header and automatic page numbering in the top-right corner.

---

## 🛠 Prerequisites

Requires Chromium or Google Chrome installed on your system:

```bash
# Arch / CachyOS / Manjaro
sudo pacman -S chromium

# Debian / Ubuntu
sudo apt install chromium-browser # or google-chrome-stable

# Fedora
sudo dnf install chromium
```

---

## 🚀 Installation & Usage

```bash
git clone https://github.com/ProgramaGrueso/apa7-pdf-engine.git
cd apa7-pdf-engine
pip install -e .
```

### Quick Example

```python
from apa7_pdf import build_apa7_document, compile_html_to_pdf

# 1. Build document structure
html = build_apa7_document(
    title="Effect of Cognitive Bias on Probabilistic Estimation",
    author="Dr. Jane Doe",
    institution="Department of Data Science, University of Technology",
    abstract="This study investigates heuristic shortcuts in high-stakes decisions...",
    sections=[
        {
            "title": "Methodology",
            "paragraphs": [
                "Data collection occurred across 500 consecutive test subjects...",
                "Statistical distributions were evaluated using non-parametric methods."
            ]
        }
    ],
    tables=[
        {
            "number": "Table 1",
            "title": "Descriptive Statistics for Experimental Cohort",
            "headers": ["Group", "Sample Size (n)", "Mean (M)", "SD"],
            "rows": [
                ["Control", "250", "45.2", "8.1"],
                ["Treatment", "250", "62.8", "7.4"]
            ],
            "note": "SD = standard deviation."
        }
    ],
    references=[
        "Kahneman, D., & Tversky, A. (1972). Subjective probability. <em>Cognitive Psychology</em>, 3(3), 430–454."
    ]
)

# 2. Compile to publication-ready PDF in < 1 second
compile_html_to_pdf(html, "APA7_Report.pdf")
```

### Run Sample Generator

```bash
python examples/generate_sample_report.py
```

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
