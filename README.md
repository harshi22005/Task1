# Task1
Titanic Dataset – Data Cleaning & Preprocessing

This project performs **data cleaning, preprocessing, outlier removal, and normalization** on the Titanic dataset.  
It includes all major steps needed before applying Machine Learning algorithms.

---

## 📌 **Features**
✔ Load the Titanic dataset  
✔ Display dataset info, summary stats & sample rows  
✔ Handle missing values (Age, Embarked, Cabin)  
✔ Encode categorical features  
✔ Detect & remove outliers (IQR method)  
✔ Normalize numerical features using StandardScaler  
✔ Save the cleaned dataset as `titanic_cleaned.csv`

---

## 📂 **Project Structure**
project/
│-- harthithag.py # Main Python script
│-- titanic.csv # Original dataset
│-- titanic_cleaned.csv # Output cleaned dataset
│-- README.md # Documentation

yaml
Copy code

---

## 🛠️ **Technologies Used**
- Python 3
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn

---

## ▶️ **How to Run**

1. Install dependencies:
   ```bash
   pip install pandas numpy seaborn matplotlib scikit-learn
Place your Titanic dataset in the same folder.
Example:

Copy code
titanic.csv
Run the Python script:

bash
Copy code
python harshithag.py
After cleaning, the script will generate:

Copy code
titanic_cleaned.csv
🧼 Steps Performed in the Script
1️⃣ Load Dataset
python
Copy code
df = pd.read_csv("titanic.csv")
2️⃣ Clean Missing Values
Age → filled with median

Embarked → filled with mode

Cabin → dropped

3️⃣ Encode Categorical Columns
python
Copy code
LabelEncoder()
4️⃣ Remove Outliers
Using IQR method

5️⃣ Normalize Features
Using:

python
Copy code
StandardScaler()
📊 Visualizations
The script generates a boxplot to show outliers before removal.


