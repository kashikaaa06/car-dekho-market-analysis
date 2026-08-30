# ============================================
# COMMON SETUP - Section 2: Vehicle Analysis
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

print("="*60)
print(" CAR DEKHO MARKET TRENDS ANALYSIS")
print("SECTION 2: VEHICLE ANALYSIS")
print("="*60)
print(f" Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print("="*60)

# Helper function to save charts
def save_chart(filename):
    os.makedirs('../../visualizations', exist_ok=True)
    plt.savefig(f'../../visualizations/{filename}', dpi=300, bbox_inches='tight')
    print(f" Chart saved: visualizations/{filename}")