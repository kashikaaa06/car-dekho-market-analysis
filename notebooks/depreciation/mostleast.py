# ============================================
# Q12: Most and Least Depreciated Vehicle
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q12: Cost Depreciation Analysis")
print("="*60)

# Step 1: Find Most Depreciated Vehicle
most_depreciated = df.loc[df['Depreciation'].idxmax()]

print("🔻 MOST DEPRECIATED VEHICLE:")
print(f"   Vehicle: {most_depreciated['Car_Name']}")
print(f"   Year: {most_depreciated['Year']}")
print(f"   Present Price: ₹{most_depreciated['Present_Price']} Lakhs")
print(f"   Selling Price: ₹{most_depreciated['Selling_Price']} Lakhs")
print(f"   Depreciation: ₹{most_depreciated['Depreciation']:.2f} Lakhs")
print(f"   Depreciation %: {most_depreciated['Depreciation_Percentage']:.2f}%")

# Step 2: Find Least Depreciated Vehicle
least_depreciated = df.loc[df['Depreciation'].idxmin()]

print("\n🔺 LEAST DEPRECIATED VEHICLE:")
print(f"   Vehicle: {least_depreciated['Car_Name']}")
print(f"   Year: {least_depreciated['Year']}")
print(f"   Present Price: ₹{least_depreciated['Present_Price']} Lakhs")
print(f"   Selling Price: ₹{least_depreciated['Selling_Price']} Lakhs")
print(f"   Depreciation: ₹{least_depreciated['Depreciation']:.2f} Lakhs")
print(f"   Depreciation %: {least_depreciated['Depreciation_Percentage']:.2f}%")

# Step 3: Show Top 5 Most Depreciated
print(f"\n Top 5 Most Depreciated Vehicles:")
print(df.nlargest(5, 'Depreciation')[['Car_Name', 'Year', 'Present_Price', 'Selling_Price', 'Depreciation', 'Depreciation_Percentage']].to_string(index=False))

# Step 4: Create Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Most depreciated (bar chart)
df.nlargest(10, 'Depreciation')[['Car_Name', 'Depreciation']].set_index('Car_Name').plot(kind='barh', ax=axes[0], color='red', legend=False)
axes[0].set_title('Top 10 Most Depreciated Vehicles', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Depreciation (Lakhs)')
axes[0].grid(axis='x', alpha=0.3)

# Least depreciated (bar chart)
df.nsmallest(10, 'Depreciation')[['Car_Name', 'Depreciation']].set_index('Car_Name').plot(kind='barh', ax=axes[1], color='green', legend=False)
axes[1].set_title('Top 10 Least Depreciated Vehicles', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Depreciation (Lakhs)')
axes[1].grid(axis='x', alpha=0.3)

plt.tight_layout()
save_chart('q12_depreciation.png')
plt.show()

print("\n" + "="*60)
print(" Q12 Complete!")