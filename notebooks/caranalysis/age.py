# ============================================
# Q15: Age and Distance Impact on Price
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q15: Impact of Age and Distance on Selling Price")
print("="*60)

# Step 1: Calculate correlations
correlation_age = df['Age'].corr(df['Selling_Price'])
correlation_km = df['Kms_Driven'].corr(df['Selling_Price'])

print(f" Correlation between Age and Selling Price: {correlation_age:.3f}")
print(f" Correlation between Kms Driven and Selling Price: {correlation_km:.3f}")

# Step 2: Interpret results
print("\n INTERPRETATION:")

# Age interpretation
if correlation_age < -0.5:
    print("   Age:  Strong negative correlation - Older vehicles sell for much less")
elif correlation_age < -0.3:
    print("   Age:  Moderate negative correlation - Older vehicles sell for less")
elif correlation_age < -0.1:
    print("   Age:  Weak negative correlation - Age has some effect on price")
else:
    print("   Age:  No significant correlation - Age doesn't affect price")

# Kms interpretation
if correlation_km < -0.5:
    print("   Kms:  Strong negative correlation - Higher mileage sells for much less")
elif correlation_km < -0.3:
    print("   Kms:  Moderate negative correlation - Higher mileage sells for less")
elif correlation_km < -0.1:
    print("   Kms:  Weak negative correlation - Mileage has some effect on price")
else:
    print("   Kms:  No significant correlation - Mileage doesn't affect price")

# Step 3: Create scatter plots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Age vs Price
scatter1 = axes[0].scatter(df['Age'], df['Selling_Price'], alpha=0.6, c=df['Selling_Price'], cmap='viridis')
axes[0].set_title('Age vs Selling Price', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Age (Years)', fontsize=11)
axes[0].set_ylabel('Selling Price (Lakhs)', fontsize=11)
axes[0].grid(True, alpha=0.3)
plt.colorbar(scatter1, ax=axes[0])

# Add trend line
z = np.polyfit(df['Age'], df['Selling_Price'], 1)
p = np.poly1d(z)
axes[0].plot(df['Age'].sort_values(), p(df['Age'].sort_values()), "r--", linewidth=2, label='Trend Line')
axes[0].legend()

# Kms vs Price
scatter2 = axes[1].scatter(df['Kms_Driven'], df['Selling_Price'], alpha=0.6, c=df['Selling_Price'], cmap='plasma')
axes[1].set_title('Kms Driven vs Selling Price', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Kms Driven', fontsize=11)
axes[1].set_ylabel('Selling Price (Lakhs)', fontsize=11)
axes[1].grid(True, alpha=0.3)
plt.colorbar(scatter2, ax=axes[1])

# Add trend line
z2 = np.polyfit(df['Kms_Driven'], df['Selling_Price'], 1)
p2 = np.poly1d(z2)
axes[1].plot(df['Kms_Driven'].sort_values(), p2(df['Kms_Driven'].sort_values()), "r--", linewidth=2, label='Trend Line')
axes[1].legend()

plt.tight_layout()
save_chart('q15_age_km_impact.png')
plt.show()

# Step 4: Additional Insights
print("\n📊 KEY OBSERVATIONS:")
print("="*50)

# Find average price by age group
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 5, 10, 15, 20, 25], labels=['0-5', '6-10', '11-15', '16-20', '21-25'])
avg_price_by_age = df.groupby('Age_Group')['Selling_Price'].mean()
print("\nAverage Price by Age Group:")
print(avg_price_by_age)

print("\n" + "="*60)
print(" Q15 Complete!")