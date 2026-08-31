# ============================================
# Q24: Newest Car Sold
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q24: Newest Car Sold")
print("="*60)

if len(cars) > 0:
    # Step 1: Find the newest car
    newest_car = cars.loc[cars['Year'].idxmax()]
    
    print(f" Newest Car:")
    print(f"   Model: {newest_car['Car_Name']}")
    print(f"   Year: {newest_car['Year']}")
    print(f"   Selling Price: ₹{newest_car['Selling_Price']} Lakhs")
    print(f"   Present Price: ₹{newest_car['Present_Price']} Lakhs")
    print(f"   Kms Driven: {newest_car['Kms_Driven']}")
    print(f"   Owner: {newest_car['Owner']}")
    print(f"   Seller Type: {newest_car['Seller_Type']}")
    print(f"   Fuel Type: {newest_car['Fuel_Type']}")
    
    # Step 2: Show top 5 newest cars
    print(f"\n Newest Cars (Top 5):")
    print(cars.nlargest(5, 'Year')[['Car_Name', 'Year', 'Selling_Price', 'Kms_Driven', 'Fuel_Type']].to_string(index=False))
    
else:
    print(" No cars found in the dataset")

print("\n" + "="*60)
print(" Q24 Complete!")