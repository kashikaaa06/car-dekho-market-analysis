# ============================================
# Q4: Total Records
# ============================================
exec(open('setup.py').read())

print("Q4: Total Records")
print("="*60)

#count total rows 
total_rec = len(df)
print(f"Total records in the dataset:{total_rec}")

# count unique models 
unique = df['Car_Name'].nunique()
print(f"This unique {unique} unique vehicle models")

print("\n" + "="*60)
print(" q4 complete")
