import pandas as pd
import re
import os

# Paths
input_path = os.path.join('data', 'vgsales.csv')
output_path = os.path.join('data', 'vgsales_cleaned.csv')

df = pd.read_csv(input_path)

# 1. Advanced Year Extraction: Handle decimals and N/A
def extract_year(val):
    match = re.search(r'(\d{4})', str(val))
    return int(match.group(1)) if match else None

# 2. String Normalization: Remove non-ASCII characters from Names
# This is great for presentation - "Cleaning for web-compatibility"
def clean_title(text):
    # This regex keeps letters, numbers, and spaces only
    return re.sub(r'[^\x00-\x7F]+', '', str(text))

# 3. Platform Consolidation: Grouping versions
def categorize_platform(name):
    name = str(name).upper()
    if re.search(r'PS|PLAYSTATION', name): return 'Sony PlayStation'
    if re.search(r'XBOX|X360', name): return 'Microsoft Xbox'
    if re.search(r'PC', name): return 'PC'
    if re.search(r'WII|GB|DS|NES|SNES|N64', name): return 'Nintendo'
    return 'Other'

# Apply transformations
df['Year'] = df['Year'].apply(extract_year)
df['Name'] = df['Name'].apply(clean_title)
df['Platform_Brand'] = df['Platform'].apply(categorize_platform)

# Drop rows where year is missing (makes NumPy analysis easier)
df = df.dropna(subset=['Year'])

df.to_csv(output_path, index=False)
print(f"Dataset upgraded! Saved to {output_path}")