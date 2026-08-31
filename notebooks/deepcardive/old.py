# ============================================
# Q23: Oldest Car Sold
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q23: Oldest Car Sold")
print("="*60)

if len(cars) > 0:
    # Step 1: Find the oldest car
    oldest_car = cars.loc[cars['Year'].idxmin()]
    
    print(f" Oldest Car:")
    print(f"   Model: {oldest_car['Car_Name']}")
    print(f"   Year: {oldest_car['Year']}")
    print(f"   Selling Price: ₹{oldest_car['Selling_Price']} Lakhs")
    print(f"   Present Price: ₹{oldest_car['Present_Price']} Lakhs")
    print(f"   Kms Driven: {oldest_car['Kms_Driven']}")
    print(f"   Owner: {oldest_car['Owner']}")
    print(f"   Seller Type: {oldest_car['Seller_Type']}")
    print(f"   Fuel Type: {oldest_car['Fuel_Type']}")
    
    # Step 2: Show top 5 oldest cars
    print(f"\n Oldest Cars (Top 5):")
    print(cars.nsmallest(5, 'Year')[['Car_Name', 'Year', 'Selling_Price', 'Kms_Driven', 'Fuel_Type']].to_string(index=False))
    
else:
    print(" No cars found in the dataset")

print("\n" + "="*60)
print(" Q23 Complete!")