# ============================================
# Q14: Factors Affecting Depreciation
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q14: Factors Affecting Cost Depreciation")
print("="*60)

# Step 1: Analyze each factor
factors = ['Year', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']

for factor in factors:
    print(f"\n Depreciation by {factor}:")
    avg_dep = df.groupby(factor)['Depreciation_Percentage'].mean().sort_values()
    print(avg_dep)

# Step 2: Create comprehensive visualization
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Factor 1: Year (Line chart)
df.groupby('Year')['Depreciation_Percentage'].mean().plot(kind='line', marker='o', ax=axes[0,0])
axes[0,0].set_title('Depreciation by Year', fontsize=11, fontweight='bold')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Depreciation %')
axes[0,0].grid(True, alpha=0.3)

# Factor 2: Fuel Type (Bar chart)
df.groupby('Fuel_Type')['Depreciation_Percentage'].mean().plot(kind='bar', ax=axes[0,1])
axes[0,1].set_title('Depreciation by Fuel Type', fontsize=11, fontweight='bold')
axes[0,1].set_xlabel('Fuel Type')
axes[0,1].set_ylabel('Depreciation %')
axes[0,1].tick_params(axis='x', rotation=0)

# Factor 3: Seller Type (Bar chart)
df.groupby('Seller_Type')['Depreciation_Percentage'].mean().plot(kind='bar', ax=axes[0,2])
axes[0,2].set_title('Depreciation by Seller Type', fontsize=11, fontweight='bold')
axes[0,2].set_xlabel('Seller Type')
axes[0,2].set_ylabel('Depreciation %')
axes[0,2].tick_params(axis='x', rotation=0)

# Factor 4: Transmission (Bar chart)
df.groupby('Transmission')['Depreciation_Percentage'].mean().plot(kind='bar', ax=axes[1,0])
axes[1,0].set_title('Depreciation by Transmission', fontsize=11, fontweight='bold')
axes[1,0].set_xlabel('Transmission')
axes[1,0].set_ylabel('Depreciation %')
axes[1,0].tick_params(axis='x', rotation=0)

# Factor 5: Owner (Bar chart)
df.groupby('Owner')['Depreciation_Percentage'].mean().plot(kind='bar', ax=axes[1,1])
axes[1,1].set_title('Depreciation by Owner', fontsize=11, fontweight='bold')
axes[1,1].set_xlabel('Previous Owners')
axes[1,1].set_ylabel('Depreciation %')
axes[1,1].tick_params(axis='x', rotation=0)

# Factor 6: Brand (Top 10)
df.groupby('Brand')['Depreciation_Percentage'].mean().sort_values().head(10).plot(kind='barh', ax=axes[1,2])
axes[1,2].set_title('Top 10 Brands - Least Depreciation', fontsize=11, fontweight='bold')
axes[1,2].set_xlabel('Depreciation %')

plt.tight_layout()
save_chart('q14_depreciation_factors.png')
plt.show()

# Step 3: Key Insights
print("\n KEY INSIGHTS:")
print("="*50)
print("1.  Year: Newer cars have lower depreciation")
print("2.  Fuel: Diesel and Petrol show different depreciation patterns")
print("3.  Seller: Individual sellers often have different pricing")
print("4.  Transmission: Automatic vs Manual affects value retention")
print("5.  Ownership: More owners usually mean higher depreciation")
print("6.  Brand: Luxury brands often retain value better")
print("="*50)

print("\n" + "="*60)
print(" Q14 Complete!")