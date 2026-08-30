# q2 lowest selling price 


exec(open('setup.py').read())
print("q2: lowest selling price")
print("="*60)

minprice = df['Selling_Price'].min()
print(f"✅ Lowest selling price: ₹{minprice} Lakhs")

#convert to rupess
print(f"💰 In Rupees: ₹{minprice * 100000:,.0f}")

#cheapest car 
cheapest = df[df['Selling_Price'] == minprice]

#Details
print(f"\n Cheapest vehicle details:")
print(cheapest[['Car_Name','Year','Selling_Price','Fuel_Type','Transmission']].to_string(index=False))
print('\n'+ '='*60)
print("q2 completed")