#  HR Employee Data Cleaning Script

A Python script that cleans and standardizes messy HR employee data using **Pandas** and **NumPy**. It handles inconsistent formatting, missing values, outliers, and exports a clean, analysis-ready CSV.

---

##  Project Structure

```
hr-data-cleaning/
├── code.py                    # Main data cleaning script
├── hr_employee_messy.csv      # Raw input file (place in root)
├── hr_employee_clean.csv      # Cleaned output (auto-generated)
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files excluded from version control
└── README.md                  # Project documentation
```

---

##  Requirements

- Python 3.8+
- pandas
- numpy

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/hr-data-cleaning.git
cd hr-data-cleaning
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your raw data

Place your messy HR CSV in the project root:

```
hr_employee_messy.csv
```

### 5. Run the script

```bash
python code.py
```

The cleaned file `hr_employee_clean.csv` will be generated automatically.

---

##  What the Script Does

| Column | Cleaning Applied |
|---|---|
| `Full_Name` | Strips whitespace, fills nulls → splits into `First_Name` / `Last_Name` |
| `Email` | Strips whitespace, fills nulls with `"Not specified"` |
| `Phone` | Strips whitespace, fills nulls with `"Unknown"` |
| `Gender` | Normalizes variants (`f`, `F`, `female`, `FEMALE` → `Female`), fills nulls → `"Unknown"` |
| `Age` | Converts to numeric, removes outliers (< 18 or > 100), fills nulls with median |
| `Department` | Normalizes variants (`hr`, `fin`, `it`, etc.), fills nulls → `"Not specified"` |
| `Job_Title` | Strips whitespace, fills nulls → `"Not specified"` |
| `Location` | Strips whitespace, fills nulls → `"Not specified"` |
| `Joining_Date` | Parses mixed date formats → `YYYY-MM-DD`, fills nulls with `2000-01-01` |
| `Years_Experience` | Converts written words (`"three"`) and unit suffixes (`"5 yrs"`) → int, fills nulls with median |
| `Annual_Salary_INR` | Strips `INR` prefix and commas, converts to numeric, fills nulls with median |
| `Performance_Rating` | Normalizes numeric (1–5) and text variants → categorical labels, fills nulls → `"Not Rated"` |
| `Is_Active` | Normalizes `yes/no/true/false/1/0` → boolean `True`/`False`, fills nulls → `True` |

---

##  Output Column Order

```
Employee_ID, Full_Name, First_Name, Last_Name, Email, Phone, Gender, Age,
Department, Job_Title, Location, Joining_Date, Years_Experience,
Annual_Salary_INR, Performance_Rating, Is_Active
```

---

##  Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

##  License

This project is open source and available under the [MIT License](LICENSE).



