# Q6: Number of Different Vehicles
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q6: Number of Different Vehicles")
print("="*60)

# count unique car models
unique = df['Car_Name'].nunique()
print(f"Total unique vehicle models:{unique}")

# show top 10 most common vehicles 
print(f"\n Top 10 most common vehicles:")
print(df['Car_Name'].value_counts().head(10))

print("\n" + "="*60)
print("Q6 completed!")

      