# ============================================
# Q19: Newest Bike Sold
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q19: Newest Bike Sold")
print("="*60)

if len(two_wheelers) > 0:
    # Step 1: Find the newest bike
    newest_bike = two_wheelers.loc[two_wheelers['Year'].idxmax()]
    
    print(f" Newest Bike:")
    print(f"   Model: {newest_bike['Car_Name']}")
    print(f"   Year: {newest_bike['Year']}")
    print(f"   Selling Price: ₹{newest_bike['Selling_Price']} Lakhs")
    print(f"   Kms Driven: {newest_bike['Kms_Driven']}")
    print(f"   Owner: {newest_bike['Owner']}")
    print(f"   Seller Type: {newest_bike['Seller_Type']}")
    
    # Step 2: Show top 5 newest bikes
    print(f"\n📊 Newest Bikes (Top 5):")
    print(two_wheelers.nlargest(5, 'Year')[['Car_Name', 'Year', 'Selling_Price', 'Kms_Driven']].to_string(index=False))
    
else:
    print(" No two-wheelers found in the dataset")

print("\n" + "="*60)
print(" Q19 Complete!")