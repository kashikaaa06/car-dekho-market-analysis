# ============================================
# Q3: Highest Selling Price
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q3: Highest Selling Price")
print("="*60)

# Step 1: Find the maximum price
max_price = df['Selling_Price'].max()
print(f" Highest selling price: ₹{max_price} Lakhs")

# Step 2: Convert to rupees
print(f" In Rupees: ₹{max_price * 100000:,.0f}")

# Step 3: Find the most expensive car
most_expensive = df[df['Selling_Price'] == max_price]

# Step 4: Show car details
print(f"\n Most expensive vehicle details:")
print(most_expensive[['Car_Name', 'Year', 'Selling_Price', 'Fuel_Type', 'Transmission']].to_string(index=False))

print("\n" + "="*60)
print(" Q3 Complete!")