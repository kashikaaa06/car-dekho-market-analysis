# ============================================
# Q22: Car Data Extraction
# ============================================

# Import the common setup (cars is already filtered)
exec(open('setup.py').read())

print("Q22: Car Data Analysis")
print("="*60)

# Step 1: Show car count
print(f" Cars found: {len(cars)}")
print(f" Percentage: {len(cars)/len(df)*100:.2f}% of total vehicles")

# Step 2: Show top 10 car models
print(f"\n Top 10 Car Models:")
print(cars['Car_Name'].value_counts().head(10))

# Step 3: Show car brands distribution
print(f"\n Car Brands Distribution:")
brand_counts = cars['Car_Name'].apply(lambda x: x.split()[0] if isinstance(x, str) else x).value_counts()
print(brand_counts.head(10))

# Step 4: Create visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Top car models
cars['Car_Name'].value_counts().head(10).plot(kind='bar', ax=axes[0], color='coral', edgecolor='black')
axes[0].set_title('Top 10 Car Models', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Car Model')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=45)

# Car brands
brand_counts.head(10).plot(kind='bar', ax=axes[1], color='lightblue', edgecolor='black')
axes[1].set_title('Top 10 Car Brands', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Brand')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
save_chart('q22_car_models_brands.png')
plt.show()

print("\n" + "="*60)
print(" Q22 Complete!")