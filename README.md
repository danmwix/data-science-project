# 🎮 Global Video Game Sales Analysis

This project analyzes global video game sales trends using **Python**, **NumPy**, **Pandas**, and **Matplotlib**.
It is developed to meet the requirements of the *Applied Sciences course at Thomas More*. 
The dataset used was obtained from Kaggle: https://www.kaggle.com/datasets/gregorut/videogamesales which derived it's game entries from the site https://www.vgchartz.com/gamedb/

---

## 📁 Repository Structure

```
data/
│── Contains the original and cleaned datasets

figures/
│── Contains the images for the plots displayed

scripts/
│── Python scripts for data cleaning (Regex)

notebooks/
│── Jupyter Notebooks for NumPy and Pandas analysis

README.md
│── Project documentation and setup instructions
```

---

## 🚀 Setup Instructions

Follow these steps to run the project successfully on your machine.

---

### 1️⃣ Get the Project Files

You can either **clone the repository** or **download it as a ZIP file**.

#### Option A: Clone the Repository

Open your terminal (or VS Code) and run:

```powershell
git clone https://github.com/danmwix/data-science-project.git
cd data-science-project
```

#### Option B: Download ZIP

1. Go to the GitHub repository page
2. Click **Code → Download ZIP**
3. Extract the ZIP file
4. Open a terminal inside the extracted folder

---

### 2️⃣ Create a Virtual Environment

We are using **Python 3.13.2**. Create a virtual environment:

```powershell
python -m venv venv
```

---

### 3️⃣ Activate the Environment

#### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

#### Mac/Linux

```bash
source venv/bin/activate
```

You should now see `(venv)` at the beginning of your terminal line.

---

### 4️⃣ Install Dependencies

While in the virtual environment, make sure to upgrade the version of pip to its latest version

```powershell
python.exe -m pip install --upgrade pip
```

After ensuring that your virtual environment is running the latest version of pip, install the dependencies in the requirements folder

```powershell
pip install -r requirements.txt
```

---

## 🛠 Fixing "Import Could Not Be Resolved" (VS Code)

If you see yellow warnings under imports like `pandas` or `numpy`, your interpreter is incorrect.

### Fix:

1. Open any `.py` file or notebook
2. Press **Ctrl + Shift + P**
3. Search: **Python: Select Interpreter**
4. Select:

   ```
   Python 3.13.x ('venv': venv)
   ```

### For Jupyter Notebooks:

* Click **Select Kernel** (top right)
* Choose the same `venv` environment

---

## 🔍 Running the Project

### Phase 0: VGChartz WebScaper

Run the Webscraping script:

```powershell
python scripts/vgchartz_scraper.py
```

### 📌 Phase 1: Data Cleaning

Run the Regex cleaning script:

```powershell
python scripts/clean_data.py
```

This will generate:

```
data/vgsales_cleaned.csv
```

---

### 📊 Phase 2 & 3: Data Analysis

1. Open the `notebooks/` folder
2. Launch the Jupyter notebooks
3. Click **Run All** to execute the analysis

---

## ✅ Summary

* Clean data using **Regex scripts**
* Analyze using **NumPy & Pandas**
* Visualize using **Matplotlib & Seaborn**
* Organized workflow for easy collaboration

---

## Additional informaiton
### The Web Scraper

The Webscraper scrapes through the vgchartz website that contains a database of videogame entries published throughout the years

The fields scraped for each title include:
- Rank
- Name
- Platform
- Year
- Genre
- Publisher
- Developer
- Critic_Score 
- User_Score
- NA_Sales
- PAL_Sales
- JP_Sales
- Other_Sales
- Global_Sales

The field `Genre` requires us to go to an individual game's page to retrieve that information

Future Impovement:
- Implement a more robust version of asyhnchronous scraping
- Write entries into the csv as you're scraping to prevent losing data during scraping
- Implement a more robust error handling

