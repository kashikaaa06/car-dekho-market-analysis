# ============================================
# Q21: Unexpected Deals in Two-Wheelers
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q21: Unexpected Deals in Two-Wheelers")
print("="*60)

if len(two_wheelers) > 0:
    # Step 1: Calculate expected price based on year
    avg_by_age = two_wheelers.groupby('Year')['Selling_Price'].mean()
    two_wheelers['Expected_Price'] = two_wheelers['Year'].map(avg_by_age)
    two_wheelers['Deal_Indicator'] = two_wheelers['Selling_Price'] - two_wheelers['Expected_Price']
    
    # Step 2: Find best deals (sold above expected)
    best_deals = two_wheelers.nlargest(5, 'Deal_Indicator')
    
    print(" BEST DEALS - Sold above expected price:")
    print(best_deals[['Car_Name', 'Year', 'Selling_Price', 'Expected_Price', 
                       'Kms_Driven', 'Owner', 'Fuel_Type']].to_string(index=False))
    
    # Step 3: Analyze reasons for high deals
    print("\n POSSIBLE REASONS FOR HIGH DEALS:")
    for _, row in best_deals.iterrows():
        print(f"\n    {row['Car_Name']} ({row['Year']}):")
        print(f"      - Sold for ₹{row['Selling_Price']} Lakhs vs expected ₹{row['Expected_Price']:.2f} Lakhs")
        print(f"      - {' Excellent condition' if row['Kms_Driven'] < 10000 else ' High mileage'}")
        print(f"      - {' Single owner' if row['Owner'] == 0 else f' {row["Owner"]+1}th owner'}")
        if row['Fuel_Type'] == 'Petrol':
            print(f"       Petrol engine (popular demand)")
    
    # Step 4: Find worst deals (sold below expected)
    worst_deals = two_wheelers.nsmallest(5, 'Deal_Indicator')
    
    print(f"\n WORST DEALS - Sold below expected price:")
    print(worst_deals[['Car_Name', 'Year', 'Selling_Price', 'Expected_Price', 
                        'Kms_Driven', 'Owner']].to_string(index=False))
    
else:
    print("No two-wheelers found in the dataset")

print("\n" + "="*60)
print(" Q21 Complete!")