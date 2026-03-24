<div align="center">

# 📄 resume-cli-py

**Generate a clean, professional resume straight from your terminal — no UI, no fluff.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![CLI](https://img.shields.io/badge/Tool-CLI-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-orange?style=flat-square)

</div>

---

## 🚀 What It Does

`resume-cli-py` is a lightweight Python CLI app that collects your details interactively and generates a neatly formatted resume — saved as `.txt`, with optional `.pdf` export.

No templates, no login, no cloud. Just Python.

---

## ✨ Features

- 🖊️ Interactive prompts — just answer the questions
- 📁 Auto-saves to `output/resume.txt`
- 📄 Optional PDF export via `reportlab`
- 🧱 Clean modular code (`main.py` + `generator.py`)
- 🐍 Zero external dependencies for core functionality

---

## 🗂️ Project Structure
```text
resume-cli-py/
├── main.py          # CLI input and app flow
├── generator.py     # Resume formatting + file generation
├── output/          # Generated files land here
│   ├── resume.txt
│   └── resume.pdf   # (optional)
└── README.md
```

---

## ⚡ Quick Start

### Prerequisites

- Python 3.9 or newer

### Run
```bash
git clone https://github.com/ashish7802/resume-cli-py.git
cd resume-cli-py
python3 main.py
```

### You'll be prompted for

| Field | Example Input |
|---|---|
| Full Name | `Ashish Yadav` |
| Skills | `Python, SQL, Communication` |
| Education | `B.Tech Computer Science, XYZ University` |
| Projects | `Resume CLI, Portfolio Website` |

---

## 🧾 Sample Output
```
==========================
         RESUME
==========================

Name: Ashish Yadav

Skills:
  - Python
  - SQL
  - Communication

Education:
  - B.Tech Computer Science, XYZ University

Projects:
  - Resume CLI
  - Portfolio Website

==========================
```

---

## 📦 Optional PDF Export
```bash
pip install reportlab
```

When prompted during the run, choose `y` to export PDF.
If `reportlab` is not installed, the app continues and saves `resume.txt` automatically.

---

## 🛠️ Built With

- [Python 3.9+](https://www.python.org/)
- [reportlab](https://pypi.org/project/reportlab/) *(optional — PDF only)*

---

## 👨‍💻 Author

**Ashish Yadav** — Full Stack Developer & AI Builder

[![Portfolio](https://img.shields.io/badge/Portfolio-ashyadav.netlify.app-blue?style=flat-square)](https://ashyadav.netlify.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/ashish-yadav-ab206124a)
[![GitHub](https://img.shields.io/badge/GitHub-ashish7802-181717?style=flat-square&logo=github)](https://github.com/ashish7802)

---

## 📜 License

MIT License — free to use, fork, and build on.

---

<div align="center">

⭐ **If this saved you time, drop a star!** ⭐

</div>
