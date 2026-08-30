# ============================================
# Q17: Two-Wheeler Data Extraction
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q17: Two-Wheeler Analysis")
print("="*60)

# Step 1: Define bike brands
bike_brands = ['Royal Enfield', 'KTM', 'Bajaj', 'TVS', 'Yamaha', 'Honda', 
               'Hero', 'Suzuki', 'Hyosung', 'Mahindra', 'UM', 'Activa', 'Apache']

# Step 2: Filter two-wheelers
two_wheelers = df[df['Car_Name'].str.contains('|'.join(bike_brands), case=False)]

print(f" Two-wheelers found: {len(two_wheelers)}")
print(f" Percentage: {len(two_wheelers)/len(df)*100:.2f}% of total vehicles")

# Step 3: Show top 10 bike models
print(f"\n🚲 Top 10 Two-Wheeler Models:")
print(two_wheelers['Car_Name'].value_counts().head(10))

# Step 4: Show bike brands
print(f"\nTwo-Wheeler Brands:")
print(two_wheelers['Car_Name'].apply(lambda x: x.split()[0] if isinstance(x, str) else x).value_counts().head(10))

# Step 5: Create visualization
plt.figure(figsize=(10,6))
two_wheelers['Car_Name'].value_counts().head(10).plot(kind='bar', color='orange', edgecolor='black')
plt.title('Top 10 Two-Wheeler Models', fontsize=14, fontweight='bold')
plt.xlabel('Two-Wheeler Model', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
save_chart('q17_two_wheelers.png')
plt.show()

print("\n" + "="*60)
print("Q17 Complete!")