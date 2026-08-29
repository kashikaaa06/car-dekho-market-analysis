# test_visualization.py - Simple visualization test
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your CSV file path
csv_path = r"C:\Users\Chandan\Downloads\1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv"

print("="*60)
print("📊 CAR DEKHO - VISUALIZATION TEST")
print("="*60)

# Load data
df = pd.read_csv(csv_path)
print(f"✅ Data loaded: {df.shape}")

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Top 10 Car Brands
top_cars = df['Car_Name'].value_counts().head(10)
top_cars.plot(kind='barh', ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Top 10 Car Models', fontsize=12)
axes[0, 0].set_xlabel('Count')

# Plot 2: Fuel Type Distribution
df['Fuel_Type'].value_counts().plot(kind='pie', ax=axes[0, 1], autopct='%1.1f%%')
axes[0, 1].set_title('Fuel Type Distribution', fontsize=12)

# Plot 3: Selling Price Distribution
df['Selling_Price'].hist(bins=30, ax=axes[1, 0], color='lightgreen', edgecolor='black')
axes[1, 0].set_title('Selling Price Distribution', fontsize=12)
axes[1, 0].set_xlabel('Price (Lakhs)')

# Plot 4: Present Price vs Selling Price
axes[1, 1].scatter(df['Present_Price'], df['Selling_Price'], alpha=0.5)
axes[1, 1].set_title('Present Price vs Selling Price', fontsize=12)
axes[1, 1].set_xlabel('Present Price (Lakhs)')
axes[1, 1].set_ylabel('Selling Price (Lakhs)')

plt.tight_layout()

# Save the plot
plt.savefig('car_analysis_test.png', dpi=300, bbox_inches='tight')
print("✅ Visualization saved as 'car_analysis_test.png'")

plt.show()
print("✅ Visualization test complete!")