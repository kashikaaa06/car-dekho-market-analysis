# ============================================
# Q7: Most Sold Vehicle
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q7: Most Sold Vehicle")
print("="*60)

# Step 1: Find the most sold vehicle
most_sold = df['Car_Name'].value_counts().head(1)
most_sold_name = most_sold.index[0]
most_sold_count = most_sold.values[0]

print(f" Most sold vehicle: {most_sold_name}")
print(f" Sold {most_sold_count} times")

# Step 2: Show top 5 most sold
print(f"\n Top 5 most sold vehicles:")
print(df['Car_Name'].value_counts().head(5))

# Step 3: Create bar chart
plt.figure(figsize=(10,6))
df['Car_Name'].value_counts().head(10).plot(kind='bar', color='coral', edgecolor='black')
plt.title('Top 10 Most Sold Vehicles', fontsize=14, fontweight='bold')
plt.xlabel('Vehicle Model', fontsize=12)
plt.ylabel('Number of Sales', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Step 4: Save and show chart
save_chart('q7_top_vehicles.png')
plt.show()

print("\n" + "="*60)
print(" Q7 Complete!")