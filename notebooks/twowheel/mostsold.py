# ============================================
# Q20: Most Sold Bike
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q20: Most Sold Bike")
print("="*60)

if len(two_wheelers) > 0:
    # Step 1: Find the most sold bike
    most_sold_bike = two_wheelers['Car_Name'].value_counts().head(1)
    most_sold_name = most_sold_bike.index[0]
    most_sold_count = most_sold_bike.values[0]
    
    print(f" Most Sold Bike:")
    print(f"   Model: {most_sold_name}")
    print(f"   Count: {most_sold_count} sales")
    
    # Step 2: Show top 10 most sold bikes
    print(f"\n Top 10 Most Sold Bikes:")
    print(two_wheelers['Car_Name'].value_counts().head(10))
    
    # Step 3: Create visualization
    plt.figure(figsize=(10,6))
    two_wheelers['Car_Name'].value_counts().head(10).plot(kind='bar', color='orange', edgecolor='black')
    plt.title('Top 10 Most Sold Bikes', fontsize=14, fontweight='bold')
    plt.xlabel('Bike Model', fontsize=12)
    plt.ylabel('Number of Sales', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    save_chart('q20_most_sold_bike.png')
    plt.show()
    
else:
    print(" No two-wheelers found in the dataset")

print("\n" + "="*60)
print(" Q20 Complete!")