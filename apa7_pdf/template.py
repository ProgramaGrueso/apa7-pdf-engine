"""
APA 7 Document generator with standardized CSS and semantic HTML.
"""

from typing import Any, Dict, List, Optional


APA7_CSS = """
@page {
    size: letter;
    margin: 1in;
    @top-right {
        content: counter(page);
        font-family: 'Times New Roman', Times, serif;
        font-size: 12pt;
    }
}

body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 2.0;
    color: #000;
    margin: 0;
    padding: 0;
}

.title-page {
    text-align: center;
    page-break-after: always;
    padding-top: 2in;
}

.title-page h1 {
    font-size: 12pt;
    font-weight: bold;
    margin-bottom: 2em;
    line-height: 2.0;
}

.author-block {
    margin-bottom: 2em;
}

.running-head {
    position: fixed;
    top: -0.7in;
    right: 0;
    font-size: 12pt;
}

h1.section-title {
    font-size: 12pt;
    font-weight: bold;
    text-align: center;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}

h2.subsection-title {
    font-size: 12pt;
    font-weight: bold;
    text-align: left;
    margin-top: 1em;
    margin-bottom: 0.5em;
}

p {
    text-indent: 0.5in;
    margin: 0;
    text-align: justify;
}

p.no-indent {
    text-indent: 0;
}

/* APA 7 Tables: No vertical borders, only top, header bottom, and table bottom */
.apa-table-container {
    margin: 1.5em 0;
    page-break-inside: avoid;
}

.table-number {
    font-weight: bold;
    margin-bottom: 0;
    text-indent: 0;
}

.table-title {
    font-style: italic;
    margin-top: 0;
    margin-bottom: 0.5em;
    text-indent: 0;
}

table.apa-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 10.5pt;
    line-height: 1.4;
    border-top: 2px solid #000;
    border-bottom: 2px solid #000;
}

table.apa-table th {
    border-bottom: 1px solid #000;
    padding: 6pt 8pt;
    text-align: center;
    font-weight: normal;
}

table.apa-table td {
    padding: 5pt 8pt;
    border: none;
}

.table-note {
    font-size: 10pt;
    line-height: 1.4;
    margin-top: 0.5em;
    text-indent: 0;
}

.table-note em {
    font-style: italic;
}

/* References: Hanging indent 0.5 in */
.references-container {
    page-break-before: always;
}

.reference-entry {
    padding-left: 0.5in;
    text-indent: -0.5in;
    margin-bottom: 1em;
    line-height: 2.0;
}
"""


def build_apa7_document(
    title: str,
    author: str,
    institution: str,
    abstract: Optional[str] = None,
    sections: Optional[List[Dict[str, Any]]] = None,
    tables: Optional[List[Dict[str, Any]]] = None,
    references: Optional[List[str]] = None,
) -> str:
    """
    Constructs a complete APA 7 formatted HTML document.
    """
    sections = sections or []
    tables = tables or []
    references = references or []

    sections_html = []
    for s in sections:
        sec_title = f"<h2 class='subsection-title'>{s.get('title', '')}</h2>" if s.get('title') else ""
        paragraphs = "".join([f"<p>{p}</p>" for p in s.get("paragraphs", [])])
        sections_html.append(f"{sec_title}\n{paragraphs}")

    tables_html = []
    for t in tables:
        headers_str = "".join([f"<th>{h}</th>" for h in t.get("headers", [])])
        rows_str = ""
        for row in t.get("rows", []):
            cells = "".join([f"<td style='text-align: {t.get('align', 'center')};'>{cell}</td>" for cell in row])
            rows_str += f"<tr>{cells}</tr>\n"

        tables_html.append(f"""
        <div class="apa-table-container">
            <p class="table-number">{t.get('number', 'Table 1')}</p>
            <p class="table-title">{t.get('title', 'Descriptive Statistics')}</p>
            <table class="apa-table">
                <thead><tr>{headers_str}</tr></thead>
                <tbody>{rows_str}</tbody>
            </table>
            {f'<p class="table-note"><em>Note.</em> {t.get("note")}</p>' if t.get('note') else ''}
        </div>
        """)

    references_html = ""
    if references:
        ref_entries = "".join([f"<div class='reference-entry'>{ref}</div>" for ref in references])
        references_html = f"""
        <div class="references-container">
            <h1 class="section-title">References</h1>
            {ref_entries}
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{APA7_CSS}</style>
</head>
<body>

    <div class="title-page">
        <h1>{title}</h1>
        <div class="author-block">
            <p class="no-indent"><strong>{author}</strong></p>
            <p class="no-indent">{institution}</p>
        </div>
    </div>

    {f'''
    <div class="abstract-page" style="page-break-after: always;">
        <h1 class="section-title">Abstract</h1>
        <p class="no-indent">{abstract}</p>
    </div>
    ''' if abstract else ''}

    <div class="main-content">
        <h1 class="section-title">{title}</h1>
        {"<br/>".join(sections_html)}
        {"<br/>".join(tables_html)}
    </div>

    {references_html}

</body>
</html>
"""
    return html
