# ============================================
# Q8: CNG Vehicles
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q8: CNG Vehicles Analysis")
print("="*60)

# Step 1: Count CNG vehicles
cng_count = df[df['Fuel_Type'] == 'CNG'].shape[0]

if cng_count > 0:
    print(f" Yes, there are {cng_count} CNG vehicles in the database")
    print(f" Percentage: {cng_count/len(df)*100:.2f}% of total vehicles")
    
    # Show CNG vehicle details
    print(f"\n CNG Vehicle Details:")
    print(df[df['Fuel_Type'] == 'CNG'][['Car_Name', 'Year', 'Selling_Price', 'Kms_Driven']].to_string(index=False))
else:
    print(" No CNG vehicles found in the database")

# Step 2: Show fuel type distribution
print(f"\n Fuel Type Distribution:")
print(df['Fuel_Type'].value_counts())

# Step 3: Create pie chart
fig, axes = plt.subplots(1, 2, figsize=(12,5))

df['Fuel_Type'].value_counts().plot(kind='pie', ax=axes[0], autopct='%1.1f%%', startangle=90)
axes[0].set_title('Fuel Type Distribution', fontsize=12, fontweight='bold')
axes[0].set_ylabel('')

df['Fuel_Type'].value_counts().plot(kind='bar', ax=axes[1], color='lightblue', edgecolor='black')
axes[1].set_title('Fuel Type Count', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Fuel Type')
axes[1].set_ylabel('Count')

plt.tight_layout()
save_chart('q8_fuel_type.png')
plt.show()

print("\n" + "="*60)
print(" Q8 Complete!")