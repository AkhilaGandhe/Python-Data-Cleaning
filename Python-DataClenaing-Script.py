
 
import pandas as pd
import numpy as np
import re
 
#  Loading the data
data= pd.read_csv('Python-Data-Cleaning/hr_employee_messy.csv')
print("data.describe()")
 

# Splitting Full_Name column into First_Name and Last_Name
data['Full_Name'] = data['Full_Name'].str.strip().fillna('Unknown')

name_split = data['Full_Name'].str.split()

data['First_Name'] = name_split.str[0].fillna('Unknown')
data['Last_Name'] = name_split.str[-1].fillna('Unknown')
 
 

# 3. Replacing Email and Phone column null values
data['Email'] = data['Email'].str.strip().fillna('Not specified')
data['Phone'] = data['Phone'].str.strip().fillna('Unknown')
 
 

#  Replacing Gender column values to consistent and replacing nulls
gender_map = {
    'f': 'Female', 'F': 'Female', 'female': 'Female', 'FEMALE': 'Female',
    'm': 'Male',   'M': 'Male',   'male': 'Male',     'MALE': 'Male',
    'Other': 'Unknown'
}
data['Gender'] = data['Gender'].map(lambda x: gender_map.get(x, x) if pd.notna(x) else x)
data['Gender'] = data['Gender'].fillna('Unknown')
 
 
# Outliers in Age columns replacing it will NUlls and Replacing nulls with median
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
data.loc[(data['Age'] < 18) | (data['Age'] > 100), 'Age'] = np.nan
data['Age'] = data['Age'].fillna(data['Age'].median()).round(0).astype(int)
 
 

#  Department columns-Replacing the values for consistency and Replacing nulls 
dept_map = {
    'hr': 'Human Resources', 'HR': 'Human Resources', 'Human Resources': 'Human Resources',
    'it': 'IT', 'IT': 'IT', 'Information Technology': 'IT',
    'finance': 'Finance', 'Finance': 'Finance', 'Fin': 'Finance',
    'marketing': 'Marketing', 'Marketing': 'Marketing', 'MARKETING': 'Marketing',
    'sales': 'Sales', 'Sales': 'Sales',
    'operations': 'Operations', 'Operations': 'Operations', 'OPERATIONS': 'Operations',
}
data['Department'] = data['Department'].map(lambda x: dept_map.get(x, x) if pd.notna(x) else x)
data['Department'] = data['Department'].fillna('Not specified')
 
 

# Job_Title and Location columns - Replacing nulls with 'Not specified' and stripping whitespace
data['Job_Title'] = data['Job_Title'].str.strip().fillna('Not specified')
data['Location']  = data['Location'].str.strip().fillna('Not specified')
 
 

#  Joining date-formatting to YYYY-MM-DD and handling nulls
data['Joining_Date'] = pd.to_datetime(data['Joining_Date'], format='mixed', dayfirst=False, errors='coerce')
data['Joining_Date'] = data['Joining_Date'].fillna(pd.Timestamp('2000-01-01'))
data['Joining_Date'] = data['Joining_Date'].dt.strftime('%Y-%m-%d')
 
 

#  YEARS_EXPERIENCE  — convert text words to numbers
word_to_num = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
}
 
def parse_experience(val):
    if pd.isna(val):
        return np.nan
    val_str = str(val).strip().lower()
    # Remove units like 'yrs', 'years', 'year'
    val_str = re.sub(r'\s*(yrs?|years?)\s*', '', val_str).strip()
    # Handle written-out number phrases like 'three years'
    if val_str in word_to_num:
        return float(word_to_num[val_str])
    try:
        return float(val_str)
    except ValueError:
        return np.nan
 
data['Years_Experience'] = data['Years_Experience'].apply(parse_experience)
data['Years_Experience'] = data['Years_Experience'].fillna(data['Years_Experience'].median())
data['Years_Experience'] = data['Years_Experience'].round(0).astype(int)
 
 

#  Annual_Salary_Inr  
data['Annual_Salary_INR'] = (
    data['Annual_Salary_INR']
    .astype(str)
    .str.replace('INR', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)
data['Annual_Salary_INR'] = pd.to_numeric(data['Annual_Salary_INR'], errors='coerce')
data['Annual_Salary_INR'] = data['Annual_Salary_INR'].fillna(data['Annual_Salary_INR'].median()).round(0).astype(int)
 
 

#  Performance_Rating
# 
perf_map = {
    
    '1': 'Poor', '2': 'Average', '3': 'Good', '4': 'High Performer', '5': 'Excellent',

    'poor': 'Poor', 'Poor': 'Poor',
    'average': 'Average', 'Average': 'Average', 'avg': 'Average', 'Avg': 'Average',
    'good': 'Good', 'Good': 'Good', 'GOOD': 'Good',
    'excellent': 'Excellent', 'Excellent': 'Excellent', 'EXCELLENT': 'Excellent',
    'High Performer': 'High Performer',
    'Not Rated': 'Not Rated',
}
data['Performance_Rating'] = data['Performance_Rating'].map(
    lambda x: perf_map.get(str(x).strip(), 'Not Rated') if pd.notna(x) else 'Not Rated'
)
 

# 12. Is_Active  — normalise to boolean True/False

true_vals  = {'1', 'true', 'yes', 'y'}
false_vals = {'0', 'false', 'no', 'n'}
 
def parse_bool(val):
    if pd.isna(val):
        return np.nan
    v = str(val).strip().lower()
    if v in true_vals:
        return True
    if v in false_vals:
        return False
    return np.nan
 
data['Is_Active'] = data['Is_Active'].apply(parse_bool)
data['Is_Active'] = data['Is_Active'].fillna(True)   # default: assume active if unknown
 
 

# Order of columns
ordered_cols = [
    'Employee_ID', 'First_Name', 'Last_Name','Full_Name',
    'Email', 'Phone', 'Gender', 'Age',
    'Department', 'Job_Title', 'Location',
    'Joining_Date', 'Years_Experience', 'Annual_Salary_INR',
    'Performance_Rating', 'Is_Active'
]
data = data[ordered_cols]
data.to_csv('hr_employee_clean.csv', index=False)
print(data.head(5).to_string())
 