# ============================================
# Q10: Automatic Transmission
# ============================================

# Import the common setup
exec(open('setup.py').read())

print("Q10: Automatic Transmission Analysis")
print("="*60)

# Step 1: Count automatic and manual cars
auto_count = df[df['Transmission'] == 'Automatic'].shape[0]
manual_count = df[df['Transmission'] == 'Manual'].shape[0]

print(f" Automatic transmission vehicles: {auto_count}")
print(f" Manual transmission vehicles: {manual_count}")

# Step 2: Show percentages
print(f"\n Percentage Breakdown:")
print(f"   Automatic: {auto_count/len(df)*100:.2f}%")
print(f"   Manual: {manual_count/len(df)*100:.2f}%")

# Step 3: Create pie chart
fig, axes = plt.subplots(1, 2, figsize=(12,5))

df['Transmission'].value_counts().plot(kind='pie', ax=axes[0], autopct='%1.1f%%', startangle=90)
axes[0].set_title('Transmission Type Distribution', fontsize=12, fontweight='bold')
axes[0].set_ylabel('')

df['Transmission'].value_counts().plot(kind='bar', ax=axes[1], color=['#FFD93D', '#6BCB77'], edgecolor='black')
axes[1].set_title('Transmission Type Count', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Transmission Type')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=0)

plt.tight_layout()
save_chart('q10_transmission.png')
plt.show()

print("\n" + "="*60)
print(" Q10 Complete!")