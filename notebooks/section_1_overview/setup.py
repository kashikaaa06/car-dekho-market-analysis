import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

df = pd.read_csv('../../data/car_data.csv')
print("="*60)
print("Car dekho market trends analysis")
print("Section 1: Data overview")
print("="*60)
print(f"Data loaded with {df.shape[0]} rows and {df.shape[1]} columns")
print(f"columns:{df.columns.tolist()}")
print("="*60)
