# test_terminal.py - Simple terminal test
import pandas as pd

# Your CSV file path
csv_path = r"C:\Users\Chandan\Downloads\1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv"

print("="*60)
print("🚗 CAR DEKHO - TERMINAL TEST")
print("="*60)

# Load the data
df = pd.read_csv(csv_path)

print(f"\n✅ Data loaded successfully!")
print(f"📊 Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"\n📋 Column Names:")
print(df.columns.tolist())

print(f"\n📋 First 5 rows:")
print(df.head())

print(f"\n📊 Basic Stats:")
print(f"   Average Selling Price: ₹{df['Selling_Price'].mean():.2f} Lakhs")
print(f"   Average Present Price: ₹{df['Present_Price'].mean():.2f} Lakhs")
print(f"   Total Cars: {len(df)}")

print("\n" + "="*60)
print("✅ Terminal test complete!")