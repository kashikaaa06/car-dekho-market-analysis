# ============================================
# Q9: Individual Sellers
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q9: Individual Seller Analysis")
print("="*60)

# Step 1: Count individual and dealer sellers
individual_count = df[df['Seller_Type'] == 'Individual'].shape[0]
dealer_count = df[df['Seller_Type'] == 'Dealer'].shape[0]

print(f" Individual sellers: {individual_count} vehicles")
print(f" Dealer sellers: {dealer_count} vehicles")

# Step 2: Show percentages
print(f"\nPercentage Breakdown:")
print(f"   Individual: {individual_count/len(df)*100:.2f}%")
print(f"   Dealer: {dealer_count/len(df)*100:.2f}%")

# Step 3: Create bar chart
plt.figure(figsize=(8,6))
df['Seller_Type'].value_counts().plot(kind='bar', color=['#FF6B6B', '#4ECDC4'], edgecolor='black')
plt.title('Seller Type Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Seller Type', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
save_chart('q9_seller_type.png')
plt.show()

print("\n" + "="*60)
print(" Q9 Complete!")