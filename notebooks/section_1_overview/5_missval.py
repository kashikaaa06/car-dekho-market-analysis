# ============================================
# Q5: Missing Values Check
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q5: Missing Values Check")
print("="*60)

# Step 1: Check missing values in each column
missing_data = df.isnull().sum()

# Step 2: Count total missing values
total_missing = missing_data.sum()

# Step 3: Check if there are any missing values
if total_missing == 0:
    print(" No missing records found in the dataset!")
    print("All columns have complete data")
else:
    print(f"⚠️ Total missing values: {total_missing}")
    print("\nMissing values by column:")
    print(missing_data[missing_data > 0])

print("\n" + "="*60)
print(" Q5 Complete!")