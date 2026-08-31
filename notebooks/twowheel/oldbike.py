# ============================================
# Q18: Oldest Bike Sold
# ============================================

# Import the common setup (two_wheelers is already filtered)
exec(open('setup.py').read())

print("Q18: Oldest Bike Sold")
print("="*60)

# Check if there are any two-wheelers
if len(two_wheelers) > 0:
    # Step 1: Find the oldest bike
    oldest_bike = two_wheelers.loc[two_wheelers['Year'].idxmin()]
    
    print(f" Oldest Bike:")
    print(f"   Model: {oldest_bike['Car_Name']}")
    print(f"   Year: {oldest_bike['Year']}")
    print(f"   Selling Price: ₹{oldest_bike['Selling_Price']} Lakhs")
    print(f"   Kms Driven: {oldest_bike['Kms_Driven']}")
    print(f"   Owner: {oldest_bike['Owner']}")
    print(f"   Seller Type: {oldest_bike['Seller_Type']}")
    
    # Step 2: Show top 5 oldest bikes
    print(f"\n📊 Oldest Bikes (Top 5):")
    print(two_wheelers.nsmallest(5, 'Year')[['Car_Name', 'Year', 'Selling_Price', 'Kms_Driven']].to_string(index=False))
    
else:
    print("❌ No two-wheelers found in the dataset")

print("\n" + "="*60)
print(" Q18 Complete!")