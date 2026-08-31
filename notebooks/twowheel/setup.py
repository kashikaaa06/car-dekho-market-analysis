# ============================================
# COMMON SETUP - Section 5: Two-Wheeler Analysis
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

# Define bike brands (common for all questions in this section)
bike_brands = ['Royal Enfield', 'KTM', 'Bajaj', 'TVS', 'Yamaha', 'Honda', 
               'Hero', 'Suzuki', 'Hyosung', 'Mahindra', 'UM', 'Activa', 'Apache', 
               'Hornet', 'Karizma', 'Pulsar', 'Dominar', 'Mojo', 'Reno']

# Filter two-wheelers
two_wheelers = df[df['Car_Name'].str.contains('|'.join(bike_brands), case=False)]

print("="*60)
print(" CAR DEKHO MARKET TRENDS ANALYSIS")
print(" SECTION 5: TWO-WHEELER ANALYSIS")
print("="*60)
print(f" Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f" Two-wheelers found: {len(two_wheelers)}")
print("="*60)

# Helper function to save charts
def save_chart(filename):
    os.makedirs('../../visualizations', exist_ok=True)
    plt.savefig(f'../../visualizations/{filename}', dpi=300, bbox_inches='tight')
    print(f" Chart saved: visualizations/{filename}")