# ============================================
# Q13: Brands Least Affected by Depreciation
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q13: Brands with Least Depreciation")
print("="*60)

# Step 1: Calculate average depreciation by brand
brand_depreciation = df.groupby('Brand')['Depreciation_Percentage'].mean().sort_values()

# Step 2: Show best and worst brands
print(" Brands with Least Depreciation (Best Value Retention):")
print(brand_depreciation.head(10))

print("\nBrands with Most Depreciation (Worst Value Retention):")
print(brand_depreciation.tail(10))

# Step 3: Create visualization
plt.figure(figsize=(12,8))
brand_depreciation.head(15).plot(kind='barh', color='green', edgecolor='black')
plt.title('Brands with Least Depreciation (Best Value Retention)', fontsize=14, fontweight='bold')
plt.xlabel('Average Depreciation %', fontsize=12)
plt.ylabel('Brand', fontsize=12)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
save_chart('q13_brand_depreciation.png')
plt.show()

print("\n" + "="*60)
print(" Q13 Complete!")