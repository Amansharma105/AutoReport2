## AutoReport

AutoReport is a Python-based Command Line Interface (CLI) application for automated report generation and data analysis. It supports multiple data sources, performs statistical analysis, generates charts, and creates HTML and PDF reports.

## Features

- CLI using Typer
- Project setup
- Organized folder structure
- Easy to extend
- CSV data loading
- Excel data loading
- JSON data loading
- SQLite database support
- Statistical analysis (Mean, Median, Mode, Standard Deviation)
- Bar Chart
- Line Chart
- Pie Chart
- Scatter Plot
- HTML report generation using Jinja2 - PDF report generation
- Automated testing with Pytest

 ## Project Structure

```text
AutoReport/
│
├── data/
│   ├── sample.csv
│   ├── sample.json
│   └── sample.xlsx
│
├── charts/
│   └── chart_generator.py
│
├── templates/
│   └── report.html
│
├── reports/
│   └── pdf_report.py
│
├── tests/
│   └── test_main.py
│
├── main.py
├── data_loader.py
├── data_sources.py
├── analysis.py
├── report_generator.py
├── pyproject.toml
└── README.md
```

### Technologies Used

- Python
- Typer
- Pandas
- Matplotlib
- Jinja2
- ReportLab
- SQLite
- Pytest

---

## Installation

```bash
pip install pandas typer matplotlib jinja2 reportlab pytest
```

---

## Usage

```bash
python main.py
```

---

## Testing

```bash
pytest
```

---

## Status

✅ Project Completed Successfully

---

## Author

### Aman Sharma
