# ============================================
# Q16: Newest Vehicles (After 2014)
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q16: Vehicles Manufactured After 2014")
print("="*60)

# Step 1: Filter vehicles from 2015 onwards
new_vehicles = df[df['Year'] >= 2015]

print(f" Vehicles after 2014: {len(new_vehicles)}")
print(f" Percentage: {len(new_vehicles)/len(df)*100:.2f}% of total vehicles")

# Step 2: Show top 10 newest vehicles
print(f"\n Top 10 Newest Vehicles:")
print(new_vehicles.nlargest(10, 'Year')[['Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Fuel_Type']].to_string(index=False))

# Step 3: Show year-wise distribution
print(f"\n Year-wise distribution (2015+):")
print(new_vehicles['Year'].value_counts().sort_index())

# Step 4: Create visualization
plt.figure(figsize=(10,6))
new_vehicles['Year'].value_counts().sort_index().plot(kind='bar', color='purple', edgecolor='black')
plt.title('Newest Vehicles Distribution (2015+)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
save_chart('q16_newest_vehicles.png')
plt.show()

print("\n" + "="*60)
print(" Q16 Complete!")