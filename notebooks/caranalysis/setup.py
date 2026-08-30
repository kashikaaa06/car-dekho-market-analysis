

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load the data
df = pd.read_csv('../../data/car_data.csv')

# Calculate age (common for Q15)
current_year = 2026
df['Age'] = current_year - df['Year']

print("="*60)
print(" CAR DEKHO MARKET TRENDS ANALYSIS")
print(" SECTION 4: CAR ANALYSIS")
print("="*60)
print(f" Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f" Age calculated for all vehicles")
print("="*60)

# Helper function to save charts
def save_chart(filename):
    os.makedirs('../../visualizations', exist_ok=True)
    plt.savefig(f'../../visualizations/{filename}', dpi=300, bbox_inches='tight')
    print(f" Chart saved: visualizations/{filename}")