# ============================================
# Q25: Unexpected Deals in Cars
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q25: Unexpected Deals in Cars")
print("="*60)

if len(cars) > 0:
    # Step 1: Calculate expected price based on year
    avg_by_year = cars.groupby('Year')['Selling_Price'].mean()
    cars['Expected_Price'] = cars['Year'].map(avg_by_year)
    cars['Deal_Indicator'] = cars['Selling_Price'] - cars['Expected_Price']
    
    # Step 2: Find best deals (sold above expected)
    best_car_deals = cars.nlargest(5, 'Deal_Indicator')
    
    print(" BEST DEALS - Sold above expected price:")
    print(best_car_deals[['Car_Name', 'Year', 'Selling_Price', 'Expected_Price', 
                           'Kms_Driven', 'Owner', 'Fuel_Type', 'Transmission']].to_string(index=False))
    
    # Step 3: Analyze reasons for high deals
    print("\n🔍 POSSIBLE REASONS FOR HIGH CAR DEALS:")
    for _, row in best_car_deals.iterrows():
        print(f"\n    {row['Car_Name']} ({row['Year']}):")
        print(f"      - Sold for ₹{row['Selling_Price']} Lakhs vs expected ₹{row['Expected_Price']:.2f} Lakhs")
        print(f"      - {' Very low mileage' if row['Kms_Driven'] < 15000 else f'{row["Kms_Driven"]} kms driven'}")
        print(f"      - {' Single owner' if row['Owner'] == 0 else f' {row["Owner"]+1}th owner'}")
        print(f"      - {' Automatic transmission (premium)' if row['Transmission'] == 'Automatic' else ' Manual transmission'}")
        if row['Car_Name'] in ['fortuner', 'innova', 'corolla', 'camry', 'land']:
            print(f"      -  Premium brand (Toyota)")
        elif row['Car_Name'] in ['city', 'civic', 'accord']:
            print(f"      -  Premium brand (Honda)")
        else:
            print(f"      - Regular brand")
    
    # Step 4: Find worst deals (sold below expected)
    worst_car_deals = cars.nsmallest(5, 'Deal_Indicator')
    
    print(f"\n WORST DEALS - Sold below expected price:")
    print(worst_car_deals[['Car_Name', 'Year', 'Selling_Price', 'Expected_Price', 
                            'Kms_Driven', 'Owner']].to_string(index=False))
    
else:
    print(" No cars found in the dataset")

print("\n" + "="*60)
print(" Q25 Complete!")