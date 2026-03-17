# Data Science Project: Global Video Game Sales Analysis 🎮

This project analyzes global video game sales trends using **Python**, **NumPy**, **Pandas**, and **Matplotlib**.  
It satisfies the requirements for the Applied Sciences course at **Thomas More**.

---

## 📁 Repository Structure

- **data/**: Contains the original and cleaned datasets.  
- **scripts/**: Python scripts for data cleaning using Regex.  
- **notebooks/**: Jupyter Notebooks for NumPy and Pandas analysis.  
- **README.md**: Setup instructions and project documentation.

---

## 🚀 Setup Instructions for Team Members

Follow these steps to ensure the project runs correctly on your machine.

### Option 1: Clone the Repository

Open your terminal (or VS Code) and run:

```powershell
git clone https://github.com/danmwix/data-science-project.git
cd data-science-project

Option 2: Download as ZIP

Go to the GitHub repository page.

Click Code → Download ZIP.

Extract the ZIP file to a folder of your choice.

Open a terminal in the extracted folder.

2. Create the Virtual Environment

We are using Python 3.13.2. Create a virtual environment to keep dependencies isolated:

python -m venv venv
3. Activate the Environment

Windows (PowerShell):

.\venv\Scripts\Activate.ps1

Mac/Linux:

source venv/bin/activate

You should see (venv) at the start of your command line.

4. Install Dependencies
pip install pandas numpy matplotlib seaborn notebook
NB: 🛠 Fixing "Import Could Not Be Resolved" (VS Code)

If you see yellow squiggles under import pandas or import numpy, VS Code is not using the correct interpreter:

Open clean_data.py or one of the notebooks.

Press Ctrl + Shift + P and type Python: Select Interpreter.

Choose the interpreter labeled Python 3.13.x ('venv': venv).

For notebooks: Click Select Kernel in the top right corner and choose the same venv path.

🔍 How to Run the Project
Phase 1: Data Cleaning

Run the Regex cleaning script:

python scripts/clean_data.py

This will generate data/vgsales_cleaned.csv.

Phase 2 & 3: Analysis

Open the notebooks in the notebooks/ folder and click Run All.

⚠️ Challenges & Troubleshooting
Challenge	Cause	Fix
KeyboardInterrupt / Hanging	OneDrive syncing while creating venv	Delete venv folder and run python -m venv venv again; wait 60s
ImportError (Matplotlib)	Corrupted install or interrupted pip	Run pip install --upgrade --force-reinstall matplotlib
FileNotFoundError	Notebook looking in the wrong directory	Ensure the path is ../data/vgsales_cleaned.csv if running inside notebooks/
Regex Issues	Year column contained floats (2008.0)	Used re.search(r'(\d{4})') to extract only the 4-digit integer
🎓 Project Highlights (For Presentation)

Regex: Cleaned non-ASCII characters from game titles (like "Pokémon") and grouped console platforms into Sony, Nintendo, and Microsoft brands.

NumPy: Performed statistical analysis (Mean, Std Dev) on 16,000+ rows.

Pandas: Used Pivot Tables and Heatmaps to show that specific publishers dominate certain genres (e.g., Electronic Arts owns the Sports genre).
