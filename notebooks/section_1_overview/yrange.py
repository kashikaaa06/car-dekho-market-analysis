# ============================================
# Q1: Manufacturing Year Range
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q1: Manufacturing Year Range")
print("="*60)

# Find min and max year
min_year = df['Year'].min()
max_year = df['Year'].max()

print(f" Oldest car year: {min_year}")
print(f" Newest car year: {max_year}")
print(f" Total years covered: {max_year - min_year + 1} years")

# Year-wise distribution
print(f"\n Year-wise distribution:")
year_counts = df['Year'].value_counts().sort_index()
print(year_counts)

# Create bar chart
plt.figure(figsize=(12,5))
year_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Vehicles by Manufacturing Year', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('../../visualizations/q1_year_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "="*60)
print(" Q1 Complete!")
print(" Chart saved as: visualizations/q1_year_distribution.png")