# ============================================
# COMMON SETUP - Section 3: Depreciation Analysis
# This file is imported by all question files
# ============================================

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

# Calculate depreciation (common for all questions in this section)
df['Depreciation'] = df['Present_Price'] - df['Selling_Price']
df['Depreciation_Percentage'] = (df['Depreciation'] / df['Present_Price']) * 100
df['Brand'] = df['Car_Name'].apply(lambda x: x.split()[0] if isinstance(x, str) else x)

print("="*60)
print(" CAR DEKHO MARKET TRENDS ANALYSIS")
print(" SECTION 3: DEPRECIATION ANALYSIS")
print("="*60)
print(f" Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f" Depreciation calculated for all vehicles")
print("="*60)

# Helper function to save charts
def save_chart(filename):
    os.makedirs('../../visualizations', exist_ok=True)
    plt.savefig(f'../../visualizations/{filename}', dpi=300, bbox_inches='tight')
    print(f" Chart saved: visualizations/{filename}")