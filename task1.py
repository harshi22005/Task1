# ---------------------------------------------
# 🧹 Task 1: Data Cleaning & Preprocessing
# Dataset: Titanic Dataset
# ---------------------------------------------

# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Step 2: Load Dataset
# ⚠ Make sure titanic.csv is in the same folder as this .py file
df = pd.read_csv("C:\\Users\\G HARSHITHA\\Downloads\\Titanic-Dataset.csv")

# Step 3: Basic Information About the Dataset
print("\n🔍 Initial Dataset Info:")
print(df.info())

print("\n📊 Summary Statistics:")
print(df.describe())

print("\n👀 First 5 Rows:")
print(df.head())

# Step 4: Check for Missing Values
print("\n❓ Missing Values Before Cleaning:")
print(df.isnull().sum())

# Step 5: Handle Missing Values
# Fill Age with median
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill Embarked with mode
if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin (too many missing values)
if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

print("\n✅ Missing Values After Cleaning:")
print(df.isnull().sum())

# Step 6: Encode Categorical Features
label = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = label.fit_transform(df[col])

print("\n🔢 Encoded Categorical Columns Successfully!")

# Step 7: Detect and Remove Outliers Using Boxplot
num_cols = df.select_dtypes(include=[np.number]).columns

plt.figure(figsize=(12, 8))
df[num_cols].boxplot()
plt.title("Boxplot Before Removing Outliers")
plt.show()

# Remove outliers using IQR method
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

print("\n🧹 Outliers Removed Successfully!")

# Step 8: Normalize/Standardize Numeric Features
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\n📏 Features Normalized Successfully!")

# Step 9: Display Final Cleaned Data Info
print("\n✅ Final Cleaned Dataset Info:")
print(df.info())

print("\n📋 Sample of Cleaned Data:")
print(df.head())

# Step 10: Save Cleaned Dataset (Optional)
df.to_csv("titanic_cleaned.csv", index=False)
print("\n💾 Cleaned dataset saved as 'titanic_cleaned.csv'")