# ============================================
# Q11: Single Owner Vehicles
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q11: Single Owner Analysis")
print("="*60)

# Step 1: Count single and multiple owner cars
single_owner = df[df['Owner'] == 0].shape[0]
multiple_owner = df[df['Owner'] > 0].shape[0]

print(f" Single owner vehicles (0 owners before): {single_owner}")
print(f" Multiple owner vehicles: {multiple_owner}")

# Step 2: Show detailed distribution
print(f"\n Ownership Distribution:")
print(df['Owner'].value_counts().sort_index())

# Step 3: Create bar chart
plt.figure(figsize=(8,6))
df['Owner'].value_counts().sort_index().plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Vehicle Ownership Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Number of Previous Owners', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
save_chart('q11_ownership.png')
plt.show()

print("\n" + "="*60)
print(" Q11 Complete!")