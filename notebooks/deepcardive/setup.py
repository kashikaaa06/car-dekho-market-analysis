# ============================================
# COMMON SETUP - Section 6: Car Deep Dive
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

# Define bike brands (to exclude from cars)
bike_brands = ['Royal Enfield', 'KTM', 'Bajaj', 'TVS', 'Yamaha', 'Honda', 
               'Hero', 'Suzuki', 'Hyosung', 'Mahindra', 'UM', 'Activa', 'Apache', 
               'Hornet', 'Karizma', 'Pulsar', 'Dominar', 'Mojo', 'Reno']

# Define car brands (to include only cars)
car_brands = ['ritz', 'sx4', 'ciaz', 'wagon', 'swift', 'vitara', 'ertiga', 'dzire', 
              'alto', 'ignis', 'baleno', 'omni', 'fortuner', 'innova', 'corolla', 
              'etios', 'camry', 'land', 'i20', 'i10', 'eon', 'xcent', 'elantra', 
              'creta', 'verna', 'city', 'brio', 'amaze', 'jazz', 'grand', 's-cross']

# Filter cars (exclude bikes, keep only cars)
cars = df[~df['Car_Name'].str.contains('|'.join(bike_brands), case=False)]
cars = cars[cars['Car_Name'].str.contains('|'.join(car_brands), case=False)]

print("="*60)
print(" CAR DEKHO MARKET TRENDS ANALYSIS")
print(" SECTION 6: CAR DEEP DIVE")
print("="*60)
print(f" Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f" Cars found: {len(cars)}")
print(f" Percentage: {len(cars)/len(df)*100:.2f}% of total vehicles")
print("="*60)

# Helper function to save charts
def save_chart(filename):
    os.makedirs('../../visualizations', exist_ok=True)
    plt.savefig(f'../../visualizations/{filename}', dpi=300, bbox_inches='tight')
    print(f" Chart saved: visualizations/{filename}")